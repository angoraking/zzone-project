# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from s3pathlib import S3Path


@dataclasses.dataclass
class Config:
    """
    :param s3uri_data: 数据存放在哪个 S3 bucket? 这个是必须的.
    :param aws_profile: 用哪个 AWS profile? 这个只在本地开发时有用, 在 CI 中会用默认的.
    """

    s3uri_data: T.Optional[str] = dataclasses.field(default=None)
    aws_profile: T.Optional[str] = dataclasses.field(default=None)

    @property
    def s3dir_data(self) -> S3Path:
        return S3Path(self.s3uri_data).to_dir()

    @property
    def s3path_zip_code_database_csv_gz(self) -> S3Path:
        return self.s3dir_data.joinpath("zip_code_database.csv.gz")

    @property
    def s3dir_detail_html(self) -> S3Path:
        return self.s3dir_data.joinpath("detail_html").to_dir()
