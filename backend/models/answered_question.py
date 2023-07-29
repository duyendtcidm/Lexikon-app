# import jsonb as jsonb
from peewee import CharField, ArrayField, DateTimeField, ForeignKeyField, fn, IntegerField, JOIN, Case
from models.base import BaseModel

from models.users import Users
from models.question import Question


class AnsweredQuestion(BaseModel):
    user_id: ForeignKeyField(Users, column_name='user_id', field='id')
    question_id: ForeignKeyField(Question, column_name='question_id', field='id')
    status: IntegerField()
    correct_times: IntegerField()
    practice_times: IntegerField()
    practice_date: DateTimeField()

    class Meta:
        table_name = 'answered_question'
