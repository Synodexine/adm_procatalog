from datetime import datetime
from typing import List

from couchbase.cluster import Bucket
from pydantic import BaseModel

from . import filter_query, upsert


def output_pydantic_model(model: BaseModel):
    def generate_model(func):
        def wrapper(*args, **kwargs):
            db_result = func(*args, **kwargs)
            if type(db_result) == list:
                return [model.parse_obj(db_dict) for db_dict in func()]
            return model.parse_obj(db_result)
        return wrapper
    return generate_model


def print_execution_time(func):
    def get_timing(*args, **kwargs):
        start = datetime.now()
        func_result = func(*args, **kwargs)
        print(datetime.now() - start)
        return func_result
    return get_timing


async def get_document_if_exists(bucket: Bucket, model: BaseModel):
    data = model.dict()
    result = await filter_query(bucket, **data)
    return result[0] if result else None


async def get_or_create(bucket: Bucket, model: BaseModel):
    document = await get_document_if_exists(bucket, model)
    if not document:
        document = await upsert(bucket, model)
    return document


async def get_or_bulk_create(bucket: Bucket, models: List[BaseModel]):
    result_models = list()
    if models:
        for model in models:
            result_models.append(await get_or_create(bucket, model))
    return result_models


async def bulk_create(bucket: Bucket, models: List[BaseModel]):
    result_models = list()
    for model in models:
        result_models.append(await upsert(bucket, model))
    return result_models
