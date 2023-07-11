from utils.auth import Auth
from fastapi import APIRouter, Depends, Header

from core.endpoints import (
    test,
    authentication
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