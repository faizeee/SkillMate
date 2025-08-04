from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlmodel import Session, select
from core.config import config
from data.db import get_session
from models import User
from sqlalchemy.orm import selectinload

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)
):
    """Check and verify the loge in user or not."""
    try:
        payload = jwt.decode(token, config.secret_key, algorithms=[config.algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid User Token")
        statement = (
            select(User)
            .where(User.username == username)
            .options(selectinload(User.role))
        )
        user = db.exec(statement).first()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid Token")
