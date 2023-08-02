from pydantic import BaseModel


class UserBase(BaseModel):
    code: str
    name: str
    email: str
    password: str
    role: str = "learner"
