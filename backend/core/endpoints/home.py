from fastapi import APIRouter, Depends
from utils.auth import Auth

from models.word_learning import WordLearning

router = APIRouter()


@router.get('/dashboard/')
def get_number_of_word_by_level(
        user=Depends(Auth())
):
    dashboard_status = WordLearning.get_word_by_level(user)
    return dashboard_status


@router.get('/calendar')
async def get_calendar_status(start_date: str, end_date: str, user=Depends(Auth())):
    calendar_status = WordLearning.get_word_by_status(start_date, end_date, user)
    return calendar_status
