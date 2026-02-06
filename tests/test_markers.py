import numpy as np
import matplotlib.pyplot as plt
from visualizations.markers import compute_markers


def test_compute_markers_runs():
    data = np.random.normal(size=100)
    mean, median, mode = compute_markers(data)

    assert isinstance(mean, float)
    assert isinstance(median, float)
    assert isinstance(mode, float)
