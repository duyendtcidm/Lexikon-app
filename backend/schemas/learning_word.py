from schemas.base import Schema, StrictDate
from typing import List

class UpdateNotePayLoad(Schema):
    id: int
    note: str
