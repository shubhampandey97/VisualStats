import numpy as np


def compute_markers(data):
    """Compute mean, median, and mode."""
    mean = np.mean(data)
    median = np.median(data)

    counts, bins = np.histogram(data, bins=50)
    mode = bins[np.argmax(counts)]

    return float(mean), float(median), float(mode)


def draw_markers(ax, data, colors):
    """
    Draw mean, median, and mode markers on the axis
    with proper spacing and labels (industry-grade UI).
    """
    mean, median, mode = compute_markers(data)

    # Safely get histogram height
    y_max = max((p.get_height() for p in ax.patches), default=1)

    # --------------------------------------------------
    # Add headroom so markers are NEVER clipped
    # --------------------------------------------------
    ax.set_ylim(0, y_max * 1.20)

    label_y = y_max * 1.05
    dot_top_y = y_max * 1.02

    # --------------------------------------------------
    # MEAN → arrow + label
    # --------------------------------------------------
    ax.annotate(
        "Mean",
        xy=(mean, dot_top_y),
        xytext=(mean, label_y),
        arrowprops=dict(arrowstyle="->", color=colors["mean"], linewidth=2),
        ha="center",
        color=colors["mean"],
        fontsize=10,
        fontweight="bold",
    )

    # --------------------------------------------------
    # MEDIAN → dashed line + dot + label
    # --------------------------------------------------
    ax.vlines(median, 0, y_max, colors=colors["median"], linestyles="--", linewidth=2)
    ax.scatter(median, dot_top_y, color=colors["median"], s=50, zorder=5)

    ax.text(
        median,
        label_y,
        "Median",
        ha="center",
        color=colors["median"],
        fontsize=10,
        fontweight="bold",
    )

    # --------------------------------------------------
    # MODE → dashed line + bottom dot + label
    # --------------------------------------------------
    bottom_dot_y = y_max * 0.02

    ax.vlines(mode, 0, y_max, colors=colors["mode"], linestyles="--", linewidth=2)
    ax.scatter(mode, bottom_dot_y, color=colors["mode"], s=50, zorder=5)

    ax.text(
        mode,
        bottom_dot_y + y_max * 0.08,
        "Mode",
        ha="center",
        color=colors["mode"],
        fontsize=10,
        fontweight="bold",
    )
