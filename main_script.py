# starter script to demonstrate the Bayesian strategy analysis
#  a singular strategy called go_left
# uses testdata from Rat 2 in Peyrache Y-maze testdata-set
import sys
import numpy as np
import pandas as pd
from Functions.set_Beta_prior import set_priors
from strategy_models.go_left import go_left
from Functions.update_strategy_posterior_probability import update_strategy_posterior_probability
from Functions.Summaries_of_Beta_distribution import summaries_of_Beta_Distribution

sys.path.append("/Functions")
sys.path.append("/strategy_models")
sys.path.append("/Processed Data")

# add numpy so the Peyrache testdata can be loaded
# initiate TestData variable so that rat 2 testdata can be loaded


TestData = pd.read_csv('data.csv')

# choosing prior type
prior_type = "Uniform"

# define priors


alpha0 = set_priors(prior_type)
beta0 = alpha0

# Set Decay rate (gamma)
decay_rate = 0.9

# main loop: for each trial, update strategy index


no_Trials = np.size(TestData.TrialIndex)
# initialise storage
Alpha = np.zeros(no_Trials)
Beta = Alpha
MAPprobability = np.zeros((no_Trials, 1))
precision = MAPprobability

success_total = 0  # initialise variables to zero
failure_total = 0

Output = pd.DataFrame()

for rows in TestData.Choice:
    trial_type = go_left(rows)

    [success_total, failure_total, Alpha, Beta] = update_strategy_posterior_probability(trial_type, decay_rate,
                                                                                        success_total, failure_total,
                                                                                        alpha0, beta0)
    MAPprobability = summaries_of_Beta_Distribution(Alpha, Beta, 'MAP')
    precision = summaries_of_Beta_Distribution(Alpha, Beta, 'precision')
    loop = pd.DataFrame([Alpha, Beta, MAPprobability, precision], )
    Output = (pd.concat([Output, loop], axis=1))
Output = Output.T
Output.columns = ['Alpha', 'Beta', 'MAPprobability', 'Precision']

Output.to_csv('Output.csv', index=False)

# plotting time series of MAPprobability and precision
