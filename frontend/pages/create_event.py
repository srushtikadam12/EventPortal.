import streamlit as st
from api import create_event

st.set_page_config(
    page_title="Create Event",
    page_icon="➕",
    layout="wide"
)

st.title("➕ Create Event")

if "token" not in st.session_state:
    st.warning("Please login first")
    st.stop()

with st.form("create_event"):

    title = st.text_input(
        "Event Title"
    )

    description = st.text_area(
        "Description"
    )

    location = st.text_input(
        "Location"
    )

    event_date = st.datetime_input(
        "Event Date"
    )

    submit = st.form_submit_button(
        "Create Event"
    )

if submit:

    response = create_event(
        st.session_state["token"],
        {
            "title": title,
            "description": description,
            "location": location,
            "event_date": event_date.isoformat()
        }
    )

    if response.status_code == 200:
        st.success(
            "Event Created Successfully"
        )
    else:
        st.error(
            response.text
        )