# -*- coding: utf-8 -*-

import json

from .config_def import Config
from .paths import path_config

config = Config(**json.loads(path_config.read_text()))
