import streamlit as st

def visualization_selector():
    return st.selectbox(
        "Select what you want to visualize",
        [
            "Mean · Median · Mode",
            "Skewness",
            "Variance & Std Deviation",
            "Outliers (IQR)",
        ]
    )
