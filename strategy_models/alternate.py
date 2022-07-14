function trial_type = alternative(test_data)

#subject choses different spatial options on consecutive trials
number_trials = size(trial_data,1)

if number_trials > 1 and trial_data.Choice(end) ~= trial_daata.Choice(end-1)
    #chose different spatial option on consectutive trial, so is successive 
    trial_type = "success" 
else 
    #chose the same option on consecutive trials 
    trial_type = "failure"


