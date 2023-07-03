from fastapi import Request, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from base64 import b64decode
import json
# from jose import jwt
# from models.master.member import Member
from starlette.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
)

class AuthError(Exception):
    def __init__(self, error, status_code=HTTP_401_UNAUTHORIZED):
        self.error = error
        self.status_code = status_code


class Auth:
    def __init__(self):
        pass

    def __call__(
        self,
        request: Request,
        authorization: HTTPAuthorizationCredentials = Security(
            HTTPBearer(auto_error=False)
        ),
    ):
        if not authorization:
            raise HTTPException(
                HTTP_403_FORBIDDEN, 'not auth'
            )

        token = authorization.credentials
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
        return True





