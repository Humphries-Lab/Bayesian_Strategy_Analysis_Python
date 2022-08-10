# starter script to demonstrate the Bayesian strategy analysis
#  a singular strategy called go_left
# uses testdata from Rat 2 in Peyrache Y-maze testdata-set
import numpy as np
import pandas as pd
from Functions.set_Beta_prior import set_priors
from strategy_models.go_right import go_right
from Functions.Summaries_of_Beta_distribution import summaries_of_Beta_Distribution
from Functions.update_strategy_posterior_probability import update_strategy_posterior_probability

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

for rows in TestData.itertuples():
    (go_right(TestData))
    print(trial_type)




