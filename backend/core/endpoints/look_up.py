from fastapi import APIRouter, Depends

from models.word import Word
from models.learning import Learning

from utils.auth import Auth

router = APIRouter()

@router.get('/new_word/')
def get_new_word(
    search_input: str,
    user=Depends(Auth())
):
    word = Word.get_list(search_input=search_input)
    if word:
        word[0]['kanji'] = word[0]['kanji'].upper()
    data = {'user_id': user.id, }

    Learning.create(**data)
    return word
