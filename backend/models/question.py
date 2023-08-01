# import jsonb as jsonb
from peewee import CharField, fn, IntegerField, JOIN, Case, ForeignKeyField
from playhouse.postgres_ext import JSONField
from models.base import BaseModel
from models.level import Level

from utils.mecab import normalize_text


class Question(BaseModel):
    code = IntegerField()
    name = CharField()
    type = CharField()
    content = CharField()
    choices = JSONField()
    answer = IntegerField()
    explanation = JSONField()
    level_id = ForeignKeyField(Level, column_name='level_id', field='id')
    search_str = CharField()

    class Meta:
        table_name = 'question'

    @classmethod
    def get_list(cls, level, amount, question_type):
        query = (
            cls.select(
                cls.id,
                cls.name,
                cls.type,
                cls.content,
                cls.choices,
                cls.answer,
                cls.explanation,
                Level.name.alias('level')
            )
            .join(Level, on=cls.level_id == Level.id)
            .where(cls.type == question_type,
                   Level.name == level,
                   cls.active)
            .limit(amount)
            .order_by(cls.id)
            .dicts()
        )

        result = list(query)
        return result

    @classmethod
    def get_by_word(cls, name):
        query = (
            cls.select(
                cls.name,
                cls.type,
                cls.content,
                cls.choices,
                cls.answer,
                cls.explanation,
                Level.name.alias('level')
            )
            .join(Level, on=cls.level_id == Level.id)
            .where(cls.name == name, cls.active)
            .order_by(cls.id)
            .dicts()
        )

        result = list(query)
        return result


    @classmethod
    def __get_one__(cls, id):
        query = (
            cls.select(
                cls.id,
                cls.code,
                cls.name,
                cls.type,
                cls.content,
                cls.choices,
                cls.answer,
                cls.explanation,
                Level.name.alias('level')
            )
            .join(Level, on=(cls.level_id == Level.id))
            .where(cls.id == id, cls.active)
            .order_by(cls.id)
        )
        result = list(query.dicts())
        print(result)
        return result
    @classmethod
    def get_by_creator(cls, creator, search_input=None):
        query = (
            cls.select(
                cls.id,
                cls.code,
                cls.name,
                cls.type,
                cls.content,
                cls.choices,
                cls.answer,
                cls.explanation,
                Level.name.alias('level')
            )
            .join(Level, on=(cls.level_id == Level.id))
            .where(cls.created_by == creator, cls.active)
            .order_by(cls.id)
        )
        if search_input:
            if search_input != '':
                query = query.where(
                    cls.search_str.contains(
                        normalize_text(search_input).lower()
                    )
                )
        result = list(query.dicts())
        return result
