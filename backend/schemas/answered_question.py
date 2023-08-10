from schemas.base import Schema
from typing import List


class NewQuestion(Schema):
    question_id: int = None
    status: int = None


class TriedQuestion(NewQuestion):
    id: int = None


class UpdateStatus(Schema):
    tried: List[TriedQuestion]
    new: List[NewQuestion]
