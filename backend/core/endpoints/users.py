from fastapi import APIRouter,Depends,Security
from utils.auth import Auth, JWTRepo
from fastapi.security import HTTPAuthorizationCredentials

from models.users import Users

router = APIRouter()


@router.get("/")
def get_user_profile(credentials: HTTPAuthorizationCredentials = Security(Auth())):
    token = JWTRepo.extract_token(credentials)
    result = Users.get_user_profile(token['email'])
    return result
