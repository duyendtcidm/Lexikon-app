from fastapi import APIRouter

from models.word import Word

router = APIRouter()

@router.get('/')
def get_list(
    find_word: str
):
    word = Word.get_list(find_word=find_word)
    print(word)
    return []