from utils.auth import Auth
from fastapi import APIRouter, Depends, Header

from core.endpoints import (
    test
)


api_router = APIRouter()

api_router.include_router(
    test.router,
    prefix="/test",
    tags=["test"],
    # dependencies=[Depends(Auth), Depends(app_context_dependency)]
    # dependencies=[Depends(Auth)]
)