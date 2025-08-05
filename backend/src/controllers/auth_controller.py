"""Contains user authentication logic: register and login handlers."""

from fastapi import HTTPException
from sqlmodel import Session, select
from models.user import User
from sqlalchemy.orm import selectinload
from core.auth import get_password_hash, verify_password, create_access_token
from models.user import UserCreate, UserRead
from models.base.auth_response import AuthResponse
from utils.roles import Roles


def register(user_input: UserCreate, db: Session) -> UserRead:
    """Register a new user.

    Checks if username already exists, hashes password, and saves to DB.

        Args:
            user_input (UserCreate): Submitted data by user.
            db (Session): Need a resolved Session object by route.
        Returns:
            UserRead: User information.
    """
    username = user_input.username

    if db.exec(select(User).where(User.username == username)).first():
        raise HTTPException(status_code=400, detail="Username already Exits")

    hashed = get_password_hash(user_input.password)
    user = User(username=username, password_hash=hashed, user_role_id=Roles.USER.value)
    db.add(user)
    db.commit()
    db.refresh(user, attribute_names=["role"])

    return {"id": user.id, "username": user.username}


def login(user_input: UserCreate, db: Session) -> AuthResponse:
    """Handel User Login.

    Checks if user exits, return user token
        Args:
            user_input (UserCreate): Submitted data by user.
            db (Session): Need a resolved Session object by route.
        Returns:
            AuthResponse: User information and token.
    """
    username = user_input.username
    statement = (
        select(User).where(User.username == username).options(selectinload(User.role))
    )
    user = db.exec(statement).first()

    if not user or not verify_password(user_input.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid Username or Password")

    token = create_access_token({"sub": user.username})
    # user_dict = user.model_validate(user)
    # user_dict["role_name"] = user.role.title
    user_data = UserRead.model_validate(
        user
    )  # OR UserRead({**user.model_dump(exclude={"password_hash"}), "role_name":user.role.title})
    return AuthResponse.from_token(
        token=token,
        user=user_data,
    )
