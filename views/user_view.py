from fastapi import APIRouter

from models.user_model import User

from controller.user import user_register

router = APIRouter(prefix="/user")


@router.get("/")
def user_home():
    return "User Home"

@router.post("/register")
def user_register(user: User):
    return user_register(user)
