# logic/statistics.py

import numpy as np

def compute_mean(data):
    return float(np.mean(data))


def compute_median(data):
    return float(np.median(data))


def compute_mode(data, bins=50):
    """
    Approximate mode using histogram bin with max frequency.
    """
    counts, bin_edges = np.histogram(data, bins=bins)
    return float(bin_edges[counts.argmax()])


def compute_variance(data: np.ndarray) -> float:
    return float(np.var(data))


def compute_std(data: np.ndarray) -> float:
    return float(np.std(data))


def compute_quartiles(data: np.ndarray):
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    return q1, q2, q3


def compute_iqr(data: np.ndarray) -> float:
    q1, _, q3 = compute_quartiles(data)
    return q3 - q1

def compute_skewness(data: np.ndarray) -> float:
    """
    Compute skewness of the distribution.
    """
    mean = np.mean(data)
    std = np.std(data)

    if std == 0:
        return 0.0

    return float(np.mean(((data - mean) / std) ** 3))