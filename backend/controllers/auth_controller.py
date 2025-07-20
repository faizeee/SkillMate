from fastapi import HTTPException
from sqlmodel import Session, select
from models.user import User
from core.auth import get_password_hash, verify_password,create_access_token
from models.user import UserCreate,UserRead
from models.base.auth_response import AuthResponse

def register(user_input:UserCreate,db:Session)->UserRead:
    """
    Registers a new user.
    Checks if username already exists, hashes password, and saves to DB.
    """
    username = user_input.username

    if db.exec(select(User).where(User.username == username)).first() :
        raise HTTPException(status_code=400,detail="Username already Exits")
    
    hashed = get_password_hash(user_input.password)
    user = User(username=username,password_hash=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"id":user.id, "username":user.username}

def login(user_input: UserCreate, db:Session) -> AuthResponse:
    username = user_input.username
    user =  db.exec(select(User).where(User.username == username)).first()

    if not user or not verify_password(user_input.password, user.password_hash):
        raise HTTPException(status_code=400, detail= "Invalid Username or Password")
    
    token = create_access_token({"sub":user.username})
    return AuthResponse.from_token(token=token)


