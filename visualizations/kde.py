import matplotlib
matplotlib.use("Agg")  # headless backend for tests/CI

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


def render_kde(data: np.ndarray, config: dict):
    """
    Render a KDE (Kernel Density Estimate) plot and return the figure.
    """
    color = config.get("color", "#4CAF50")
    linewidth = config.get("linewidth", 2.5)

    kde = gaussian_kde(data)

    x_vals = np.linspace(min(data), max(data), 500)
    y_vals = kde(x_vals)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x_vals, y_vals, color=color, linewidth=linewidth)

    ax.set_xlabel("Value")
    ax.set_ylabel("Density")
    ax.set_title("Kernel Density Estimate")

    return fig
