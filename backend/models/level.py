from peewee import CharField, DateField, ForeignKeyField, fn, IntegerField, JOIN, Case
from playhouse.postgres_ext import JSONField
from models.base import BaseModel
from datetime import datetime
from i18n import t
from zoneinfo import ZoneInfo


class Level(BaseModel):
    code = IntegerField()
    name = CharField()

    class Meta:
        table_name = 'level'
