import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from core.dataset_manager import list_datasets, get_active_dataset
from logic.statistics import (
    compute_mean,
    compute_median,
    compute_mode,
    compute_skewness,
)
from logic.insights import generate_distribution_insight
from logic.skewness import get_skew_label


def _plot_hist(ax, data, title, color="#4CAF50"):
    ax.hist(data, bins=20, color=color, alpha=0.8, edgecolor="black")
    ax.set_title(title)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")


def render_comparison_dashboard():
    """Render side-by-side dataset comparison."""

    st.subheader("📊 Dataset Comparison")

    datasets = list_datasets()

    if len(datasets) < 2:
        st.info("Load at least two datasets to enable comparison.")
        return

    # -----------------------------
    # Dataset selectors
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        left_name = st.selectbox("Left dataset", datasets, key="cmp_left")

    with col2:
        right_name = st.selectbox("Right dataset", datasets, key="cmp_right")

    if left_name == right_name:
        st.warning("Select two different datasets to compare.")
        return

    # -----------------------------
    # Retrieve data
    # -----------------------------
    from core.dataset_manager import st as _st  # session access
    data_left = _st.session_state["datasets"][left_name]
    data_right = _st.session_state["datasets"][right_name]

    # -----------------------------
    # Side-by-side histograms
    # -----------------------------
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    _plot_hist(axes[0], data_left, left_name, "#42A5F5")
    _plot_hist(axes[1], data_right, right_name, "#FFA726")

    st.pyplot(fig)

    # -----------------------------
    # Statistics comparison
    # -----------------------------
    stats = {
        "Mean": [compute_mean(data_left), compute_mean(data_right)],
        "Median": [compute_median(data_left), compute_median(data_right)],
        "Mode": [compute_mode(data_left), compute_mode(data_right)],
        "Skewness": [compute_skewness(data_left), compute_skewness(data_right)],
    }

    st.markdown("### 📈 Statistical Comparison")

    st.dataframe(
        {
            "Metric": list(stats.keys()),
            left_name: [round(v[0], 3) for v in stats.values()],
            right_name: [round(v[1], 3) for v in stats.values()],
        },
        use_container_width=True,
    )

    # -----------------------------
    # Insight comparison
    # -----------------------------
    st.markdown("### 🧠 Insight Comparison")

    left_insight = generate_distribution_insight(
        get_skew_label(stats["Skewness"][0]),
        abs(stats["Skewness"][0]) < 0.5,
        *[stats[k][0] for k in ["Mean", "Median", "Mode"]],
    )

    right_insight = generate_distribution_insight(
        get_skew_label(stats["Skewness"][1]),
        abs(stats["Skewness"][1]) < 0.5,
        *[stats[k][1] for k in ["Mean", "Median", "Mode"]],
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"**{left_name}**\n\n{left_insight}")

    with col2:
        st.info(f"**{right_name}**\n\n{right_insight}")
