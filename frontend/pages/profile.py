import streamlit as st

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)

st.title("👤 User Profile")

if "token" not in st.session_state:
    st.warning("Please login first")
    st.stop()

st.success("You are logged in")

if st.button("🚪 Logout"):

    st.session_state.clear()

    st.success("Logged Out Successfully")

    st.rerun()