import streamlit as st


def metric_card(title, value):

    st.markdown(
        f"""
        <div class="metric-card">
            <h4>{title}</h4>
            <h2>{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


def section_header(title):

    st.markdown(
        f"""
        <div class="section-header">
            {title}
        </div>
        """,
        unsafe_allow_html=True
    )


def swot_card(title, items):

    st.markdown(f"### {title}")

    for item in items:
        st.markdown(f"• {item}")


def recommendation_box(text):

    st.info(text)