from fastapi import APIRouter, Depends
from datetime import date

from utils.auth import Auth
from models.word_learning import WordLearning

import schemas.learning_word as learning_word_schemas


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

@router.put('/update_note')
def update_note(payload: learning_word_schemas.UpdateNotePayLoad, user=Depends(Auth())):
    WordLearning.update_one(payload.id, {'note': payload.note, 'modified_by': user.id})

@router.put('/update_status')
def update_status(payload: learning_word_schemas.UpdateStatusPayLoad, user=Depends(Auth())):
    WordLearning.update_one(
        payload.id,
        {
            'status': payload.status,
            'correct_times': payload.correct_times,
            'practice_times': payload.practice_times,
            'practice_date': payload.practice_date,
            'modified_by': user.id
        }
    )

@router.delete('/{id}')
def delete_size_group(id: int, user=Depends(Auth())):
    return WordLearning.soft_delete(id, user.id)

def validate_pratice_date(word, current_date):
    '''Check if users practice word frequently or not
        If practice_date < current_date -> update status, practice_times and practice_date before return to user
    '''
    if word['practice_date'] < current_date:
        word['practice_date'] = current_date
        word['status'] = (word['status'] > 1) and (word['status'] - 1) or 0
        word['practice_times'] += 1
    return word
