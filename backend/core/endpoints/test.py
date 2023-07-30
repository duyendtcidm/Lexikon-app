from fastapi import APIRouter, Depends
from datetime import date

from utils.auth import Auth
from models.question import Question
from models.answered_question import AnsweredQuestion

router = APIRouter()


@router.get('/get_question_to_practice')
def get_list_question(
        level: str,
        amount: int,
        question_type: str,
        user=Depends(Auth())
):
    tried_question = AnsweredQuestion.get_list(level, amount, question_type, user)
    if len(tried_question) == 0:
        amount = amount
    else:
        amount = amount - len(tried_question)
    # Get more question to practice if tried_question is not enough
    list_question = Question.get_list(level, amount, question_type)
    return tried_question + list_question


# @router.get('/admin_list_owned_question')
# def get_list_question(user=Depends(Auth())):
#     list_question = Question.get_list(user)
#     return list_question


# @router.put('/update_status')
# def update_status_question(search_str: str):
#     list_question = Question.get_list(search_str)
#     return list_question

