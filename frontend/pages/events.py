import streamlit as st
from api import get_events, book_event

st.set_page_config(
    page_title="Events",
    page_icon="🎫",
    layout="wide"
)

st.title("🎫 Available Events")

response = get_events()

if response.status_code == 200:

    events = response.json()

    if len(events) == 0:
        st.warning("No Events Available")

    for event in events:

        with st.container():

            st.markdown("---")

            st.subheader(event["title"])

            st.write(
                f"📍 Location: {event['location']}"
            )

            st.write(
                f"📅 Date: {event['event_date']}"
            )

            st.write(
                event["description"]
            )

            if "token" in st.session_state:

                if st.button(
                    "Book Event",
                    key=event["id"]
                ):

                    booking = book_event(
                        st.session_state["token"],
                        event["id"]
                    )

                    if booking.status_code == 200:
                        st.success(
                            "Event Booked Successfully"
                        )
                    else:
                        st.error(
                            booking.text
                        )

else:
    st.error("Unable to Load Events")
