from utils.auth import Auth
from fastapi import APIRouter, Depends, Header

from core.endpoints import (
    test,
    authentication,
    users
)


api_router = APIRouter()

api_router.include_router(
    test.router,
    prefix="/test",
    tags=["test"]
)

api_router.include_router(
    authentication.router,
    prefix="/auth",
    tags=["Authentication"]
)

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["user"],
    dependencies=[Depends(Auth())]
)
