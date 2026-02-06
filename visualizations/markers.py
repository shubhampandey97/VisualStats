import numpy as np


def compute_markers(data):
    mean = np.mean(data)
    median = np.median(data)

    counts, bins = np.histogram(data, bins=50)
    mode = bins[np.argmax(counts)]

    return mean, median, mode


def draw_markers(ax, data, colors):
    mean, median, mode = compute_markers(data)

    y_max = max(p.get_height() for p in ax.patches) if ax.patches else 1

    # Mean → arrow
    ax.annotate(
        "Mean",
        xy=(mean, y_max * 0.9),
        xytext=(mean, y_max * 1.1),
        arrowprops=dict(arrowstyle="->", color=colors["mean"], linewidth=2),
        ha="center",
        color=colors["mean"],
    )

    # Median → line + top dot
    ax.vlines(median, 0, y_max, colors=colors["median"], linestyles="--", linewidth=2)
    ax.scatter(median, y_max, color=colors["median"], s=40, zorder=5)

    # Mode → line + bottom dot
    ax.vlines(mode, 0, y_max, colors=colors["mode"], linestyles="--", linewidth=2)
    ax.scatter(mode, 0, color=colors["mode"], s=40, zorder=5)
