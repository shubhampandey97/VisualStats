import numpy as np
import matplotlib.figure as mpl_fig

from visualizations.hist_kde import render_histogram_kde


def test_hist_kde_returns_figure():
    data = np.random.normal(size=100)
    fig = render_histogram_kde(data, config={})
    assert isinstance(fig, mpl_fig.Figure)
