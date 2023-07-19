from peewee import CharField, DateField, ForeignKeyField, fn, IntegerField, JOIN, Case, DateTimeField
from playhouse.postgres_ext import  DateTimeTZField
from peewee import (JOIN)
from models.base import BaseModel
from models.level import Level
from models.users import Users
from models.word import Word
# from models.grammar import Grammar


class WordLearning(BaseModel):
    user_id = ForeignKeyField(Users, column_name='user_id')
    word_id = ForeignKeyField(Word, column_name='word_id')
    status = IntegerField()
    correct_times = IntegerField()
    practice_times = IntegerField()
    practice_date = DateTimeField()
    note = CharField()

    class Meta:
        table_name = 'word_learning'

    @classmethod
    def get_by_date(cls, user_id, date):
        query = (
            cls.select(
                cls.id,
                Word.name.alias('name'),
                Word.yomi.alias('yomi'),
                Word.meanings.alias('meanings'),
                Word.kanji.alias('kanji'),
                Word.synonym.alias('synonym'),
                Word.antonym.alias('antonym'),
                Word.kanren.alias('kanren'),
                Word.usage_pattern.alias('usage_pattern'),
                Word.compound_word.alias('compound_word'),
                Word.common_word.alias('common_word'),
                Level.name.alias('level'),
                cls.status,
                cls.correct_times,
                cls.practice_times,
                cls.practice_date,
                cls.note
           )
            .join(Word, on=(cls.word_id == Word.id))
            .join(Level, on=Word.level == Level.id)
            .where(cls.active, cls.user_id == user_id, cls.practice_date <= date)
            .order_by(cls.status.asc())
            .dicts()
        )
        return list(query)

    @classmethod
    def check_duplicate(cls, user_id, word_id):
        query = cls.select().where(cls.active, cls.user_id == user_id, cls.word_id == word_id)
        data = list(query)
        if len(data):
            print(data[0])
        return data
