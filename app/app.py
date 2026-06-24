from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

from sqlalchemy.orm import Session

from uuid import uuid4

from app.database import get_db, engine
from app.models import Base, User, Event, Booking
from app.schemas import (
    UserAuth,
    UserOut,
    TokenSchema,
    EventCreate,
    EventOut,
    EventUpdate,
)

from app.deps import get_current_user

from app.utils import (
    get_hashed_password,
    verify_password,
    create_access_token,
    create_refresh_token,
)

app = FastAPI()


Base.metadata.create_all(bind=engine)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/signup", response_model=UserOut)
async def create_user(
    data: UserAuth,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.username == data.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    user = User(
        id=str(uuid4()),
        username=data.username,
        email=data.email,
        password=get_hashed_password(data.password),
        role=data.role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user



@app.post("/login", response_model=TokenSchema)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username == form_data.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=400,
            detail="User not found"
        )

    if not verify_password(
        form_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=400,
            detail="Incorrect password"
        )

    return {
        "access_token": create_access_token(user.username),
        "refresh_token": create_refresh_token(user.username),
        "token_type": "bearer"
    }




@app.get("/users", response_model=list[UserOut])
async def get_users(
    db: Session = Depends(get_db)
):
    return db.query(User).all()




@app.post("/events", response_model=EventOut)
async def create_event(
    event: EventCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admins can create events"
        )

    new_event = Event(
        id=str(uuid4()),
        title=event.title,
        description=event.description,
        location=event.location,
        event_date=event.event_date,
        created_by=current_user.email
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event



@app.get("/events")
async def get_events(
    db: Session = Depends(get_db)
):
    return db.query(Event).all()



@app.get("/events/{event_id}")
async def get_event(
    event_id: str,
    db: Session = Depends(get_db)
):

    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event



@app.put("/events/{event_id}")
async def update_event(
    event_id: str,
    event: EventUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admins can update events"
        )

    existing_event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not existing_event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    update_data = event.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(existing_event, key, value)

    db.commit()
    db.refresh(existing_event)

    return existing_event



@app.delete("/events/{event_id}")
async def delete_event(
    event_id: str,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admins can delete events"
        )

    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    db.delete(event)
    db.commit()

    return {
        "message": "Event deleted successfully"
    }




@app.post("/events/{event_id}/book")
async def book_event(
    event_id: str,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    booking = Booking(
        booking_id=str(uuid4()),
        event_id=event_id,
        user_email=current_user.email
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking



@app.get("/my-bookings")
async def my_bookings(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return db.query(Booking).filter(
        Booking.user_email == current_user.email
    ).all()

