from pydantic import BaseModel
from datetime import date
from enum import Enum
from pydantic.datetime_parse import parse_date

class Roles(str, Enum):
    user = "user"
    admin = "admin"

class UserBase(BaseModel):
    code: str
    name: str
    email: str
    role: Roles = "user"
