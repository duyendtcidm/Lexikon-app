from utils.auth import Auth
from fastapi import APIRouter, Depends, Header

from core.endpoints import (
    authentication,
    users,
    home,
    look_up,
    practice,
    test,
    content
)

api_router = APIRouter()

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

api_router.include_router(
    look_up.router,
    prefix="/look_up",
    tags=["look_up"],
    # dependencies=[Depends(Auth())]
)

api_router.include_router(
    practice.router,
    prefix="/practice",
    tags=["practice"],
    # dependencies=[Depends(Auth())]
)

api_router.include_router(
    home.router,
    prefix="/home",
    tags=["home"],
    # dependencies=[Depends(Auth())]
)

api_router.include_router(
    test.router,
    prefix="/test",
    tags=["test"],
    # dependencies=[Depends(Auth())]
)

api_router.include_router(
    content.router,
    prefix="/content",
    tags=["content"],
    # dependencies=[Depends(Auth())]
)

# api_router.include_router(
#     grammar_question.router,
#     prefix="/grammar_question",
#     tags=["grammar_question"],
#     # dependencies=[Depends(Auth())]
# )

