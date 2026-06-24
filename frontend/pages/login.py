import streamlit as st
from utils.api import login

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Login")

st.markdown("### Welcome Back")

with st.form("login_form"):

    username = st.text_input(
        "Username",
        placeholder="Enter your username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    submit = st.form_submit_button(
        "Login"
    )

if submit:

    if not username or not password:
        st.warning(
            "Please fill all fields"
        )

    else:

        response = login(
            username,
            password
        )

        if response.status_code == 200:

            data = response.json()

            st.session_state["token"] = data["access_token"]
            st.session_state["username"] = username

            st.success(
                f"Welcome {username}!"
            )

            st.rerun()

        else:

            try:
                st.error(
                    response.json()["detail"]
                )
            except:
                st.error(
                    "Login Failed"
                )

st.markdown("---")

st.info(
    "Don't have an account? Go to the Signup page from the sidebar."
)