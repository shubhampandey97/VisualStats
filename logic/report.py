from datetime import datetime


def generate_text_report(
    dataset_name: str,
    mean: float,
    median: float,
    mode: float,
    variance: float,
    std_dev: float,
    skewness: float,
    insight: str,
) -> str:
    """Create a human-readable analytics report."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
STATISTICS EXPLORER REPORT
Generated at: {timestamp}

Dataset: {dataset_name}

--- Descriptive Statistics ---
Mean: {mean:.4f}
Median: {median:.4f}
Mode: {mode:.4f}
Variance: {variance:.4f}
Standard Deviation: {std_dev:.4f}
Skewness: {skewness:.4f}

--- Automated Insight ---
{insight}

--------------------------------
End of Report
"""

    return report.strip()
