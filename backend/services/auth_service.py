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
        user = {}
        if len(_user):
            user['email'] = _user[0]['email']
            user['name'] = _user[0]['name']
            user['role'] = _user[0]['role']
            if not pwd_context.verify(login.password, _user[0]['password']):
                raise HTTPException(
                    status_code=400, detail=t('lexikon.authentication.login.invalid_password'))
            return {'token': JWTRepo(data={"email": _user[0]['email']}).generate_token(), 'user': user}
        raise HTTPException(status_code=404, detail=t('lexikon.authentication.login.invalid_email'))

    @staticmethod
    async def forgot_password_service(forgot_password: ForgotPasswordSchema):
        _email = await Users.find_by_email(forgot_password.email)
        if _email is None:
            raise HTTPException(status_code=404, detail=t('lexikon.authentication.login.invalid_email'))
        await Users.update_password(forgot_password.email, pwd_context.hash(forgot_password.new_password))

