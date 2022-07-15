# starter script to demonstrate the Bayesian strategy analysis
#  a singular strategy called go_left
# uses testdata from Rat 2 in Peyrache Y-maze testdata-set
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
from Functions.set_Beta_prior import set_priors
from strategy_models.go_left import go_left
from Functions.update_strategy_posterior_probability import update_strategy_posterior_probability
from Functions.Summaries_of_Beta_distribution import summaries_of_Beta_Distribution

sys.path.append("/Functions")
sys.path.append("/strategy_models")
sys.path.append("/Processed Data")

# initiate TestData variable so that rat 2 testdata can be loaded
TestData = pd.read_csv('data.csv')

prior_type = "Uniform"  # choosing prior type

[alpha0, beta0] = set_priors(prior_type)  # define priors

decay_rate = 0.9  # Set Decay rate (gamma)

# MAIN LOOP: FOR EACH TRIAL TO UPDATE STRATEGY INDEX

no_Trials = np.size(TestData.TrialIndex)

Alpha = np.zeros(no_Trials)  # initialises storage
Beta = Alpha
MAPprobability = np.zeros((no_Trials, 1))
precision = MAPprobability

success_total = 0  # initialise variables to zero
failure_total = 0

Output = pd.DataFrame()  # empty Dataframe to input data into

for rows in TestData.Choice:
    trial_type = go_left(rows)

    [success_total, failure_total, Alpha, Beta] = update_strategy_posterior_probability(trial_type, decay_rate,
                                                                                        success_total, failure_total,
                                                                                        alpha0, beta0)
    MAPprobability = summaries_of_Beta_Distribution(Alpha, Beta, 'MAP')
    precision = summaries_of_Beta_Distribution(Alpha, Beta, 'precision')
    loop = pd.DataFrame([Alpha, Beta, MAPprobability, precision], )
    Output = pd.concat([Output, loop], axis=1, ignore_index=True)
Output = Output.T
Output.columns = ['Alpha', 'Beta', 'MAPprobability', 'Precision']

Output.to_csv('Output.csv', index=False, )  # creates a csv of the output of Alpha, Beta, MAPprobabitlity and Precision

# plotting time series of MAPprobability
plt.figure(figsize=(10,5))
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
    plt.axhspan(1, 1.25, xmin=minx, alpha=0.3, edgecolor = 'k')  # change transparency for separation
    plt.axvline(x, 0.8, 1)  # dividing lines

#  creating labels
plt.text(11, 1.125, "1", label = 'Go to the Right')
plt.text(143.5, 1.125, "2", label = 'Go to the Lit Arm')
plt.text(248.5, 1.125, "3", label = 'Go to the Left')
plt.text(335, 1.125, "4", label = 'Go to the Dark Arm')
plt.legend()  # add legend
plt.show()
