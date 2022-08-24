import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import strategymodels

#from strategy_models.go_left import go_left
#from strategy_models.go_right import go_right
#from strategy_models.alternate import alternate
from Functions.set_Beta_prior import set_priors
from Functions.update_strategy_posterior_probability import update_strategy_posterior_probability
from Functions.Summaries_of_Beta_distribution import summaries_of_Beta_Distribution

# initiate TestData variable so that rat 2 testdata can be loaded
TestData = pd.read_csv('data.csv')

#  choose strategies to evaluate: subset shown in Figure 1
strategies = ['go_left','go_right']

# set prior
prior_type = 'Uniform' #set prior type
decay_rate = 0.9

[alpha0, beta0] = set_priors(prior_type)  # define priors

no_Trials = np.size(TestData.TrialIndex)


#%% initialise storage
Output_collection = {} # empty dict in which to store dataframes
event_totals = {}   # empty dict to store totals of events for each strategy
# initialise dataframes
for index_strategy in range(len(strategies)):
    Output_collection[strategies[index_strategy]] =  pd.DataFrame(columns = ['Alpha', 'Beta', 'MAPprobability', 'Precision'])  # empty Dataframe to input data into
    event_totals[strategies[index_strategy]] = {}; # create empty dict for this strategy
    event_totals[strategies[index_strategy]]['success_total'] = 0;
    event_totals[strategies[index_strategy]]['failure_total'] = 0;

#%%
for trial in range(len(TestData)):
    
    rows_of_data = TestData.iloc[0:trial+1]     # select all rows of data up to the curren trial; is trial+1 as dataframe includes colu   
     
    print(rows_of_data)
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
    
       # store results  - dynamically-defined dataframe...
       new_row = {'Alpha':Alpha, 'Beta':Beta, 'MAPprobability':MAPprobability, 'Precision':precision}     # create new row for dataframe as a dict
       new_df= pd.DataFrame([new_row])   # have to convert to dataframe to use concat!!
       Output_collection[strategies[index_strategy]] = pd.concat([Output_collection[strategies[index_strategy]], new_df], ignore_index=True)       # add new row to dataframe
       
#%% plot results
# plotting time series of MAPprobability
plt.figure(figsize=(10, 5))
plt.plot(Output_collection['go_right'].MAPprobability, linewidth=0.75)  # plots the time series
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
       
       