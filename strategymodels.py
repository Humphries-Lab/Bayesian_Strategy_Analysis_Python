# -*- coding: utf-8 -*-
"""
Strategy models module

A set of functions that define each strategy model
Each function takes a Pandas dataframe, where each row is the data for one trial, 
up to the current trial

The column names in the dataframe are used to find the values 

Created on Tue Aug 23 12:42:13 2022

@author: lpzmdh
"""

########## rule strategies
def go_left(rows):
    # checks if the subject chose the left option on this trial
    nTrials = len(rows);
     # "at" selects the value at the row/column location in the dataframe
    if rows.at[nTrials-1,'Choice'] == "left":      # check the current trial's choice
        trial_type = "success"
    elif rows.at[nTrials-1,'Choice'] == "right":
        trial_type = "failure"
    return trial_type


def go_right(rows):
    # checks if the subject chose the right-hand option on this trial
    nTrials = len(rows);
     # "at" selects the value at the row/column location in the dataframe
    if rows.at[nTrials-1,'Choice'] == "right":      # check the current trial's choice
        trial_type = "success"
    elif rows.at[nTrials-1,'Choice'] == "left":
        trial_type = "failure"
    return trial_type

############ exploration strategies

def alternate(rows):
    # checks if the subject made a different choice on this trial
    nTrials = len(rows);
     # "at" selects the value at the row/column location in the dataframe
    if nTrials > 1 & rows.at[nTrials-1,'Choice'] != rows.at[nTrials-2,'Choice']:      # check the current trial's choice
        trial_type = "success"
    else:
        trial_type = "failure"
    return trial_type
