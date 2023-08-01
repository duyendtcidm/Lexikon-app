from schemas.base import Schema


class QuestionCreate(Schema):
    name: str
    type: str
    content: str
    choices: dict
    answer: int
    explanation: dict = {}
    level_id: int


class QuestionUpdate(QuestionCreate):
    id: int
