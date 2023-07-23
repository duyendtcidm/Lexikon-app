from utils.mecab import normalize_text
from fastapi import HTTPException
from peewee import fn


def gen_search_str(**kwargs):
    params = []
    for key in kwargs:
        arg = kwargs.get(key)
        if arg:
            params.append(str(arg))

    params = set(params)
    search_str = "|".join(params)
    return search_str.lower()


def get_param(data: dict):
    param = data.copy()
    param['name'] = normalize_text(param['name'])
    if 'name_eng' in param:
        param['name_eng'] = (
            normalize_text(param['name_eng']) if param['name_eng'] else None
        )
    if 'yomi' in param:
        param['yomi'] = normalize_text(param['yomi']) if param['yomi'] else None
    if 'name_short' in param:
        param['name_short'] = (
            normalize_text(param['name_short']) if param['name_short'] else None
        )
    param['search_str'] = gen_search_str(
        code=param.get('code'),
        name=param.get('name'),
        name_eng=param.get('name_eng'),
        yomi=param.get('yomi'),
        short_name=param.get('name_short')
    )
    return param
