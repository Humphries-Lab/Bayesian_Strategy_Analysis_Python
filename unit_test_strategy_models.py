#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 19:39:45 2022

Unit tests for the strategy models

@author: Mark Humphries
"""

import pandas as pd
import strategymodels

# load test dataframe
# set na_filter = False to load "null" as strings
UnitTestData = pd.read_csv('UnitTestData.csv',na_filter=False)

TestResults = pd.DataFrame();

#%% run rule strategy models
trial_type_left = []; trial_type_right = []; trial_type_cued = []; trial_type_uncued = [];
for trial in range(len(UnitTestData)):
    rows_of_data = UnitTestData.iloc[0:trial+1]     # select all rows of data up to the curren trial; is trial+1 as dataframe includes column row as row 0????
    trial_type_left.append(strategymodels.go_left(rows_of_data))         # test whether go-left was used       
    trial_type_right.append(strategymodels.go_right(rows_of_data))
    trial_type_cued.append(strategymodels.go_cued(rows_of_data))  
    trial_type_uncued.append(strategymodels.go_uncued(rows_of_data))  
    
#%% did they pass the tests?    
TestResults['go_left_result'] = UnitTestData['go_left'].eq(trial_type_left)
TestResults['go_right_result'] = UnitTestData['go_right'].eq(trial_type_right)
TestResults['go_cued_result'] = UnitTestData['go_cued'].eq(trial_type_cued)
TestResults['go_uncued_result'] = UnitTestData['go_uncued'].eq(trial_type_uncued)

# print to screen
print('Go left passed? ' + str(TestResults['go_left_result'].all()))

print('Go right passed? ' + str(TestResults['go_right_result'].all()))    

print('Go cued passed? ' + str((TestResults['go_cued_result'].all())))

print('Go uncued passed? ' + str(TestResults['go_uncued_result'].all()))    

#%%
#  test Explore strategy models
# 

trial_type_alternate = []; trial_type_sticky = []; trial_type_win_stay_spatial= []; 
trial_type_win_stay_cued = []; trial_type_lose_shift_spatial= []; trial_type_lose_shift_cued= []; 

for trial in range(len(UnitTestData)):
    rows_of_data = UnitTestData.iloc[0:trial+1]     # select all rows of data up to the curren trial; is trial+1 as dataframe includes column row as row 0????  
    trial_type_alternate.append(strategymodels.alternate(rows_of_data)) 
    trial_type_sticky.append(strategymodels.sticky(rows_of_data)) 
    trial_type_win_stay_spatial.append(strategymodels.win_stay_spatial(rows_of_data)) 
    trial_type_win_stay_cued.append(strategymodels.win_stay_cued(rows_of_data)) 
    trial_type_lose_shift_spatial.append(strategymodels.lose_shift_spatial(rows_of_data)) 
    trial_type_lose_shift_cued.append(strategymodels.lose_shift_cued(rows_of_data)) 
    
# did they pass test?    
TestResults['alternate_result'] = UnitTestData['alternate'].eq(trial_type_alternate)
TestResults['sticky_result'] = UnitTestData['sticky'].eq(trial_type_sticky)
TestResults['win_stay_spatial_result'] = UnitTestData['win_stay_spatial'].eq(trial_type_win_stay_spatial)
TestResults['win_stay_cued_result'] = UnitTestData['win_stay_cued'].eq(trial_type_win_stay_cued)
TestResults['lose_shift_spatial_result'] = UnitTestData['lose_shift_spatial'].eq(trial_type_lose_shift_spatial)
TestResults['lose_shift_cued_result'] = UnitTestData['lose_shift_cued'].eq(trial_type_lose_shift_cued)

# print to screen
print('Alternate passed? ' + str(TestResults['alternate_result'].all()))

print('Sticky passed? ' + str(TestResults['sticky_result'].all()))    

print('Win-stay-spatial passed? ' + str(TestResults['win_stay_spatial_result'].all()))    
    
print('Win-stay-cued passed? ' + str(TestResults['win_stay_cued_result'].all()))    

print('Lose-shift-spatial passed? ' + str(TestResults['lose_shift_spatial_result'].all()))    
    
print('Lose-shift-cued passed? ' + str(TestResults['lose_shift_cued_result'].all()))    