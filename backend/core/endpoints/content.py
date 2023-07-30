from fastapi import APIRouter, Depends

from models.question import Question
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
    result = Question.get_one(id)
    return result

# @router.get('/word/')
# def get_word_by_admin(
#     user=Depends(Auth())
# ):
#     words = Word.get_by_creator(user)
#     return words
