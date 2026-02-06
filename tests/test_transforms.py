import numpy as np
from logic.transforms import apply_skewness


def test_no_skew_returns_same_data():
    data = np.array([1, 2, 3, 4, 5])
    result = apply_skewness(data, 0.0)

    assert np.allclose(result.mean(), data.mean(), atol=1e-6)


def test_skew_changes_distribution():
    data = np.random.normal(size=1000)

    result = apply_skewness(data, 5.0)

    assert not np.allclose(result, data)
