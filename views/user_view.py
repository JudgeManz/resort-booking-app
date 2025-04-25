from fastapi import APIRouter

from models.user_model import User

from controller.user import user_register

router = APIRouter(prefix="/user")


@router.get("/")
def home_user():
    return "User Home"

@router.post("/register")
def register_user(user: User):
    return user_register(user)
