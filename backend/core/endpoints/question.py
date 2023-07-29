from fastapi import APIRouter, Depends
from datetime import date

from utils.auth import Auth
from models.question import Question

router = APIRouter()

@router.get('/get_by_name')
def get_list_by_word(name: str):
    list_question = Question.get_by_word(name)
    return list_question
