# app.py

from core.logging import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)
logger.info("App started")

import streamlit as st

from core.registry import VisualizationRegistry
from visualizations import register_visualizations

from config.constants import COLORS
from data.generator import generate_skewed_data
from logic.skewness import get_skew_label, get_skew_state
from logic.statistics import (
    compute_mean,
    compute_median,
    compute_mode,
    compute_skewness,
    compute_variance,
    compute_std,
    compute_quartiles,
    compute_iqr,
)

from logic.transforms import apply_skewness
from logic.hypothesis import normality_test, one_sample_ttest

from ui.insight_cards import render_skewness_cards
from ui.interpretation import render_interpretation_banner
from ui.diagnostics import render_normality_diagnostics
from ui.insight_panel import render_insight_panel
from ui.workspace import render_workspace_sidebar
from ui.comparison import render_comparison_dashboard
from ui.report_panel import render_report_download

from core.dataset_manager import get_active_dataset


# -----------------------------
# App configuration
# -----------------------------
st.set_page_config(page_title="Statistics Explorer", layout="centered")

render_workspace_sidebar()
st.title("📊 Statistics Explorer")


# -----------------------------
# Visualization registry
# -----------------------------
registry = VisualizationRegistry()
register_visualizations(registry)


# -----------------------------
# DATA PIPELINE (industry clean)
# -----------------------------
data = get_active_dataset()

# ---- Synthetic fallback when no dataset loaded ----
if data is None:
    st.info("No dataset loaded. Showing synthetic demo data.")

    gen_skewness = st.slider(
        "Synthetic Data Skewness",
        -10.0, 10.0, 0.0, 0.5,
        key="synthetic_generation_skewness",
    )

    logger.debug("Generating synthetic fallback data")
    data = generate_skewed_data(gen_skewness)

    state = get_skew_state(gen_skewness)
    fill_color = COLORS[state]
    skew_label = get_skew_label(gen_skewness)

else:
    fill_color = "#4CAF50"
    skew_label = "Dataset"


# =============================
# DISTRIBUTION TRANSFORMATION
# =============================
st.subheader("⚙️ Distribution Transformation")

skewness = st.slider(
    "Apply skewness transformation",
    -10.0, 10.0, 0.0, 0.5,
    key="transform_skewness_slider",
)

data = apply_skewness(data, skewness)


# -----------------------------
# Statistics Computation
# -----------------------------
mean = compute_mean(data)
median = compute_median(data)
mode = compute_mode(data)

variance = compute_variance(data)
std_dev = compute_std(data)
q1, q2, q3 = compute_quartiles(data)
iqr = compute_iqr(data)

skew_value = compute_skewness(data)


# -----------------------------
# Statistics Panel UI
# -----------------------------
st.subheader("📊 Statistical Summary")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Mean", f"{mean:.2f}")
    st.metric("Median", f"{median:.2f}")
    st.metric("Mode", f"{mode:.2f}")

with c2:
    st.metric("Variance", f"{variance:.2f}")
    st.metric("Std Dev", f"{std_dev:.2f}")
    st.metric("Skewness", f"{skew_value:.2f}")

with c3:
    st.metric("Q1", f"{q1:.2f}")
    st.metric("Q3", f"{q3:.2f}")
    st.metric("IQR", f"{iqr:.2f}")

render_normality_diagnostics(data)


# -----------------------------
# Hypothesis Testing
# -----------------------------
st.subheader("🧪 Hypothesis Testing")

stat, p = normality_test(data)
st.write(f"Normality Test → Statistic: {stat:.3f} | p-value: {p:.5f}")

popmean = st.number_input("Test mean value", value=float(mean))
t_stat, t_p = one_sample_ttest(data, popmean)
st.write(f"t-statistic: {t_stat:.3f} | p-value: {t_p:.5f}")


# -----------------------------
# Insight
# -----------------------------
is_normal = abs(skew_value) < 0.5

render_insight_panel(
    skew_label=skew_label,
    is_normal=is_normal,
    mean=mean,
    median=median,
    mode=mode,
)

insight_text = f"{skew_label} distribution with skewness {skew_value:.2f}"

# -----------------------------
# Skewness Concept Cards
# -----------------------------
st.subheader("📘 Skewness Interpretation")
render_skewness_cards()

# -----------------------------
# Visualization
# -----------------------------
st.subheader("📈 Select Visualization")

visualization_name = st.selectbox(
    "Visualization Type",
    registry.list_available(),
)

config = {}

if visualization_name == "Histogram":
    from config.settings import CONFIG

    bins = st.slider(
        "Number of bins",
        CONFIG.min_bins,
        CONFIG.max_bins,
        CONFIG.default_bins,
        key="bins_slider",
    )
    config = {
        "bins": bins,
        "color": fill_color,
        "edgecolor": "#000000",
        "alpha": 0.85,
    }

render_fn = registry.get(visualization_name)
fig = render_fn(data, config=config)
st.pyplot(fig)

# -----------------------------
# Interpretation
# -----------------------------
st.divider()
st.subheader("📌 Interpretation")
render_interpretation_banner(skew_value)

# -----------------------------
# Dataset Comparison
# -----------------------------
render_comparison_dashboard()

# -----------------------------
# Export Report
# -----------------------------
render_report_download(
    mean=mean,
    median=median,
    mode=mode,
    variance=variance,
    std_dev=std_dev,
    skewness=skew_value,
    insight=insight_text,
)

