from fastapi import APIRouter, Depends
from schemas import answered_question as test_schema

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
        tried_question_list.append(ques['question_id'])

    # Get more question to practice if tried_question is not enough
    if len(tried_question) < amount:
        list_question = Question.get_list(level, amount, question_type)
        for ques in list_question:
            if ques['question_id'] not in tried_question_list:
                tried_question.append(ques)
    return tried_question


@router.put('/update_status')
@transaction
def update_status_question(param: test_schema.UpdateStatus, user=Depends(Auth())):
    data = param.dict()
    answered_question = []
    new_question = []
    for ques in data["tried"]:
        answered_question.append({"id": ques["id"], "user_id": user.id, "question_id": ques["question_id"], "status": ques["status"]})
    for ques in data["new"]:
        new_question.append({"user_id": user.id, "question_id": ques["question_id"], "status": ques["status"]})
    if len(new_question):
        AnsweredQuestion.insert_many(new_question).dicts().execute()
    if len(answered_question):
        for ques in answered_question:
            AnsweredQuestion.update(status=ques['status']).where(
                AnsweredQuestion.id == ques['id'],
                AnsweredQuestion.user_id == ques['user_id'],
                AnsweredQuestion.question_id == ques['question_id'],
                AnsweredQuestion.modified_by == user.id,
                AnsweredQuestion.active
            ).execute()
    return True
