# checks if the subject chose the left option on this trial
# TYPE = GO_RIGHT(TRIAL_DATA) takes the Table of testdata TRIAL_DATA up to the current trial, and
# returns the TYPE ("success", 'failure')
import pandas as pd


# Checks only the current trial


def go_right(TestData):
    if TestData.Choice == "right":
        trial_type = "success"
    else:
        trial_type = "failure"
    return trial_type
