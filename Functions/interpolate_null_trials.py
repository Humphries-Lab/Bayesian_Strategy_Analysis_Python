#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 12:14:59 2022

@author: Mark Humphries
"""
import numpy as np
from Functions.Summaries_of_Beta_distribution import summaries_of_Beta_Distribution

# trial_data is a dict of {Alpha,Beta,MAPprobability,Precision}
# dataframe_row_of_prior_trials is a Pandas dataframe row of the previous trial
# (or the empty dataframe on the first trial)

def interpolate_null_trials(dict_of_trial_data,dataframe_row_of_prior_trial,alpha_zero,beta_zero):
    
    # if not NAN, then no need to interpolate: just assign the supdated alpha etc to the interpolated variables
    if not np.isnan(dict_of_trial_data['Alpha']):
        interpolated_values = {'Alpha_interpolated': dict_of_trial_data['Alpha'], 'Beta_interpolated': dict_of_trial_data['Beta'], \
                      'MAPprobability_interpolated': dict_of_trial_data['MAPprobability'], 'Precision_interpolated': dict_of_trial_data['Precision']}
       
      
    elif dataframe_row_of_prior_trial.empty:
    # it is a null trial: check if dataframe row is empty - then is first trial, so assign priors
         MAPprobability = summaries_of_Beta_Distribution(alpha_zero,beta_zero,'MAP')
         precision = summaries_of_Beta_Distribution(alpha_zero,beta_zero,'precision') 
         interpolated_values = {'Alpha_interpolated': alpha_zero, 'Beta_interpolated': beta_zero, \
                       'MAPprobability_interpolated': MAPprobability, 'Precision_interpolated': precision}
    else:
    # it is a null trial, and the dataframe is not empty, so assign interpolated values of previous trial
          interpolated_values = {'Alpha_interpolated': dataframe_row_of_prior_trial.at['Alpha_interpolated'], 'Beta_interpolated': dataframe_row_of_prior_trial.at['Beta_interpolated'], \
                        'MAPprobability_interpolated': dataframe_row_of_prior_trial.at['MAPprobability_interpolated'], 'Precision_interpolated': dataframe_row_of_prior_trial.at['Precision_interpolated']}  
    
    
    dict_of_trial_data.update(interpolated_values)  # add interpolated values to others from this trial
    return dict_of_trial_data # a dict of all results for this trial