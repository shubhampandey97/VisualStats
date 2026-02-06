import streamlit as st


def render_skewness_cards():
    """Render informational skewness interpretation cards."""

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style="border:1px solid #2a2a2a;
                        padding:20px;
                        border-radius:12px;
                        text-align:center">
                <h3 style="color:#34d399;">Symmetric</h3>
                <p>Skewness ≈ 0</p>
                <p>Mean ≈ Median ≈ Mode</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style="border:1px solid #2a2a2a;
                        padding:20px;
                        border-radius:12px;
                        text-align:center">
                <h3 style="color:#fbbf24;">Right-Skewed (+)</h3>
                <p>Skewness &gt; 0</p>
                <p>Mode &lt; Median &lt; Mean</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style="border:1px solid #2a2a2a;
                        padding:20px;
                        border-radius:12px;
                        text-align:center">
                <h3 style="color:#60a5fa;">Left-Skewed (−)</h3>
                <p>Skewness &lt; 0</p>
                <p>Mean &lt; Median &lt; Mode</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
