from fastapi import APIRouter, Depends, Security
from utils.auth import Auth, JWTRepo
from fastapi.security import HTTPAuthorizationCredentials

from models.users import Users

router = APIRouter()


@router.get("/")
def get_user_profile(user=Depends(Auth())):
    return Users.get_user_profile(user.id)
