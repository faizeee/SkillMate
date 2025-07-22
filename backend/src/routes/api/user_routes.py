# from fastapi import APIRouter, Depends
# from models.user import UserRead
# from models.user import User
# from services.auth_service import get_current_user

# user_router = APIRouter()

# @user_router.get("/",response_model=UserRead)
# def get_user_data(user:User = Depends(get_current_user)):
#     return {"id":user.id, "username":user.username}
