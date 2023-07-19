from fastapi import APIRouter, Depends
from datetime import date

from utils.auth import Auth
from models.word_learning import WordLearning


router = APIRouter()

@router.get('/')
def get_list_practice(current_date: date, user=Depends(Auth())):
    list_word = WordLearning.get_by_date(user, current_date)
    for word in list_word:
        validate_pratice_date(word, current_date)
        mean = ''
        for meaning in word['meanings']:
            mean += meaning['mean']
        word['meanings'] = mean
        word['score'] = str(word['correct_times']) + '/' + str(word['practice_times'])
    return list_word

def validate_pratice_date(word, current_date):
    '''Check if users practice word frequently or not
        If practice_date < current_date -> update status, practice_times and practice_date before return to user
    '''
    if word['practice_date'] < current_date:
        word['practice_date'] = current_date
        word['status'] = (word['status'] > 1) and (word['status'] - 1) or 0
        word['practice_times'] += 1
    return word
