from peewee import CharField, ForeignKeyField, fn, IntegerField, JOIN, Case
from playhouse.postgres_ext import JSONField
from models.base import BaseModel
from models.level import Level

class Word(BaseModel):
    code = IntegerField()
    word = CharField()
    meaning = JSONField()
    kanji = CharField()
    pronunciation = CharField()
    level_id = ForeignKeyField(Level, column_name='level', field='id')

    class Meta:
        table_name = 'word'
