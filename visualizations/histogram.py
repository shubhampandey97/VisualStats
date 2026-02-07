import numpy as np
import matplotlib.pyplot as plt
import time

from logic.statistics import compute_mean, compute_median, compute_mode


def _draw_markers(ax, data, color_mean="#ef4444", color_median="#3b82f6", color_mode="#22c55e"):
    """Draw styled statistical markers."""

    mean = compute_mean(data)
    median = compute_median(data)
    mode = compute_mode(data)

    # Smooth premium lines
    ax.axvline(mean, linestyle="--", linewidth=2.5, color=color_mean, label="Mean")
    ax.axvline(median, linestyle="-.", linewidth=2.5, color=color_median, label="Median")
    ax.axvline(mode, linestyle=":", linewidth=3, color=color_mode, label="Mode")

    # Dot markers
    ymax = ax.get_ylim()[1]

    ax.scatter(mean, ymax * 0.92, s=90, color=color_mean, zorder=5)
    ax.scatter(median, ymax * 0.85, s=90, color=color_median, zorder=5)
    ax.scatter(mode, ymax * 0.78, s=90, color=color_mode, zorder=5)

    # Labels
    ax.text(mean, ymax * 0.95, "Mean", ha="center", color=color_mean, fontsize=10, weight="bold")
    ax.text(median, ymax * 0.88, "Median", ha="center", color=color_median, fontsize=10, weight="bold")
    ax.text(mode, ymax * 0.81, "Mode", ha="center", color=color_mode, fontsize=10, weight="bold")


def render_histogram(data, config=None):
    """
    Industry-grade histogram with soft animation effect.
    """

    if config is None:
        config = {}

    bins = config.get("bins", 20)
    color = config.get("color", "#4CAF50")
    edgecolor = config.get("edgecolor", "#000000")
    alpha = config.get("alpha", 0.85)

    fig, ax = plt.subplots(figsize=(9, 5))

    # Base histogram
    ax.hist(data, bins=bins, color=color, edgecolor=edgecolor, alpha=alpha)

    # Smooth transition illusion
    # (small pause helps visual continuity in Streamlit rerender)
    time.sleep(0.05)

    # Draw premium statistical markers
    _draw_markers(ax, data)

    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution with Statistical Markers")

    ax.legend(frameon=False)

    return fig
