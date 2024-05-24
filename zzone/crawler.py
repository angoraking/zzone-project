# -*- coding: utf-8 -*-

import polars as pl

from .paths import path_zip_code_database_csv
from .dynamodb import Task


def put_zipcode_list_into_dynamodb():
    df = pl.read_csv(path_zip_code_database_csv)
    Task.create_table(wait=True)
    with Task.batch_write() as batch:
        for zipcode in df["zip"]:
            zipcode = str(zipcode)
            task = Task.make(task_id=f"{zipcode}")
            batch.save(task)
