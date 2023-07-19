from fastapi import APIRouter, Depends
from datetime import date, timedelta

from models.word import Word
from models.word_learning import WordLearning

from utils.auth import Auth

router = APIRouter()

@router.get('/new_word/')
def get_new_word(
    search_input: str,
    user=Depends(Auth())
):
    word = Word.get_list(search_input=search_input)
    if word:
        word['kanji'] = word['kanji'].upper()
        pratice_date = date.today() + timedelta(days=1)
        is_learned = WordLearning.check_duplicate(user.id, word['id'])
        # check if user id learning this word or not, if not add to word_learning
        if not is_learned:
            data = {'user_id': user.id, 'word_id': word['id'], 'status': 0, 'correct_times': 0, 'practice_times': 0, 'practice_date' : pratice_date}
            WordLearning.create(**data)
    return word
