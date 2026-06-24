import streamlit as st

st.set_page_config(
    page_title="Event Management System",
    page_icon="📅",
    layout="wide"
)

# Session State
if "token" not in st.session_state:
    st.session_state["token"] = None

if "username" not in st.session_state:
    st.session_state["username"] = None

# Hide only footer
st.markdown(
    """
    <style>
    footer {
        visibility: hidden;
    }

    .block-container {
        padding-top: 3rem;
        max-width: 1200px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logout button if logged in
if st.session_state["token"]:

    col1, col2 = st.columns([9, 1])

    with col2:

        if st.button("Logout"):

            st.session_state.clear()
            st.rerun()

# Landing Page

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <h1 style="
        font-size:100px;
        font-weight:700;
        line-height:1.0;
        margin-bottom:20px;
    ">
        Event<br>
        Management
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        font-size:28px;
        color:#808080;
        margin-top:10px;
    ">
        Manage events with ease and book your favorite ones.
    </p>
    """,
    unsafe_allow_html=True
)