import requests

BASE_URL = "https://eventportal-9g45.onrender.com"


def signup(data):
    return requests.post(
        f"{BASE_URL}/signup",
        json=data
    )


def login(username, password):
    return requests.post(
        f"{BASE_URL}/login",
        data={
            "username": username,
            "password": password
        }
    )


def get_events():
    return requests.get(
        f"{BASE_URL}/events"
    )


def create_event(token, event_data):
    return requests.post(
        f"{BASE_URL}/events",
        json=event_data,
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


def book_event(token, event_id):
    return requests.post(
        f"{BASE_URL}/events/{event_id}/book",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


def get_my_bookings(token):
    return requests.get(
        f"{BASE_URL}/my-bookings",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


def get_users():
    return requests.get(
        f"{BASE_URL}/users"
    )