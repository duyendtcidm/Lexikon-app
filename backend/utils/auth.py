from fastapi import Request, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from typing import Optional
from base64 import b64decode
import json
from jose import jwt
# from models.master.member import Member
from starlette.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
)

from models.users import Users

SECRET_KEY = "lexikon23"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 600

class JWTRepo:

    def __init__(self, data: dict = {}, token: str = None):
        self.data = data
        self.token = token

    def generate_token(self, expires_delta: Optional[timedelta] = None):
        to_encode = self.data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return encode_jwt

    def decode_token(self):
        try:
            decode_token = jwt.decode(
                self.token, SECRET_KEY, algorithms=[ALGORITHM])
            return decode_token if decode_token["expires"] >= datetime.time() else None
        except:
            return {}

    @staticmethod
    def extract_token(token: str):
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


class Auth:
    def __init__(self):
        pass

    async def __call__(
        self,
        request: Request,
        authorization: HTTPAuthorizationCredentials = Security(HTTPBearer(auto_error=False))
    ):

        if authorization:
            token = authorization.credentials
            if not authorization.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail={"status": "Forbidden", "message": "Invalid authentication schema."})
            if not self.verify_jwt(token):
                raise HTTPException(
                    status_code=403, detail={"status": "Forbidden", "message": "Invalid token or expired token."})
            payload = JWTRepo.extract_token(token)
            if 'email' in payload:
                email = payload['email']
            else:
                email = request.headers.get('x-user-email')
                if not email:
                    raise HTTPException(
                        HTTP_403_FORBIDDEN, 'not auth'
                    )

            user = Users.get_or_none(email=email, active=True)

            if not user:
                raise HTTPException(
                    HTTP_403_FORBIDDEN, 'Member not found'
                )
            return user

        else:
            raise HTTPException(
                status_code=403, detail={"status": "Forbidden", "message": "Invalid authorization code."})

    @staticmethod
    def verify_jwt(jwt_token: str):
        return True if jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM]) is not None else False






