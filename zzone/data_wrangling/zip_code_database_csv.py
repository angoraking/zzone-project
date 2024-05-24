# -*- coding: utf-8 -*-

"""
zip_code_database.csv 是从 https://www.unitedstateszipcodes.org/zip-code-database/
下载下来的免费数据库 CSV 文件. 也是我们项目的起点. 这个模块专注于处理这个文件.
"""

import typing as T
import gzip
import dataclasses

import polars as pl

from ..paths import path_zip_code_database_csv
from ..config_load import config


def download_zip_code_database_csv():
    """
    从 S3 中下载 zip_code_database.csv.gz 到本地, 然后解压缩.
    """
    path_zip_code_database_csv.write_bytes(
        gzip.decompress(config.s3path_zip_code_database_csv_gz.read_bytes())
    )


def load_zipcode_list() -> T.List[str]:
    """
    把 path_zip_code_database.csv 中的 zipcode list 提取出来, 将其变成
    DynamoDB 中 的 Item 并保存.
    """
    df = pl.read_csv(path_zip_code_database_csv)
    return list(df["zip"].cast(str))


@dataclasses.dataclass
class Zipcode:
    """
    :param zip: str
    :param type: str, UNIQUE, STANDARD, PO BOX, MILITARY
    """

    zip: str = dataclasses.field()
    type: str = dataclasses.field()

    def is_unique(self) -> bool:
        return self.type == "UNIQUE"

    def is_standard(self) -> bool:
        return self.type == "STANDARD"

    def is_po_box(self) -> bool:
        return self.type == "PO BOX"

    def is_military(self) -> bool:
        return self.type == "MILITARY"


T_ZIPCODE_LOOKUP_MAPPER = T.Dict[str, Zipcode]


def load_zipcode_lookup_mapper() -> T_ZIPCODE_LOOKUP_MAPPER:
    """
    我并不需要将所有 zip_code_database.csv 中的数据都保存到 DynamoDB 中. 因为数据量不大,
    我们可以在本地内存中用一个字典来保存这些数据. 然后从 DynamoDB 取得 Key 之后, 去
    这个字典中查既可. 这个函数就是用来加载这个字典的.
    """
    df = pl.read_csv(path_zip_code_database_csv)
    mapper: T_ZIPCODE_LOOKUP_MAPPER = dict()
    for record in df.select([pl.col("zip").cast(str), "type"]).to_dicts():
        mapper[record["zip"]] = Zipcode(**record)
    return mapper
