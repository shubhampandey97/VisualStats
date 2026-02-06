import numpy as np
from logic.hypothesis import normality_test, one_sample_ttest


def test_normality_returns_values():
    data = np.random.normal(size=200)
    stat, p = normality_test(data)

    assert isinstance(stat, float)
    assert isinstance(p, float)


def test_one_sample_ttest_runs():
    data = np.random.normal(loc=5, size=200)
    stat, p = one_sample_ttest(data, popmean=5)

    assert isinstance(stat, float)
    assert isinstance(p, float)
