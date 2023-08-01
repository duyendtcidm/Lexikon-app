from fastapi import APIRouter, Depends

from services.master import reformat_string, get_param
from utils.db import transaction

from models.question import Question
from schemas import question as question_schemas
from models.word_learning import Word
from utils.auth import Auth

router = APIRouter()


@router.get('/question/')
def get_question_by_admin(
        search_input: str = None,
        user=Depends(Auth())
):
    questions = Question.get_by_creator(user, search_input=search_input)
    return questions


@router.get('/question/{id}')
def get_question_by_id(id: int):
    result = Question.__get_one__(id)
    return result[0]


@router.put('/')
@transaction
def update_question(
        question: question_schemas.QuestionUpdate,
        user=Depends(Auth()),
):
    question = reformat_string(question.dict())
    question = get_param(question)
    question['modified_by'] = user.id
    question_update = Question.update_one(question["id"], question)
    return question_update


@router.post('/')
@transaction
def create_question(
        question: question_schemas.QuestionCreate,
        user=Depends(Auth()),
):
    question = reformat_string(question.dict())
    question = get_param(question)
    question['created_by'] = user.id
    question_create = Question.create(**question)
    return question_create


@router.delete('/question/{id}')
def delete_unit(id: int, member=Depends(Auth())):
    return Question.soft_delete(id, member.id)
