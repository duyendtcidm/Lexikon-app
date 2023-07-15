from fastapi import APIRouter, Depends
from utils.auth import Auth

router = APIRouter()


@router.post("/")
def index(data=Depends(Auth())):
    return {
        "Hello": "test api"
    }
