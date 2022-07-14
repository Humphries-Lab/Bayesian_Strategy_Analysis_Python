# checks if the subject chose the left option on this trial
# TYPE = GO_LEFT(TRIAL_DATA) takes the Table of testdata TRIAL_DATA up to the current trial, and
# returns the TYPE ("success", 'failure')

# Checks only the current trial
global trial_type


def go_left(rows):
    if rows == "left":
        trial_type = "success"
    elif rows == "right":
        trial_type = "failure"
    return trial_type
