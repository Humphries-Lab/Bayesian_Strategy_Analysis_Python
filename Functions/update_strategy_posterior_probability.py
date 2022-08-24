import numpy as np

def update_strategy_posterior_probability(trial_type, decay_rate, success_total, failure_total, alpha0, beta0):
    if trial_type == "success":
        success_total = (decay_rate * success_total + 1)
        failure_total = (decay_rate * failure_total)
        alpha = (alpha0 + success_total)
        beta = (beta0 + failure_total)
    elif trial_type == "failure":
        success_total = (decay_rate * success_total)
        failure_total = (decay_rate * failure_total + 1)
        alpha = (alpha0 + success_total)
        beta = (beta0 + failure_total)
    else:
        alpha = np.nan
        beta = np.nan

    return success_total, failure_total, alpha, beta

