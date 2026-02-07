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

from data.csv_loader import load_numeric_column, CSVDataError
from logic.transforms import apply_skewness
from logic.hypothesis import normality_test, one_sample_ttest
from ui.insight_cards import render_skewness_cards
from ui.interpretation import render_interpretation_banner
from ui.diagnostics import render_normality_diagnostics
from ui.insight_panel import render_insight_panel

from ui.workspace import render_workspace_sidebar
from core.dataset_manager import get_active_dataset

from ui.comparison import render_comparison_dashboard









# -----------------------------
# App configuration
# -----------------------------
st.set_page_config(page_title="Statistics Explorer", layout="centered")

render_workspace_sidebar()


st.title("📊 Statistics Explorer")


# -----------------------------
# Initialize visualization registry
# -----------------------------
registry = VisualizationRegistry()
register_visualizations(registry)


# -----------------------------
# Data Source Selection
# -----------------------------
st.subheader("📂 Data Source")

data = get_active_dataset()

if data is None:
    st.info("Upload or generate a dataset from the sidebar to begin.")
    st.stop()



# -----------------------------
# Data Loading
# -----------------------------
if data_source == "Synthetic Distribution":

    # Synthetic generation skewness (ONLY for generation)
    gen_skewness = st.slider(
        "Generation Skewness",
        -10.0,
        10.0,
        0.0,
        0.5,
        key="generation_skewness_slider",
    )
    
    logger.debug("Generating synthetic skewed data")
    data = generate_skewed_data(gen_skewness)

    state = get_skew_state(gen_skewness)
    fill_color = COLORS[state]

    st.write(f"Distribution Type: **{get_skew_label(gen_skewness)}**")

else:
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            import pandas as pd

            df = pd.read_csv(uploaded_file)
            numeric_columns = df.select_dtypes(include="number").columns.tolist()

            if not numeric_columns:
                logger.warning("CSV uploaded but no numeric columns found")
                st.error("No numeric columns found in CSV.")
                st.stop()

            column = st.selectbox("Select numeric column", numeric_columns)

            # reload file for clean read
            uploaded_file.seek(0)
            data = load_numeric_column(uploaded_file, column)

            fill_color = "#4CAF50"  # neutral color for real data

        except CSVDataError as e:
            logger.error(f"CSV parsing failed: {e}")
            st.error(str(e))
            st.stop()

    else:
        st.info("Upload a CSV file to continue.")
        st.stop()


# =============================
# DISTRIBUTION TRANSFORMATION
# =============================
st.subheader("⚙️ Distribution Transformation")

skewness = st.slider(
    "Apply skewness transformation",
    -10.0,
    10.0,
    0.0,
    0.5,
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

render_insight_panel(
    skew_label=get_skew_label(skewness) if data_source == "Synthetic Distribution" else "Unknown",
    is_normal=(skew_value == 0 or abs(skew_value) < 0.5),
    mean=mean,
    median=median,
    mode=mode,
)

# =============================
# Hypothesis Testing
# =============================
st.subheader("🧪 Hypothesis Testing")

# --- Normality Test ---
stat, p = normality_test(data)

st.write("**Normality Test (D’Agostino-Pearson)**")
st.write(f"Statistic: {stat:.3f} | p-value: {p:.5f}")

if p > 0.05:
    st.success("Data looks normally distributed (fail to reject H₀)")
else:
    st.warning("Data is NOT normally distributed (reject H₀)")


# --- One-sample t-test ---
st.write("### One-Sample t-Test")

popmean = st.number_input("Test mean value", value=float(mean))

t_stat, t_p = one_sample_ttest(data, popmean)

st.write(f"t-statistic: {t_stat:.3f} | p-value: {t_p:.5f}")

if t_p > 0.05:
    st.success("Mean is NOT significantly different from test value")
else:
    st.error("Mean is significantly different from test value")



st.subheader("📘 Skewness Interpretation")
render_skewness_cards()

# -----------------------------
# Visualization Selector
# -----------------------------
st.subheader("📈 Select Visualization")

visualization_name = st.selectbox(
    "Visualization Type",
    registry.list_available(),
)


# -----------------------------
# Visualization-specific Controls
# -----------------------------
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


# -----------------------------
# Render Visualization
# -----------------------------
render_fn = registry.get(visualization_name)
fig = render_fn(data, config=config)
st.pyplot(fig)

# -----------------------------
# Dataset Comparison Dashboard
# -----------------------------
from ui.comparison import render_comparison_dashboard


# -----------------------------
# Interpretation Section
# -----------------------------
st.divider()
st.subheader("📌 Interpretation")
render_interpretation_banner(skew_value)

