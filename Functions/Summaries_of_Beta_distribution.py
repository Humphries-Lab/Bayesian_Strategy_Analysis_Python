import numpy as np
from scipy.stats import beta


def summaries_of_Beta_Distribution(Alpha, Beta, stat_type, *args):
    if np.isnan(Alpha) or np.isnan(Beta):
        statistic = np.nan
    else:
        if stat_type == 'MAP':
            x = np.arange(0, 1, 0.001)
            y = beta.pdf(x, Alpha, Beta)
            statistic = x[np.argmax(y)]
        elif stat_type == 'Mean':
            statistic = Alpha / (Alpha + Beta)
        elif stat_type == 'Var':
            statistic = ((Alpha * Beta) / (((Alpha + Beta) ** 2) * (Alpha + Beta + 1)))
        elif stat_type == 'precision':
            statistic = 1 / ((Alpha * Beta) / (((Alpha + Beta) ** 2) * (Alpha + Beta + 1)))
        elif stat_type == 'Percentile':
            Prct = args[0]
            Delta = 1 - Prct
            P = [Delta / 2, Prct + Delta / 2]
            statistic = beta.ppf(P, Alpha, Beta)
        else:
            print("ERROR")
    return statistic
