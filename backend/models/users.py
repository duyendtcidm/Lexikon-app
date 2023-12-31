from peewee import CharField, DateField, ForeignKeyField, fn, IntegerField, JOIN, Case
from models.base import BaseModel
from models.level import Level
from datetime import datetime, timezone


class Users(BaseModel):
    code = IntegerField()
    name = CharField()
    level_id = ForeignKeyField(Level, column_name='id')
    email = CharField()
    password = CharField()
    role = CharField()

    class Meta:
        table_name = 'users'

    @classmethod
    def find_by_email(cls, email):
        query = cls.select().where(cls.email == email, cls.active).dicts()
        return list(query)

    @classmethod
    def get_user_profile(cls, id):
        query = cls.select(cls.id, cls.name, cls.code, cls.email, cls.role, cls.level_id).where(cls.id == id,
                                                                                        cls.active).dicts()
        return list(query)

    @classmethod
    def find_by_name(cls, name):
        query = cls.select().where(cls.name == name, cls.active).dicts()
        return list(query)

    @classmethod
    async def update_password(cls, email: str, password: str):
        query = cls.update(password=password, modified_at=datetime.now(timezone.utc)).where(
            cls.email == email, cls.active
        )
        query.execute()
