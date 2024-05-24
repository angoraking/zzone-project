# -*- coding: utf-8 -*-

from boto_session_manager import BotoSesManager
from s3pathlib import context
from .config_load import config

bsm = BotoSesManager(profile_name=config.aws_profile)
context.attach_boto_session(bsm.boto_ses)
credentials = bsm.boto_ses.get_credentials()
aws_access_key_id = credentials.access_key
aws_secret_access_key = credentials.secret_key
