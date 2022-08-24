# starter script to demonstrate the Bayesian strategy analysis
#  a singular strategy called go_left
# uses testdata from Rat 2 in Peyrache Y-maze testdata-set
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import strategymodels

from Functions.set_Beta_prior import set_priors
from Functions.update_strategy_posterior_probability import update_strategy_posterior_probability
from Functions.Summaries_of_Beta_distribution import summaries_of_Beta_Distribution
from Functions.plotSessionStructure import plotSessionStructure

# initiate TestData variable so that rat 2 testdata can be loaded
TestData = pd.read_csv('data.csv')

prior_type = "Uniform"  # choosing prior type

[alpha0, beta0] = set_priors(prior_type)  # define priors

decay_rate = 0.9  # Set Decay rate (gamma)

no_Trials = np.size(TestData.TrialIndex)

success_total = 0  # initialise variables to zero
failure_total = 0

Output = pd.DataFrame(columns = ['Alpha', 'Beta', 'MAPprobability', 'Precision'])  # empty Dataframe to input data into

#%% run strategy analysis
for trial in range(len(TestData)):
    rows_of_data = TestData.iloc[0:trial+1]     # select all rows of data up to the curren trial; is trial+1 as dataframe includes column row as row 0????
    trial_type = strategymodels.go_left(rows_of_data)          # test whether go-left was used       
        
    [success_total, failure_total, Alpha, Beta] = update_strategy_posterior_probability(trial_type, decay_rate,
                                                                                        success_total, failure_total,
                                                                                        alpha0, beta0)
    MAPprobability = summaries_of_Beta_Distribution(Alpha, Beta, 'MAP')
    precision = summaries_of_Beta_Distribution(Alpha, Beta, 'precision')
    
    #store output of analysis on this trial
    new_row = {'Alpha':Alpha, 'Beta':Beta, 'MAPprobability':MAPprobability, 'Precision':precision}     # create new row for dataframe as a dict
    new_df= pd.DataFrame([new_row])   # have to convert to dataframe to use concat!!
    Output = pd.concat([Output, new_df], ignore_index=True)       # add new row to dataframe

# save output    
Output.to_csv('Output.csv', index=False, )  # creates a csv of the output of Alpha, Beta, MAPprobabitlity and Precision

# plotting time series of MAPprobability
plt.figure(figsize=(10, 5))
plt.plot(Output.MAPprobability, linewidth=0.75)  # plots the time series
plt.axis([0, no_Trials, 0, 1.25])  # establishes axis limits
plt.xlabel('Trials'), plt.ylabel('P(Strategy)')  # labelling the axis
plt.axhline(y=0.5, color='firebrick', linestyle='--', linewidth=0.75,
            label="Chance")  # shows the line at which Chance is exceeded

plotSessionStructure(TestData)

plt.show()
