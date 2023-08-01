from schemas.base import Schema
from typing import List


class Status(Schema):
    id: int
    status: int


class UpdateStatus(Status):
    tried: List[Status]
    new: List[Status]
