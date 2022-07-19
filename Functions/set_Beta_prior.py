# set requested prior parameters for Beta distributions
# [A,B]= SET_BETA_PRIOR(P) sets the Beta distribution to the specified prior
# in P: 'Uniform'; 'Jeffreys'
def set_priors(prior_type):
    if prior_type == 'Uniform':
        alpha0 = 1
        beta0 = 1
    elif prior_type == 'Jeffreys':
        alpha0 = 0.5
        beta0 = 0.5
    else:
        print('Unknown prior distribution for the Beta distribution')
    return alpha0, beta0
