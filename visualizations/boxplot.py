import matplotlib.pyplot as plt
import numpy as np


def render_boxplot(data: np.ndarray, config: dict) -> None:
    """
    Render a box plot visualization.

    Parameters
    ----------
    data : np.ndarray
        Input data to visualize.
    config : dict
        Configuration options (color, linewidth, etc.).
    """
    color = config.get("color", "#1f7a3f")
    linewidth = config.get("linewidth", 2.0)

    fig, ax = plt.subplots(figsize=(9, 4))

    ax.boxplot(
        data,
        vert=False,
        patch_artist=True,
        boxprops=dict(facecolor=color, linewidth=linewidth),
        medianprops=dict(color="black", linewidth=linewidth),
        whiskerprops=dict(linewidth=linewidth),
        capprops=dict(linewidth=linewidth),
    )

    ax.set_xlabel("Value")
    ax.set_yticks([])

    return fig

