import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import strategymodels

from Functions.set_Beta_prior import set_priors
from Functions.update_strategy_posterior_probability import update_strategy_posterior_probability
from Functions.Summaries_of_Beta_distribution import summaries_of_Beta_Distribution
from Functions.plotSessionStructure import plotSessionStructure
from Functions.interpolate_null_trials import interpolate_null_trials

# initiate TestData variable so that rat 2 testdata can be loaded
TestData = pd.read_csv('data.csv')

#  choose strategies to evaluate: subset shown in Figure 1
strategies = ['go_left','go_right','go_cued','win_stay_spatial','lose_shift_cued','lose_shift_spatial']

# set prior
prior_type = 'Uniform' #set prior type
decay_rate = 0.9

[alpha0, beta0] = set_priors(prior_type)  # define priors


#%% initialise storage
Output_collection = {} # empty dict in which to store dataframes
event_totals = {}   # empty dict to store totals of events for each strategy
# initialise dataframes
for index_strategy in range(len(strategies)):
    Output_collection[strategies[index_strategy]] =  pd.DataFrame(columns = ['Alpha', 'Beta','MAPprobability', 'Precision','Alpha_interpolated', 'Beta_interpolated','MAPprobability_interpolated', 'Precision_interpolated'])  # empty Dataframe to input data into
    event_totals[strategies[index_strategy]] = {}; # create empty dict for this strategy
    event_totals[strategies[index_strategy]]['success_total'] = 0;
    event_totals[strategies[index_strategy]]['failure_total'] = 0;

#%%
for trial in range(len(TestData)):
    
    rows_of_data = TestData.iloc[0:trial+1]     # select all rows of data up to the curren trial; is trial+1 as dataframe includes colu   
     
   #%% 
    for index_strategy in range(len(strategies)):
       # run current strategy model on data up to current trial 
       strategy_fcn = getattr(strategymodels,strategies[index_strategy])  # dynamically assign string as function to be called
       trial_type = strategy_fcn(rows_of_data)   #call currently assigned function
     
       # update probability of strategy
       [event_totals[strategies[index_strategy]]['success_total'], event_totals[strategies[index_strategy]]['failure_total'], Alpha, Beta] \
           = update_strategy_posterior_probability(trial_type, decay_rate,event_totals[strategies[index_strategy]]['success_total'], event_totals[strategies[index_strategy]]['failure_total'],alpha0, beta0)
               
       MAPprobability = summaries_of_Beta_Distribution(Alpha, Beta, 'MAP')
       precision = summaries_of_Beta_Distribution(Alpha, Beta, 'precision')
      
              
       #%% interpolate null trials
       this_trials_data= {'Alpha':Alpha, 'Beta':Beta, 'MAPprobability':MAPprobability, 'Precision':precision}     # create dict of current data to pass
       if trial > 0:
           previous_trials_data = Output_collection[strategies[index_strategy]].iloc[trial-1] 
       else:
           previous_trials_data = Output_collection[strategies[index_strategy]]  # pass empty dataframe
           
       new_row_of_data = interpolate_null_trials(this_trials_data,previous_trials_data,alpha0,beta0)
       
       # store results  - dynamically-defined dataframe...
       new_df= pd.DataFrame([new_row_of_data])   # have to convert to dataframe to use concat!!
       Output_collection[strategies[index_strategy]] = pd.concat([Output_collection[strategies[index_strategy]], new_df], ignore_index=True)       # add new row to dataframe
      
      
#%% plot results
no_Trials = np.size(TestData.TrialIndex)

# plotting time series of MAPprobability for Rule Strategies
plt.figure(figsize=(10, 5))
plt.plot(Output_collection['go_left'].MAPprobability, linewidth=0.75)  # plots the time series
plt.plot(Output_collection['go_right'].MAPprobability, linewidth=0.75, color=(0.4, 0.8, 0.5))  # plots the time series
plt.plot(Output_collection['go_cued'].MAPprobability, linewidth=0.75, color=(0.8,0.6,0.5))  # plots the time series
plt.axis([0, no_Trials, 0, 1.25])  # establishes axis limits 
plt.xlabel('Trials'), plt.ylabel('P(Strategy)')  # labelling the axis
plt.axhline(y=0.5, color='darkgrey', linewidth=0.75, label="Chance")  # shows the line at which Chance is exceeded

plotSessionStructure(TestData)
plt.show()       

# plotting Precision for the same three strategies (precision identical for go_left and go_right)
plt.figure(figsize=(10, 5))
plt.plot(Output_collection['go_left'].Precision, linewidth=0.75)  # plots the time series
plt.plot(Output_collection['go_cued'].Precision, linewidth=0.75, color=(0.8,0.6,0.5))  # plots the time series
plt.xlabel('Trials'), plt.ylabel('Precision')  # labelling the axis
plt.show()      
       

# plotting MAP probability for some exploratory strategies - use interpolated values
plt.figure(figsize=(10, 5))
plt.plot(Output_collection['lose_shift_cued'].MAPprobability_interpolated, linewidth=0.75, color=(1, 0.1, 0.6))  # plots the time series
plt.plot(Output_collection['lose_shift_spatial'].MAPprobability_interpolated, linewidth=0.75, color=(0.8, 0.6, 0.5))  # plots the time series
plt.plot(Output_collection['win_stay_spatial'].MAPprobability_interpolated, linewidth=0.75, color=(0.4,0.8,0.5))  # plots the time series
plt.axis([0, no_Trials, 0, 1.25])  # establishes axis limits 
plt.xlabel('Trials'), plt.ylabel('P(Strategy)')  # labelling the axis
plt.axhline(y=0.5, color='darkgrey', linewidth=0.75, label="Chance")  # shows the line at which Chance is exceeded

plotSessionStructure(TestData)
plt.show()  