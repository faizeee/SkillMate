from fastapi import APIRouter
from models.user import UserCreate, UserRead
from controllers.auth_controller import register,login
from models.base.auth_response import AuthResponse


router = APIRouter()

@router.post('/register',response_model=UserRead)
def register_user(user_input:UserCreate):
    return register(user_input)

@router.post('/login', response_model=AuthResponse)
def login_user (user_input:UserCreate):
    return login(user_input)