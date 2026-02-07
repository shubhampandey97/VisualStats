import streamlit as st

from logic.report import generate_text_report
from core.dataset_manager import get_active_name


def render_report_download(
    mean,
    median,
    mode,
    variance,
    std_dev,
    skewness,
    insight,
):
    """Render download button for analytics report."""

    dataset_name = get_active_name() or "Unknown Dataset"

    report_text = generate_text_report(
        dataset_name=dataset_name,
        mean=mean,
        median=median,
        mode=mode,
        variance=variance,
        std_dev=std_dev,
        skewness=skewness,
        insight=insight,
    )

    st.subheader("📄 Export Report")

    st.download_button(
        label="Download TXT Report",
        data=report_text,
        file_name=f"{dataset_name}_report.txt",
        mime="text/plain",
    )
