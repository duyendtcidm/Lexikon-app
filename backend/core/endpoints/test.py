from fastapi import APIRouter, Depends
from schemas import test as test_schema

from utils.db import transaction

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
    tried_question_list = []
    for ques in tried_question:
        tried_question_list.append(ques['id'])

    # Get more question to practice if tried_question is not enough
    if len(tried_question) < amount:
        list_question = Question.get_list(level, amount, question_type)
        for ques in list_question:
            if ques['id'] not in tried_question_list:
                tried_question.append(ques)
    return tried_question


@router.put('/update_status')
@transaction
def update_status_question(param: test_schema.UpdateStatus):
    answered_question = []
    new_question = []
    print(param)
    # list_question = Question.get_list(search_str)
    return True
