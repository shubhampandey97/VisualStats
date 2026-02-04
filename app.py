# app.py



import streamlit as st

from core.registry import VisualizationRegistry
from visualizations import register_visualizations

from config.constants import COLORS
from data.generator import generate_skewed_data
from logic.skewness import get_skew_label, get_skew_state
from logic.statistics import compute_mean, compute_median, compute_mode
# from visualizations.distribution import plot_distribution



# -----------------------------
# App configuration
# -----------------------------
st.set_page_config(page_title="Statistics Explorer", layout="centered")

st.title("📊 Statistics Explorer")

# -----------------------------
# Initialize visualization registry
# -----------------------------
registry = VisualizationRegistry()
register_visualizations(registry)

# -----------------------------
# Controls
# -----------------------------
skewness = st.slider("Skewness", -10.0, 10.0, 0.0, 0.5)

# -----------------------------
# Data generation
# -----------------------------
data = generate_skewed_data(skewness)

# -----------------------------
# Statistics
# -----------------------------
mean = compute_mean(data)
median = compute_median(data)
mode = compute_mode(data)

state = get_skew_state(skewness)
fill_color = COLORS[state]

st.write(f"Distribution Type: **{get_skew_label(skewness)}**")

# -----------------------------
# Visualization selector
# -----------------------------
st.subheader("Select Visualization")

visualization_name = st.selectbox(
    "Visualization Type",
    registry.list_available(),
)

# -----------------------------
# Visualization-specific UI controls
# -----------------------------
config = {}

if visualization_name == "Histogram":
    bins = st.slider("Number of bins", 5, 50, 15)
    config = {
        "bins": bins,
        "color": fill_color,
        "edgecolor": "#000000",
        "alpha": 0.85,
    }

# -----------------------------
# Render visualization via registry
# -----------------------------
render_fn = registry.get(visualization_name)
# render_fn(data, config=config)
fig = render_fn(data, config=config)
st.pyplot(fig)


