# app.py

import streamlit as st
from config.constants import COLORS
from data.generator import generate_skewed_data
from logic.skewness import get_skew_label, get_skew_state
from logic.statistics import compute_mean, compute_median, compute_mode
from visualizations.distribution import plot_distribution

st.set_page_config(page_title="Statistics Explorer", layout="centered")

st.title("📊 Statistics Explorer")

skewness = st.slider("Skewness", -10.0, 10.0, 0.0, 0.5)

data = generate_skewed_data(skewness)

mean = compute_mean(data)
median = compute_median(data)
mode = compute_mode(data)

state = get_skew_state(skewness)
fill_color = COLORS[state]

st.write(f"Distribution Type: **{get_skew_label(skewness)}**")

fig = plot_distribution(
    data=data,
    mean=mean,
    median=median,
    mode=mode,
    fill_color=fill_color,
    bins=15
)

st.pyplot(fig)
