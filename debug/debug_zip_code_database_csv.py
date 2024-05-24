# -*- coding: utf-8 -*-

from zzone.data_wrangling.zip_code_database_csv import (
    download_zip_code_database_csv,
    load_zipcode_list,
    load_zipcode_lookup_mapper,
)
from rich import print as rprint

download_zip_code_database_csv()
# rprint(load_zipcode_list()[:10])
# rprint(load_zipcode_lookup_mapper()["20036"])
