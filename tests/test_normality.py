import numpy as np
from logic.normality import shapiro_test, dagostino_test, is_normal


def test_normal_data_detected():
    data = np.random.normal(size=500)

    _, p = shapiro_test(data)
    assert isinstance(p, float)


def test_non_normal_data_detected():
    data = np.random.exponential(size=500)

    _, p = dagostino_test(data)
    assert isinstance(p, float)


def test_is_normal_logic():
    assert is_normal(0.5) is True
    assert is_normal(0.001) is False
