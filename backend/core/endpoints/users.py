from fastapi import APIRouter, Depends
from utils.auth import Auth

from models.users import Users

router = APIRouter()


@router.get("/")
def get_user_profile(user=Depends(Auth())):
    return Users.get_user_profile(user.id)
