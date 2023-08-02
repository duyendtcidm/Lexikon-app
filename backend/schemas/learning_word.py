from datetime import date

from schemas.base import Schema
from typing import List


class UpdateNotePayLoad(Schema):
    id: int
    note: str


class UpdateStatusPayLoad(Schema):
    id: int
    status: int
    correct_times: int
    practice_times: int
    practice_date: date
