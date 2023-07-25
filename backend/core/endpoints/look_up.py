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
    words = Word.get_list(search_input=search_input)
    if len(words):
        for word in words:
            word['kanji'] = word['kanji'].upper()
            pratice_date = date.today() + timedelta(days=1)

            # check if user id learning this word or not
            # if not add to word_learning
            # else update practice date and status, correct_times, practice_time.
            learned_word = WordLearning.check_duplicate(user.id, word['id'])
            if not learned_word:
                data = {'user_id': user.id, 'word_id': word['id'], 'status': 0, 'correct_times': 0, 'practice_times': 0,
                        'practice_date': pratice_date}
                WordLearning.create(**data)
            else:
                WordLearning.update_one(learned_word, {
                    'status': 0,
                    'correct_times': 0,
                    'practice_times': 0,
                    'practice_date': pratice_date
                })
    return words
