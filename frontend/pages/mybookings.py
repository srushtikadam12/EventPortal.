import streamlit as st
import pandas as pd
from api import get_my_bookings

st.set_page_config(
    page_title="My Bookings",
    page_icon="📖",
    layout="wide"
)

st.title("📖 My Bookings")

if "token" not in st.session_state:
    st.warning("Please login first")
    st.stop()

response = get_my_bookings(
    st.session_state["token"]
)

if response.status_code == 200:

    bookings = response.json()

    if len(bookings) == 0:
        st.info("No Bookings Found")

    else:

        df = pd.DataFrame(bookings)

        st.dataframe(
            df,
            use_container_width=True
        )

else:
    st.error(
        "Unable to Fetch Bookings"
    )
