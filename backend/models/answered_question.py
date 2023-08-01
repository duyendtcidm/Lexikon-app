# import jsonb as jsonb
from peewee import CharField, DateTimeField, ForeignKeyField, fn, IntegerField, JOIN, Case
from models.base import BaseModel

from models.users import Users
from models.question import Question

from models.level import Level


class AnsweredQuestion(BaseModel):
    user_id = ForeignKeyField(Users, column_name='user_id', field='id')
    question_id = ForeignKeyField(Question, column_name='question_id', field='id')
    status = IntegerField()

    class Meta:
        table_name = 'answered_question'

    @classmethod
    def get_list(cls, level, amount, question_type, user):
        query = (
            cls.select(
                cls.id,
                cls.status,
                Question.type.alias('type'),
                Question.content.alias('content'),
                Question.choices.alias('choices'),
                Question.answer.alias('answer'),
                Question.explanation.alias('explanation'),
                Level.name.alias('level')
            )
            .join(Question, on=cls.question_id == Question.id)
            .join(Level, on=Question.level_id == Level.id)
            .where(
                cls.status < 5,
                cls.user_id == user,
                Question.type == question_type,
                Level.name == level,
                cls.active)
            .limit(amount)
            .order_by(cls.status.asc())
            .dicts()
        )

        result = list(query)
        return result
