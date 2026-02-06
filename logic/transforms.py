import numpy as np
from scipy.stats import skewnorm


def apply_skewness(data: np.ndarray, skewness: float) -> np.ndarray:
    """
    Apply skewness transformation to data while preserving scale.
    """
    if abs(skewness) < 1e-6:
        return data

    mean = np.mean(data)
    std = np.std(data)

    if std == 0:
        return data

    normalized = (data - mean) / std
    skewed = skewnorm.rvs(a=skewness, size=len(data))

    return skewed * std + mean
