# checks if the subject chose the right-hand option on this trial
# TYPE = GO_RIGHT(TRIAL_DATA) takes the Table of testdata TRIAL_DATA up to the current trial, and
# returns the TYPE ("success", 'failure')

# Checks only the current trial

def go_right(rows):
    nTrials = len(rows);
     # "at" selects the value at the row/column location in the dataframe
    if rows.at[nTrials-1,'Choice'] == "right":      # check the current trial's choice
        trial_type = "success"
    elif rows.at[nTrials-1,'Choice'] == "left":
        trial_type = "failure"
    return trial_type
