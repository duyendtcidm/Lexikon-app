# import jsonb as jsonb
from peewee import CharField, DateField, ForeignKeyField, fn, IntegerField, JOIN, Case
from playhouse.postgres_ext import JSONField
from models.base import BaseModel

class Test(BaseModel):
    word: JSONField()

    class Meta:
        table_name = 'test_word'