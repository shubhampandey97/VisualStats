import streamlit as st
from logic.normality import shapiro_test, dagostino_test, is_normal


def render_normality_diagnostics(data):
    """Display automatic statistical diagnostics."""

    st.subheader("🧠 Data Diagnostics")

    shapiro_stat, shapiro_p = shapiro_test(data)
    dago_stat, dago_p = dagostino_test(data)

    normal = is_normal(dago_p)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Shapiro p-value", f"{shapiro_p:.4f}")

    with col2:
        st.metric("D’Agostino p-value", f"{dago_p:.4f}")

    if normal:
        st.success("Distribution appears NORMAL (p > 0.05)")
    else:
        st.warning("Distribution is NOT normal (p ≤ 0.05)")
