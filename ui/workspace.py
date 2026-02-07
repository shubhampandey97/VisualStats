"""
Workspace Sidebar UI

Provides:
- dataset upload
- dataset switching
- active dataset display
"""

import streamlit as st
import pandas as pd

from core.dataset_manager import (
    add_dataset,
    list_datasets,
    set_active_dataset,
    get_active_name,
)
from data.csv_loader import load_numeric_column, CSVDataError


def render_workspace_sidebar():
    """Render dataset workspace in Streamlit sidebar."""

    st.sidebar.header("📂 Workspace")

    # -------------------------
    # Upload new dataset
    # -------------------------
    uploaded_file = st.sidebar.file_uploader(
        "Upload CSV dataset",
        type=["csv"],
    )

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            numeric_cols = df.select_dtypes(include="number").columns.tolist()

            if not numeric_cols:
                st.sidebar.error("No numeric columns found.")
            else:
                column = st.sidebar.selectbox(
                    "Select numeric column",
                    numeric_cols,
                    key="workspace_column_select",
                )

                uploaded_file.seek(0)
                data = load_numeric_column(uploaded_file, column)

                dataset_name = f"{uploaded_file.name}:{column}"
                add_dataset(dataset_name, data)

                st.sidebar.success(f"Added dataset: {dataset_name}")

        except CSVDataError as e:
            st.sidebar.error(str(e))

    # -------------------------
    # Existing datasets list
    # -------------------------
    datasets = list_datasets()

    if datasets:
        active = get_active_name()

        selected = st.sidebar.selectbox(
            "Select active dataset",
            datasets,
            index=datasets.index(active) if active in datasets else 0,
            key="workspace_dataset_select",
        )

        if selected != active:
            set_active_dataset(selected)

        st.sidebar.caption(f"Active: {selected}")

    else:
        st.sidebar.info("No datasets loaded.")
