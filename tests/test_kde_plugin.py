import numpy as np
import matplotlib.figure as mpl_fig

from visualizations.kde import render_kde


def test_kde_returns_figure():
    data = np.random.normal(size=100)

    fig = render_kde(data, config={})

    assert isinstance(fig, mpl_fig.Figure)


def test_kde_runs_with_small_dataset():
    data = np.array([1, 2, 3, 4, 5])

    fig = render_kde(data, config={})

    assert fig is not None
