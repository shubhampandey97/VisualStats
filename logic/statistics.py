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
