import numpy as np
from scipy import stats


def normality_test(data: np.ndarray):
    """
    Perform D’Agostino and Pearson’s normality test.
    Returns statistic and p-value.
    """
    stat, p = stats.normaltest(data)
    return float(stat), float(p)


def one_sample_ttest(data: np.ndarray, popmean: float):
    """
    Perform one-sample t-test against a population mean.
    Returns statistic and p-value.
    """
    stat, p = stats.ttest_1samp(data, popmean)
    return float(stat), float(p)
