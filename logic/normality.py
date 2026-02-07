import numpy as np
from scipy import stats


def shapiro_test(data: np.ndarray):
    """Return Shapiro-Wilk statistic and p-value."""
    stat, p = stats.shapiro(data)
    return float(stat), float(p)


def dagostino_test(data: np.ndarray):
    """Return D’Agostino normality test statistic and p-value."""
    stat, p = stats.normaltest(data)
    return float(stat), float(p)


def is_normal(p_value: float, alpha: float = 0.05) -> bool:
    """Determine if distribution is normal."""
    return p_value > alpha
