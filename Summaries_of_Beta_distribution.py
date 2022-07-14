import numpy as np
from scipy.stats import beta

global statistic
def summaries_of_Beta_Distribution(Alpha, Beta, type, *args):
    if np.isnan(Alpha) or np.isnan(Beta):
        statistic = nan
    else:
        match type:
            case 'MAP':
                x = np.arange(0, 1, 0.001)
                y = beta.pdf(x, Alpha, Beta)
                statistic = x[np.argmax(y)]
            case 'Mean':
                statistic = Alpha / (Alpha + Beta)
            case 'Var':
                statistic = ((Alpha * Beta) / (((Alpha + Beta)**2) * (Alpha + Beta + 1)))
            case 'precision':
                statistic = 1/((Alpha * Beta) / (((Alpha + Beta) ** 2) * (Alpha + Beta + 1)))
            case 'Percentile':
                Prct = args
                Delta = 1 - Prct
                P = [Delta/2, Prct + Delta/2]
                statistic = beta.ppf(P, Alpha, Beta)
    return statistic
