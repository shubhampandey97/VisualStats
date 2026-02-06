import streamlit as st


def _get_interpretation(skew: float):
    if skew > 0.5:
        return (
            "Mode < Median < Mean",
            "In right-skewed data, the tail pulls the mean to the right.",
            "#34d399",
        )
    elif skew < -0.5:
        return (
            "Mean < Median < Mode",
            "In left-skewed data, the tail pulls the mean to the left.",
            "#60a5fa",
        )
    else:
        return (
            "Mean ≈ Median ≈ Mode",
            "Symmetric distribution with balanced tails.",
            "#fbbf24",
        )    
        
        

# ui/interpretation.py

import streamlit as st


def render_interpretation_banner(skew_value: float) -> None:
    """Render interpretation banner below visualization."""

    # ---------- Determine order ----------
    if skew_value > 0.1:
        order = "Mode < Median < Mean"
        explanation = "In right-skewed data, the tail pulls the mean to the right."
        highlight = "Mean"

    elif skew_value < -0.1:
        order = "Mean < Median < Mode"
        explanation = "In left-skewed data, the tail pulls the mean to the left."
        highlight = "Mode"

    else:
        order = "Mean ≈ Median ≈ Mode"
        explanation = "Symmetric distribution with balanced tails."
        highlight = None

    # ---------- Color highlight ----------
    if highlight:
        order = order.replace(
            highlight,
            f"<span style='color:#22c55e; font-weight:700'>{highlight}</span>"
        )

    # ---------- Clean HTML (NO indentation issues) ----------
    html = f"""
    <div style="
        background: linear-gradient(135deg,#0f172a,#1e293b);
        border-radius: 16px;
        padding: 28px;
        margin-top: 24px;
        text-align: center;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);">
        <div style="font-size:28px; font-weight:700; margin-bottom:10px;">
            {order}
        </div>

        <p style="color:#9ca3af; margin:0; font-size:15px;">
            {explanation}
        </p>
    </div>
    """

    # ---------- Render ----------
    st.markdown(html, unsafe_allow_html=True)
