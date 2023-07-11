from fastapi import APIRouter

from schemas.auth import ResponseSchema, RegisterSchema, LoginSchema, ForgotPasswordSchema
from services.auth_service import AuthService
from i18n import t


router = APIRouter()


@router.post("/register", response_model=ResponseSchema)
def register(request_body: RegisterSchema):
    AuthService.register_service(request_body)
    return ResponseSchema(detail=t('lexikon.authentication.register.success'))

@router.post("/login", response_model=ResponseSchema)
def login(requset_body: LoginSchema):
    token = AuthService.logins_service(requset_body)
    return ResponseSchema(detail="Successfully login", result={"token_type": "Bearer", "access_token": token})

@router.post("/forgot-password", response_model=ResponseSchema)
def forgot_password(request_body: ForgotPasswordSchema):
    AuthService.forgot_password_service(request_body)
    return ResponseSchema(detail="Successfully update data!")
