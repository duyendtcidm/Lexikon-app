from fastapi import APIRouter, Depends
from utils.auth import Auth

router = APIRouter()


@router.get("/")
def index(data=Depends(Auth())):
# def index():
    return {
        "Hello": "test api"
    }
