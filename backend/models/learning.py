from peewee import CharField, DateField, ForeignKeyField, fn, IntegerField, JOIN, Case, DateTimeField
from playhouse.postgres_ext import  DateTimeTZField
from models.base import BaseModel
from models.users import Users
from models.word import Word
from models.grammar import Grammar


class Learning(BaseModel):
    type = CharField()
    user_id = ForeignKeyField(Users, column_name='id')
    word_id = ForeignKeyField(Word, column_name='id')
    grammar_id = ForeignKeyField(Grammar, column_name='id')
    status = IntegerField()
    correct_times = IntegerField()
    practice_times = IntegerField()
    practice_date = DateTimeField()
    note = CharField()

    class Meta:
        table_name = 'learning'

    @classmethod
    def get_by_date(cls, user_id, date):
        query = (
            cls.select()
            .where(cls.active, cls.user_id == user_id, cls.practice_date == date)
            .order_by(cls.status.asc())
            .dicts()
        )
        return list(query)[0]