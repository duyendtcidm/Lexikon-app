from peewee import CharField, DateField, ForeignKeyField, fn, IntegerField, JOIN, Case
from playhouse.postgres_ext import JSONField
from models.base import BaseModel
from models.level import Level
from schemas import Roles
from sqlalchemy import Enum
from datetime import datetime
from i18n import t
from zoneinfo import ZoneInfo

class User(BaseModel):
    code = IntegerField()
    name = CharField()
    level_id = ForeignKeyField(Level, column_name='id')
    email = CharField()
    role = CharField()

    class Meta:
        table_name = 'user'
