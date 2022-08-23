# starter script to demonstrate the Bayesian strategy analysis
#  a singular strategy called go_left
# uses testdata from Rat 2 in Peyrache Y-maze testdata-set
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Functions.set_Beta_prior import set_priors
from strategy_models.go_left import go_left
from Functions.update_strategy_posterior_probability import update_strategy_posterior_probability
from Functions.Summaries_of_Beta_distribution import summaries_of_Beta_Distribution

# initiate TestData variable so that rat 2 testdata can be loaded
TestData = pd.read_csv('data.csv')

prior_type = "Uniform"  # choosing prior type

[alpha0, beta0] = set_priors(prior_type)  # define priors

decay_rate = 0.9  # Set Decay rate (gamma)

# MAIN LOOP: FOR EACH TRIAL TO UPDATE STRATEGY INDEX

no_Trials = np.size(TestData.TrialIndex)

Alpha = 0   # initialises storage
Beta = 0 
MAPprobability = 0 
precision = 0

success_total = 0  # initialise variables to zero
failure_total = 0

Output = pd.DataFrame(columns = ['Alpha', 'Beta', 'MAPprobability', 'Precision'])  # empty Dataframe to input data into

#%% run strategy analysis
for trial in range(len(TestData)):
    rows_of_data = TestData.iloc[0:trial+1]     # select all rows of data up to the curren trial; is trial+1 as dataframe includes column row as row 0????
    trial_type = go_left(rows_of_data)          # test whether go-left was used       
        
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
sessionLines = TestData[TestData['NewSessionTrials'] == 1].index  # indices list  when new session was started
plt.vlines(sessionLines, 0, 1, colors='lightgray', linestyles='--', linewidth=0.75,
           label="New Sessions")  # vertical lines indicate the new session trials
ruleLines = np.array(TestData[TestData['RuleChangeTrials'] == 1].index)  # indices list  when new session was started
ruleLines = np.insert(ruleLines, 0, 0)  # sets array for x values of rule change

for x in ruleLines:  # to get shade change for rule change and labels
    minx = x / no_Trials
    plt.axhspan(1, 1.25, xmin=minx, alpha=0.3, edgecolor='k')  # change transparency for separation
    plt.axvline(x, 0.8, 1)  # dividing lines

#  creating labels
plt.text(1, 1.125, "Right Arm", label='Go to the Right')
plt.text(120, 1.125, "Lit Arm", label='Go to the Lit Arm')
plt.text(225, 1.125, "Left Arm", label='Go to the Left')
plt.text(330, 1.125, "Unlit Arm", label='Go to the Dark Arm')
plt.text(150, 1.3, "Rule for Reward")
plt.legend()  # add legend
plt.show()
