from datetime import datetime

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from jose import jwt
from pydantic import ValidationError

from app.utils import ALGORITHM, SECRET_KEY
from app.schemas import TokenPayload, SystemUser
from app.database import get_db
from app.models import User


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


async def get_current_user(
    token: str = Depends(reuseable_oauth),
    db: Session = Depends(get_db)
) -> SystemUser:

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired"
            )

    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials"
        )

    user = db.query(User).filter(
        User.username == token_data.sub
    ).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user"
        )

    return SystemUser(
        id=user.id,
        username=user.username,
        email=user.email,
        role=user.role
    )