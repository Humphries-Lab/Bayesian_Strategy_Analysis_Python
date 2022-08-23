# checks if the subject chose the left option on this trial
# TYPE = GO_LEFT(TRIAL_DATA) takes the Table of testdata TRIAL_DATA up to the current trial, and
# returns the TYPE ("success", 'failure')

# Checks only the current trial

def go_left(rows):

    nTrials = len(rows);
     # "at" selects the value at the row/column location in the dataframe
    if rows.at[nTrials-1,'Choice'] == "left":      # check the current trial's choice
        trial_type = "success"
    elif rows.at[nTrials-1,'Choice'] == "right":
        trial_type = "failure"
    return trial_type
