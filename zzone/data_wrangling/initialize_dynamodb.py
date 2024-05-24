# -*- coding: utf-8 -*-


import polars as pl

from .zip_code_database_csv import load_zipcode_list
from ..dynamodb import Task


def put_zipcode_list_into_dynamodb():
    """
    把 path_zip_code_database.csv 中的 zipcode list 提取出来, 将其变成
    DynamoDB 中 的 Item 并保存.
    """
    zipcode_list = load_zipcode_list()
    Task.create_table(wait=True)
    with Task.batch_write() as batch:
        for zipcode in zipcode_list:
            task = Task.make(task_id=zipcode)
            batch.save(task)
