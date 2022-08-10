import numpy as np
import pandas as pd
import os
os.add_dll_directory(Functions)
import matplotlib.pyplot as plt

from strategy_models.go_left import go_left
from strategy_test.go_right import go_right
from strategy_models.alternate import alternate
from Functions.update_strategy_posterior_probability import update_strategy_posterior_probability
from Functions.Summaries_of_Beta_distribution import summaries_of_Beta_Distribution

# initiate TestData variable so that rat 2 testdata can be loaded
TestData = pd.read_csv('data.csv')

#  choose strategies to evaluate: subset shown in Figure 1

prior_type = 'Uniform' #set prior type
decay_rate = 0.9

[alpha0, beta0] = set_priors(prior_type)  # define priors

no_Trials = np.size(TestData.TrialIndex)

for rows in TestData.itertuples():
    TestData.apply(go_ri)
