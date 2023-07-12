from fastapi import APIRouter

from models.word import Word

router = APIRouter()

@router.get('/new_word')
def get_new_word(
    search_input: str
):
    word = Word.get_list(search_input=search_input)
    print(word)
    return []