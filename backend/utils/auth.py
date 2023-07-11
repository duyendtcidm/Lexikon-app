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

SECRET_KEY = "lexikon23"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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


class Auth(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(Auth, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(Auth, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail={"status": "Forbidden", "message": "Invalid authentication schema."})
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail={"status": "Forbidden", "message": "Invalid token or expired token."})
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail={"status": "Forbidden", "message": "Invalid authorization code."})

    @staticmethod
    def verify_jwt(jwt_token: str):
        return True if jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM]) is not None else False


# class Auth:
#     def __init__(self):
#         pass
#
#     def __call__(
#         self,
#         request: Request,
#         authorization: HTTPAuthorizationCredentials = Security(
#             HTTPBearer(auto_error=False)
#         ),
#     ):
#         if not authorization:
#             raise HTTPException(
#                 HTTP_403_FORBIDDEN, 'not auth'
#             )
#
#         token = authorization.credentials
        # get data between '.' - chua authen duoc
        # parts = token.split('.')
        # payload_b64 = parts[1] if parts else None
        # payload_json = b64decode(payload_b64 + '==').decode('utf-8')
        # payload = json.loads(payload_json)
        #
        # if 'username' in payload:
        #     email = payload['username']
        # else:
        #     email = request.headers.get('x-user-email')
        #     if not email:
        #         raise HTTPException(
        #             HTTP_403_FORBIDDEN, 'not auth'
        #         )
        #
        # member = Member.get_or_none(email=email, active=True)
        #
        # if not member:
        #     raise HTTPException(
        #         HTTP_403_FORBIDDEN, 'Member not found'
        #     )
        #
        # return member
        # return True





