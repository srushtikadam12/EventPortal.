from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# ======================
# User Schemas
# ======================

class UserAuth(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str


class UserOut(BaseModel):
    id: str
    username: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True


class SystemUser(BaseModel):
    id: str
    username: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True


# ======================
# JWT Schemas
# ======================

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: str
    exp: int


# ======================
# Event Schemas
# ======================

class EventCreate(BaseModel):
    title: str
    description: str
    location: str
    event_date: datetime


class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    event_date: Optional[datetime] = None


class EventOut(BaseModel):
    id: str
    title: str
    description: str
    location: str
    event_date: datetime

    class Config:
        from_attributes = True


# ======================
# Booking Schemas
# ======================

class BookingOut(BaseModel):
    booking_id: str
    event_id: str
    user_email: str

    class Config:
        from_attributes = True