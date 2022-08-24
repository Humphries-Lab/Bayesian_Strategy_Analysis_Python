#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 19:39:45 2022

Unit tests for the strategy models

@author: Mark Humphries
"""

import pandas as pd
import strategymodels

# make test dataframe
test_data_for_rules = {'Choice' : ['left','left','left','left','right','right','right','right'],
        'CuePosition': ['left','right','left','right','left','right','left','right'],
        'Reward': ['yes','yes','no','no','yes','yes','no','no']}
TestData = pd.DataFrame(test_data_for_rules)

# target results for rules

go_left_target = ['success','success','success','success','failure','failure','failure','failure']
go_right_target = ['failure','failure','failure','failure','success','success','success','success']
go_cued_target = ['success','failure','success','failure','failure','success','failure','success']
go_uncued_target = ['failure','success','failure','success','success','failure','success','failure']

#%% run rule strategy models
trial_type_left = []; trial_type_right = []; trial_type_cued = []; trial_type_uncued = [];
for trial in range(len(TestData)):
    rows_of_data = TestData.iloc[0:trial+1]     # select all rows of data up to the curren trial; is trial+1 as dataframe includes column row as row 0????
    trial_type_left.append(strategymodels.go_left(rows_of_data))         # test whether go-left was used       
    trial_type_right.append(strategymodels.go_right(rows_of_data))
    trial_type_cued.append(strategymodels.go_cued(rows_of_data))  
    trial_type_uncued.append(strategymodels.go_uncued(rows_of_data))  
    
#%% did they pass the tests?    
print('Go left passed?')    
print(trial_type_left == go_left_target)

print('Go right passed?')    
print(trial_type_right == go_right_target)

print('Go cued passed?')    
print(trial_type_cued == go_cued_target)
    
print('Go uncued passed?')    
print(trial_type_uncued == go_uncued_target)

#%%
#  test Explore strategy models
# 

# extend test data to include all win-stay and lose-shift test cases
test_data_for_rules['Choice'].append('right','left','right','right','left')
test_data_for_rules['CuePosition'].append('right','right','left','left','left')
test_data_for_rules['Reward'].append('yes','yes','yes','no','no')

TestData = pd.DataFrame(test_data_for_rules)  # overwrite dataframe

# define target results for exploration rules (null, success, failure)


# run explore strategy models
trial_type_alternate = []; trial_type_sticky = []; trial_type_win_stay_spatial= []; 
trial_type_win_stay_cue = []; trial_type_lose_shift_spatial= []; trial_type_lose_shift_cue = []; 

for trial in range(len(TestData)):
    rows_of_data = TestData.iloc[0:trial+1]     # select all rows of data up to the curren trial; is trial+1 as dataframe includes column row as row 0????  
    