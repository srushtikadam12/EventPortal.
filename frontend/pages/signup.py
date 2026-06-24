import streamlit as st
from utils.api import signup

st.set_page_config(
    page_title="Signup",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Create Account")

with st.form("signup_form"):

    username = st.text_input(
        "Username"
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Role",
        [
            "user",
            "admin"
        ]
    )

    submit = st.form_submit_button(
        "Create Account"
    )

if submit:

    response = signup(
        {
            "username": username,
            "email": email,
            "password": password,
            "role": role
        }
    )

    if response.status_code == 200:

        st.success(
            "Account Created Successfully"
        )

    else:

        try:
            st.error(
                response.json()["detail"]
            )
        except:
            st.error(
                "Signup Failed"
            )