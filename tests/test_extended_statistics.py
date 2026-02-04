import numpy as np
from logic.statistics import (
    compute_variance,
    compute_std,
    compute_quartiles,
    compute_iqr,
)


def test_variance():
    data = np.array([1, 2, 3, 4, 5])
    assert compute_variance(data) == 2.0


def test_std():
    data = np.array([1, 2, 3, 4, 5])
    assert round(compute_std(data), 5) == round(np.std(data), 5)


def test_quartiles():
    data = np.array([1, 2, 3, 4, 5])
    q1, q2, q3 = compute_quartiles(data)

    assert q1 == 2
    assert q2 == 3
    assert q3 == 4


def test_iqr():
    data = np.array([1, 2, 3, 4, 5])
    assert compute_iqr(data) == 2
