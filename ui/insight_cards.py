import streamlit as st


def _card(title, subtitle, description, active=False):
    """Render one skewness card with dynamic size."""

    scale = 1.15 if active else 1.0
    opacity = 1.0 if active else 0.5
    border = "2px solid #4CAF50" if active else "1px solid #444"

    st.markdown(
        f"""
        <div style="
            transform: scale({scale});
            opacity: {opacity};
            border: {border};
            border-radius: 14px;
            padding: 18px;
            text-align: center;
            background: #111827;
            color: white;
            transition: all 0.25s ease-in-out;
        ">
            <h3 style="margin-bottom:6px;">{title}</h3>
            <p style="color:#9ca3af; margin:4px 0;">{subtitle}</p>
            <p style="font-size:13px; color:#cbd5e1;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_skewness_cards(skew_value: float):
    """Render 3 cards with dynamic highlight based on skewness."""

    is_sym = abs(skew_value) < 0.5
    is_right = skew_value > 0.5
    is_left = skew_value < -0.5

    col1, col2, col3 = st.columns(3)

    with col1:
        _card(
            "Symmetric",
            "Skewness ≈ 0",
            "Mean ≈ Median ≈ Mode",
            active=is_sym,
        )

    with col2:
        _card(
            "Right-Skewed (+)",
            "Skewness > 0",
            "Mode < Median < Mean",
            active=is_right,
        )

    with col3:
        _card(
            "Left-Skewed (−)",
            "Skewness < 0",
            "Mean < Median < Mode",
            active=is_left,
        )
