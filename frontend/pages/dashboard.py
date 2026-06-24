import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown(
    """
    <h1 style="
        font-size:70px;
        font-weight:700;
        line-height:1.0;
    ">
        Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        font-size:24px;
        color:gray;
    ">
        Welcome to your Event Management Dashboard.
    </p>
    """,
    unsafe_allow_html=True
)