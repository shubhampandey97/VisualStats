def generate_distribution_insight(
    skew_label: str,
    is_normal: bool,
    mean: float,
    median: float,
    mode: float,
) -> str:
    """
    Generate human-readable statistical insight.
    """

    # Base description
    if skew_label == "Symmetric":
        description = "Distribution is symmetric with balanced tails."
        reliability = "Mean, median, and mode are all reliable."
    elif skew_label == "Right Skewed":
        description = "Distribution is right-skewed with a long positive tail."
        reliability = "Median is more reliable than mean."
    else:
        description = "Distribution is left-skewed with a long negative tail."
        reliability = "Median is more reliable than mean."

    # Normality interpretation
    if is_normal:
        normality_text = "Data follows a normal distribution."
    else:
        normality_text = "Data does NOT follow a normal distribution."

    return f"{description} {normality_text} {reliability}"
