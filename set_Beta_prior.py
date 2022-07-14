# set requested prior parameters for Beta distributions
# [A,B]= SET_BETA_PRIOR(P) sets the Beta distribution to the specified prior
# in P: 'Uniform'; 'Jeffreys'


def set_priors(prior_type):
    if prior_type == "Uniform":
        return 1
    if prior_type == "Jeffreys":
        return 0.5
    else:
        print('Unknown prior distribution for the Beta distribution')