# tests/test_statistics.py

import numpy as np
from logic.statistics import compute_mean, compute_median

def test_mean():
    data = np.array([1, 2, 3])
    assert compute_mean(data) == 2.0

def test_median():
    data = np.array([1, 3, 2])
    assert compute_median(data) == 2.0
