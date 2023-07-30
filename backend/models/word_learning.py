from peewee import CharField, DateField, ForeignKeyField, fn, IntegerField, JOIN, Case, DateTimeField
from playhouse.postgres_ext import DateTimeTZField
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
        return data

    @classmethod
    def get_word_by_status(cls, start_date, end_date, user_id):
        query = (
            cls.select(
                cls.id,
                cls.status,
                cls.created_at
            )
            .where(
                cls.created_at.between(start_date, end_date) &
                cls.active &
                (cls.user_id == user_id)
            )
            .order_by(cls.created_at)
            .dicts()
        )
        words = list(query)
        new_words = []
        doing_words = []
        complete_words = []
        for word in words:
            word['created_at'] = word['created_at'].date()
            if word['status'] == 0:
                new_words.append(word)
            elif word['status'] == 5:
                complete_words.append(word)
            else:
                doing_words.append(word)

        return {
            "new_words": new_words,
            "doing_words": doing_words,
            "complete_words": complete_words
        }

    @classmethod
    def get_word_by_level(cls, user_id):
        query = (
            cls.select(
                cls.id,
                cls.status,
                Level.name.alias('level')
            )
            .where(
                (cls.word_id == Word.id) &
                (Word.level_id == Level.id) &
                cls.active &
                (cls.user_id == user_id)
            )
            .join(Word, on=(cls.word_id == Word.id))
            .join(Level, on=Word.level == Level.id)
            .dicts()
        )
        words = list(query)
        n1 = []
        n2 = []
        n3 = []
        n4 = []
        n5 = []
        for word in words:
            if word['level'] == 'N1':
                n1.append(word)
            elif word['level'] == 'N2':
                n2.append(word)
            elif word['level'] == 'N3':
                n3.append(word)
            elif word['level'] == 'N4':
                n4.append(word)
            else:
                n5.append(word)

        return {
            "n1": n1,
            "n2": n2,
            "n3": n3,
            "n4": n4,
            "n5": n5,
        }
