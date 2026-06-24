from sqlalchemy import Column, String, DateTime, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(100), primary_key=True)
    username = Column(String(100), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(255))
    role = Column(String(20))

class Event(Base):
    __tablename__ = "events"

    id = Column(String(100), primary_key=True)
    title = Column(String(255))
    description = Column(String(500))
    location = Column(String(255))
    event_date = Column(DateTime)
    created_by = Column(String(100))

class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(String(100), primary_key=True)
    event_id = Column(String(100), ForeignKey("events.id"))
    user_email = Column(String(100))