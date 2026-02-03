# logic/skewness.py

from config.constants import SKEW_THRESHOLD

def get_skew_state(skewness: float) -> str:
    """
    Classify skewness into left, right, or symmetric.
    """
    if abs(skewness) < SKEW_THRESHOLD:
        return "symmetric"
    return "right" if skewness > 0 else "left"


def get_skew_label(skewness: float) -> str:
    """
    Human-readable label for skewness.
    """
    state = get_skew_state(skewness)

    if state == "symmetric":
        return "Symmetric"
    if state == "right":
        return "Right-Skewed (Positive)"
    return "Left-Skewed (Negative)"
