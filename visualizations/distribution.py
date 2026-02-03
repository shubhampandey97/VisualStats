# visualizations/distribution.py

import matplotlib.pyplot as plt

def darken_color(hex_color: str, factor: float = 0.6) -> str:
    hex_color = hex_color.lstrip("#")
    r, g, b = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    return f"#{int(r*factor):02x}{int(g*factor):02x}{int(b*factor):02x}"


def plot_distribution(data, mean, median, mode, fill_color, bins=15):
    """
    Plot histogram with mean, median, mode markers.
    """
    edge_color = darken_color(fill_color)

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.hist(
        data,
        bins=bins,
        color=fill_color,
        edgecolor=edge_color,
        linewidth=2.5,
        alpha=0.85
    )

    y_max = max(p.get_height() for p in ax.patches)

    # Mean → Arrow
    ax.annotate(
        "Mean",
        xy=(mean, y_max * 0.95),
        xytext=(mean, y_max * 1.15),
        arrowprops=dict(arrowstyle="->", linewidth=2),
        ha="center"
    )

    # Median → Top dot
    ax.vlines(median, 0, y_max, linestyles="--", linewidth=2)
    ax.scatter(median, y_max, s=50)

    # Mode → Bottom dot
    ax.vlines(mode, 0, y_max, linestyles="--", linewidth=2)
    ax.scatter(mode, 0, s=50)

    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    return fig
