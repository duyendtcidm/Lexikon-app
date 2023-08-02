from pydantic import BaseModel
from config.database import PeeweeGetterDict
from datetime import date
from pydantic.datetime_parse import parse_date


# def validate_date(v) -> date:
#     try:
#         v = str(v)
#         if (
#             len(v) != 10
#             and 1 <= int(v[5:7]) <= 12
#             and 1 <= int(v[8:]) <= 31
#             and v[4] != '-'
#             and v[7] != '-'
#         ):
#             raise ValueError("Don't allow value")
#
#     except Exception:
#         raise ValueError("Don't allow value")
#     return parse_date(v)
#
#
# class StrictDate(date):
#     @classmethod
#     def __get_validators__(cls):
#         yield validate_date


class Schema(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
