from peewee import CharField, ForeignKeyField, fn, IntegerField, JOIN, Case
from playhouse.postgres_ext import JSONField
from models.base import BaseModel
from models.level import Level


class Word(BaseModel):
    code = IntegerField()
    name = CharField()
    meanings = JSONField()
    kanji = CharField()
    yomi = CharField()
    search_str = CharField()
    level_id = ForeignKeyField(Level, column_name='level_id', field='id')
    synonym = JSONField()
    antonym = JSONField()
    kanren = JSONField()
    usage_pattern = JSONField()
    compound_word = JSONField()
    common_word = JSONField()

    class Meta:
        table_name = 'word'

    @classmethod
    def get_list(cls, get_dict=True, search_input=None):
        query = (
            cls.select(
                cls.id,
                cls.name,
                cls.code,
                cls.meanings,
                cls.kanji,
                cls.yomi,
                Level.name.alias("level"),
                cls.synonym,
                cls.antonym,
                cls.kanren,
                cls.usage_pattern,
                cls.compound_word,
                cls.common_word
            )
            .join(Level, on=cls.level_id == Level.id)
            .where(cls.search_str.contains(search_input), cls.active)
            .order_by(cls.id))
        if get_dict:
            query = query.dicts()
        data = list(query)
        return data

    @classmethod
    def get_by_creator(cls, creator):
        query = (
            cls.select()
            .where(cls.created_by == creator, cls.active)
            .order_by(cls.id)
            .dicts()
        )
        result = list(query)
        return result
