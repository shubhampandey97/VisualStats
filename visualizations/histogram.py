import matplotlib.pyplot as plt
import numpy as np


def render_histogram(data: np.ndarray, config: dict) -> None:
    """
    Render a histogram visualization.

    Parameters
    ----------
    data : np.ndarray
        Input data to visualize.
    config : dict
        Configuration options (bins, colors, etc.).
    """
    bins = config.get("bins", 15)
    color = config.get("color", "#1f7a3f")
    edgecolor = config.get("edgecolor", "#0e3d1f")
    alpha = config.get("alpha", 0.85)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(
        data,
        bins=bins,
        color=color,
        edgecolor=edgecolor,
        linewidth=2.5,
        alpha=alpha,
    )

    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    return fig
