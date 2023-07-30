# import jsonb as jsonb
from peewee import CharField, fn, IntegerField, JOIN, Case, ForeignKeyField
from playhouse.postgres_ext import JSONField
from models.base import BaseModel
from models.level import Level


class Question(BaseModel):
    code = IntegerField()
    name = CharField()
    type = CharField()
    content = CharField()
    choices = JSONField()
    answer = IntegerField()
    explanation = JSONField()
    level_id = ForeignKeyField(Level, column_name='level_id', field='id')

    class Meta:
        table_name = 'question'

    @classmethod
    def get_list(cls, level, amount, question_type):
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
