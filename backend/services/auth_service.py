import base64
from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException

from passlib.context import CryptContext
from models.users import Users
from schemas.auth import LoginSchema, ForgotPasswordSchema, RegisterSchema
from utils.auth import JWTRepo
from i18n import t


# Encrypt password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:

    @staticmethod
    def register_service(register: RegisterSchema):
        register.password = pwd_context.hash(register.password)
        # Checking the same email
        _email = Users.find_by_email(register.email)
        if _email:
            raise HTTPException(
                status_code=400, detail=t('lexikon.authentication.register.existed_email'))

        else:
            #  insert to tables
            Users.create(**register.dict())

    @staticmethod
    def logins_service(login: LoginSchema):
        _user = Users.find_by_email(login.email)

        if _user is not None:
            if not pwd_context.verify(login.password, _user[0]['password']):
                raise HTTPException(
                    status_code=400, detail="Invalid Password !")
            return JWTRepo(data={"username": _user[0]['name']}).generate_token()
        raise HTTPException(status_code=404, detail="Username not found !")

    @staticmethod
    async def forgot_password_service(forgot_password: ForgotPasswordSchema):
        _email = await Users.find_by_email(forgot_password.email)
        if _email is None:
            raise HTTPException(status_code=404, detail="Email not found !")
        await Users.update_password(forgot_password.email, pwd_context.hash(forgot_password.new_password))


# Generate roles manually
# async def generate_role():
#     _role = await RoleRepository.find_by_list_role_name(["admin", "user"])
#     if not _role:
#         await RoleRepository.create_list(
#             [Role(id=str(uuid4()), role_name="admin"), Role(id=str(uuid4()), role_name="user")])
