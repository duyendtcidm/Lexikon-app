from fastapi import HTTPException
import logging
import re
from typing import TypeVar, Optional

from pydantic import BaseModel

T = TypeVar('T')

# get root logger
logger = logging.getLogger(__name__)


class RegisterSchema(BaseModel):
    name: str
    email: str
    password: str
    role: str = "learner"


class LoginSchema(BaseModel):
    email: str
    password: str


class ForgotPasswordSchema(BaseModel):
    email: str
    new_password: str


class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None
