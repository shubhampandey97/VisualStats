import streamlit as st
from logic.insights import generate_distribution_insight


def render_insight_panel(skew_label, is_normal, mean, median, mode):
    """Display AI-style statistical insight."""

    st.subheader("🧠 Automated Insight")

    insight = generate_distribution_insight(
        skew_label, is_normal, mean, median, mode
    )

    st.info(insight)
