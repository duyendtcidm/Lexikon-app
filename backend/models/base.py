from typing import List
import re

from peewee import Model, BooleanField, BigIntegerField, fn
from playhouse.postgres_ext import DateTimeTZField
from config.database import db
from datetime import datetime, timezone
from peewee import DoesNotExist, SQL, fn, IntegerField, CharField
from fastapi import HTTPException
from utils.db import EXCLUDED, transaction
from utils.mecab import normalize_text


class BaseModel(Model):
    code = IntegerField()
    name = CharField()
    created_at = DateTimeTZField()
    created_by = BigIntegerField()
    modified_at = DateTimeTZField()
    modified_by = BigIntegerField()
    deleted_at = DateTimeTZField()
    deleted_by = BigIntegerField()
    active = BooleanField(default=True)

    class Meta:
        database = db

    @classmethod
    def get_word_grammar(cls, get_dict=True, search_input=None):
        query = cls.select().where(cls.active).order_by(cls.id)
        if search_input:
            if search_input != '':
                query = query.where(
                    cls.search_str.contains(
                        normalize_text(search_input).lower()
                    )
                )
        if get_dict:
            query = query.dicts()
        data = list(query)
        return data

    @classmethod
    def update_one(cls, id: int, data_update: dict):
        try:
            query = cls.update(**data_update, modified_at=datetime.now(timezone.utc)).where(
                cls.id == id
            )
            query.execute()

            data = cls.get_by_id(id)
            return data
        except DoesNotExist:
            raise HTTPException(
                status_code=404, detail=f"{cls.__name__} not found"
            )

    @classmethod
    def get_one(cls, id: int, get_dict=True):
        try:
            data = cls.get_or_none(id=id)
            if data and get_dict:
                data = data.__dict__['__data__']
            return data
        except DoesNotExist:
            raise HTTPException(
                status_code=404, detail=f"{cls.__name__} not found"
            )

    @classmethod
    def soft_delete(cls, id: int, deleted_by: int = None):
        try:
            data = cls.get_by_id(id)
            data.active = False
            data.deleted_at = datetime.now(timezone.utc)
            data.deleted_by = deleted_by
            data.save()
            return {"detail": f"Deleted {cls.__name__} {id}"}
        except DoesNotExist:
            raise HTTPException(
                status_code=404, detail=f"{cls.__name__} not found"
            )

    @classmethod
    def soft_delete_many(cls, ids, deleted_by: int = None):
        try:
            if (ids is None) or (len(ids) == 0):
                return "Nothing to delete"

            query = (cls.update(
                {
                    'active': False,
                    'deleted_at': datetime.now(timezone.utc),
                    'deleted_by': deleted_by
                }
            ).where(
                cls.id.in_(ids)
            ))

            query.execute()
            return {"detail": f"Deleted {cls.__name__} {','.join(str(x) for x in ids)}"}
        except DoesNotExist:
            raise HTTPException(
                status_code=404, detail=f"{cls.__name__} not found"
            )