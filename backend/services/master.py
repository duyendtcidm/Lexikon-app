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
    if 'yomi' in param:
        param['yomi'] = normalize_text(param['yomi']) if param['yomi'] else None
    param['search_str'] = gen_search_str(
        code=param.get('code'),
        name=param.get('name'),
        yomi=param.get('yomi')
    )
    return param


def reformat_string(data: dict):
    # Remove white spaces at top & bottom
    formatted_data = {k: normalize_text(v).strip() if (type(v) is str and v is not None) else v for k, v in
                      data.items()}
    return formatted_data
