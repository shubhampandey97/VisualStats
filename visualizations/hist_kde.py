import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

from visualizations.markers import draw_markers
from config.constants import COLORS


def render_histogram_kde(data: np.ndarray, config: dict):
    """
    Render histogram with KDE overlay.
    Returns a matplotlib Figure.
    """

    bins = config.get("bins", 20)
    color = config.get("color", "#4CAF50")
    edgecolor = config.get("edgecolor", "#000000")
    alpha = config.get("alpha", 0.6)
    linewidth = config.get("linewidth", 2.5)

    fig, ax = plt.subplots(figsize=(9, 5))

    # Histogram (density normalized)
    ax.hist(
        data,
        bins=bins,
        density=True,
        color=color,
        edgecolor=edgecolor,
        alpha=alpha,
    )
    
    draw_markers(ax, data, COLORS)


    # KDE curve
    kde = gaussian_kde(data)
    x_vals = np.linspace(min(data), max(data), 500)
    y_vals = kde(x_vals)

    ax.plot(x_vals, y_vals, color="black", linewidth=linewidth)

    ax.set_xlabel("Value")
    ax.set_ylabel("Density")
    ax.set_title("Histogram with KDE Overlay")

    return fig
