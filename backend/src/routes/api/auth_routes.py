from fastapi import APIRouter, Depends
from sqlmodel import Session
from data.db import get_session
from models.user import UserCreate, UserRead
from controllers.auth_controller import register, login
from models.base.auth_response import AuthResponse


router = APIRouter()


@router.post("/register", response_model=UserRead)
def register_user(user_input: UserCreate, db: Session = Depends(get_session)):
    """Register a new user."""
    return register(user_input, db)


@router.post("/login", response_model=AuthResponse)
def login_user(user_input: UserCreate, db: Session = Depends(get_session)):
    """Authenticate a user."""
    return login(user_input, db)
