from peewee import CharField, ForeignKeyField, fn, IntegerField, JOIN, Case
from playhouse.postgres_ext import JSONField
from models.base import BaseModel
from models.level import Level

class Grammar(BaseModel):
    code = IntegerField()
    name = CharField()
    usage = JSONField()
    kanji = CharField()
    search_str = CharField()
    level = ForeignKeyField(Level, column_name='level', field='id')


    class Meta:
        table_name = 'grammar'

    @classmethod
    def get_list(cls, get_dict=True, search_input=None):
        query = (
            cls.select(
                cls.id,
                cls.name,
                cls.code,
                cls.usage,
                cls.kanji,
                cls.yomi,
                Level.name.alias("level"),
            )
            .join(Level, on=cls.level == Level.id)
            .where(cls.name == search_input, cls.active)
            .order_by(cls.id))
        if get_dict:
            query = query.dicts()
        data = list(query)
        return data


