# -*- coding: utf-8 -*-

import pynamodb_mate.api as pm
from .boto_ses import bsm, aws_access_key_id, aws_secret_access_key

st = pm.patterns.status_tracker


class StatusEnum(st.BaseStatusEnum):
    pending = 10
    in_progress = 20
    failed = 30
    succeeded = 40
    ignored = 50


class Task(
    st.BaseTask,
    pm.patterns.large_attribute.LargeAttributeMixin,
):
    class Meta:
        table_name = "zzone-dev-status-tracker"
        region = bsm.aws_region
        billing_mode = pm.constants.PAY_PER_REQUEST_BILLING_MODE
        aws_access_key_id = aws_access_key_id
        aws_secret_access_key = aws_secret_access_key

    detail_html: pm.OPTIONAL_STR = pm.UnicodeAttribute(null=True)
    geojson: pm.OPTIONAL_STR = pm.UnicodeAttribute(null=True)

    status_and_update_time_index = st.StatusAndUpdateTimeIndex()

    config = st.TrackerConfig.make(
        use_case_id="crawl",
        pending_status=StatusEnum.pending.value,
        in_progress_status=StatusEnum.in_progress.value,
        failed_status=StatusEnum.failed.value,
        succeeded_status=StatusEnum.succeeded.value,
        ignored_status=StatusEnum.ignored.value,
        n_pending_shard=1,
        n_in_progress_shard=1,
        n_failed_shard=1,
        n_succeeded_shard=1,
        n_ignored_shard=1,
        status_zero_pad=3,
        status_shard_zero_pad=3,
        max_retry=3,
        lock_expire_seconds=15,  # 抓取一个网页最多耗时 5-10 秒
    )
