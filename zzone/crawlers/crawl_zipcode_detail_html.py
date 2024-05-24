# -*- coding: utf-8 -*-

import requests
from fake_useragent import UserAgent
import pynamodb_mate.api as pm
from datetime import datetime, timezone

from ..dynamodb import Task
from ..boto_ses import bsm
from ..config_load import config
from ..helpers import get_utc_now
from ..exc import HtmlDetailIsNotStandardError, CrawlTooFastError, NoDataError
from ..data_wrangling.api import T_ZIPCODE_LOOKUP_MAPPER

ua = UserAgent(browsers=["chrome", "edge", "firefox", "safari"])
st = pm.patterns.status_tracker


def get(zipcode: str) -> bytes:
    """
    For standard zipcode, it should return lots of Demographics data.
    You can use http get to get the data.
    """
    url = "https://www.unitedstateszipcodes.org/{zipcode}/".format(
        zipcode=zipcode.zfill(5)
    )
    headers = {
        "user-agent": ua.random,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6,ja;q=0.5",
        "cache-control": "no-cache",
        "origin": "https://www.unitedstateszipcodes.org",
        "dnt": "1",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "cookie": "from_zip=a%3A33%3A%7Bs%3A7%3A%22quality%22%3Bs%3A2%3A%2260%22%3Bs%3A8%3A%22latitude%22%3Bs%3A9%3A%2238.935776%22%3Bs%3A9%3A%22longitude%22%3Bs%3A10%3A%22-77.159523%22%3Bs%3A9%3A%22offsetlat%22%3Bs%3A9%3A%2238.935848%22%3Bs%3A9%3A%22offsetlon%22%3Bs%3A9%3A%22-77.16214%22%3Bs%3A6%3A%22radius%22%3Bs%3A4%3A%224800%22%3Bs%3A11%3A%22boundingbox%22%3Ba%3A4%3A%7Bs%3A5%3A%22north%22%3Bs%3A8%3A%2238.96841%22%3Bs%3A5%3A%22south%22%3Bs%3A9%3A%2238.903141%22%3Bs%3A4%3A%22east%22%3Bs%3A10%3A%22-77.116539%22%3Bs%3A4%3A%22west%22%3Bs%3A10%3A%22-77.202507%22%3B%7Ds%3A4%3A%22name%22%3BN%3Bs%3A5%3A%22line1%22%3BN%3Bs%3A5%3A%22line2%22%3Bs%3A16%3A%22Mclean%2C+VA+22101%22%3Bs%3A5%3A%22line3%22%3BN%3Bs%3A5%3A%22line4%22%3Bs%3A13%3A%22United+States%22%3Bs%3A5%3A%22cross%22%3BN%3Bs%3A5%3A%22house%22%3BN%3Bs%3A6%3A%22street%22%3BN%3Bs%3A7%3A%22xstreet%22%3BN%3Bs%3A8%3A%22unittype%22%3BN%3Bs%3A4%3A%22unit%22%3BN%3Bs%3A6%3A%22postal%22%3Bs%3A5%3A%2222101%22%3Bs%3A12%3A%22neighborhood%22%3BN%3Bs%3A4%3A%22city%22%3Bs%3A6%3A%22Mclean%22%3Bs%3A6%3A%22county%22%3Bs%3A14%3A%22Fairfax+County%22%3Bs%3A5%3A%22state%22%3Bs%3A8%3A%22Virginia%22%3Bs%3A7%3A%22country%22%3Bs%3A13%3A%22United+States%22%3Bs%3A11%3A%22countrycode%22%3Bs%3A2%3A%22US%22%3Bs%3A9%3A%22statecode%22%3Bs%3A2%3A%22VA%22%3Bs%3A10%3A%22countycode%22%3BN%3Bs%3A8%3A%22timezone%22%3Bs%3A16%3A%22America%2FNew_York%22%3Bs%3A8%3A%22areacode%22%3Bs%3A3%3A%22571%22%3Bs%3A4%3A%22uzip%22%3Bs%3A5%3A%2222101%22%3Bs%3A4%3A%22hash%22%3BN%3Bs%3A5%3A%22woeid%22%3Bs%3A8%3A%2212766820%22%3Bs%3A7%3A%22woetype%22%3Bs%3A2%3A%2211%22%3B%7D; fsbotchecked=true; _pk_id.29.e1c2=22645f0de4fa62fc.1639342613.; _fssid=e247ef7b-3dba-4c48-9ef4-0b524c5c1029; _pbjs_userid_consent_data=3524755945110770; _pubcid=67b709a0-31f2-4083-9892-1c52ea90b24e; __qca=P0-1329109895-1639342614147; __gads=ID=515a5b651c15ac4a:T=1639342614:S=ALNI_MYLV5YsXYXY-bqgZBZTGGzMVRsr-w; download_form=1; _lr_env_src_ats=false; panoramaId_expiry=1639970132164; _cc_id=c152aba02997cc1975f5db00b4e405da; panoramaId=a7bb805649e71f2be388a7df8a724945a702e8757b95adef306fccd06981c5c0; cookie=%7B%22id%22%3A%2201FMZ3TFK7W9V0KD7D3DAGHYMH%22%2C%22ts%22%3A1639505137378%7D; _pk_ref.29.e1c2=%5B%22%22%2C%22%22%2C1639519693%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; cto_bidid=l2Lm319sN0N3NW5ZRHpjelZpcDFnNEJtbmJPbGxoTVhiNnUlMkZWNGY0dTFhM252JTJGenV5MmdHVWoxM1MlMkZrclZVQnRGcmZtZGV5TTdOSFgyRmEwa1dZUTlQdVhtYjBsTCUyQlJtUFZaOUhRTCUyQkN0WTMyQ3UxWlBkNVF3M2N1U2hUaHJyRUJtelA; cto_bundle=Q1-VMF9MS0tEU0lBaWxWNDJGOSUyQm8zcDNCQ244amlkdnpad0gxNHBBOWZFQ1hUSlp4ViUyRnpKV090T0xkNXEyMFd1UWY1YVlBQnp6a210YnAlMkZFSSUyRlBYaVRoa0NUV3VHUFdZQnc5R05iUHpIdVl2TnBETzhJd2pFWTg2enE1bzVtQTd2UyUyQlIlMkIxZ0xjdTFXcDRsejRxaVdNMk5hJTJCekM0NG1yZE1UN3pYR0Z5U1pnOWY5dyUzRA; cto_bundle=zFE5QF9MS0tEU0lBaWxWNDJGOSUyQm8zcDNCQ2dPanI2S2FKRjZiaCUyRk5pcGdwbmJUNjdSY0RkUk1oY2FmOXdwcUtIcmEyYk1wVUhwbEVaNThKWSUyRnYxTnA3JTJCOCUyRnVNMWVPWkRiZ0hLRDdvR01MNmMzJTJGMDlFT0JncGJFc1pBSVY5eUgzVUtiNEczQVd4b01SejR4UUpSY2RuR0xUVkx0Q1lrZnN4MmVjWWliJTJGeU5seHRoTSUzRA; cto_bundle=zFE5QF9MS0tEU0lBaWxWNDJGOSUyQm8zcDNCQ2dPanI2S2FKRjZiaCUyRk5pcGdwbmJUNjdSY0RkUk1oY2FmOXdwcUtIcmEyYk1wVUhwbEVaNThKWSUyRnYxTnA3JTJCOCUyRnVNMWVPWkRiZ0hLRDdvR01MNmMzJTJGMDlFT0JncGJFc1pBSVY5eUgzVUtiNEczQVd4b01SejR4UUpSY2RuR0xUVkx0Q1lrZnN4MmVjWWliJTJGeU5seHRoTSUzRA"
    }
    res = requests.get(url, headers=headers)
    return res.content


def post(zipcode: str) -> bytes:
    """
    For non-standard zipcode, you need to send a post request to get the data.
    """
    origin = "https://www.unitedstateszipcodes.org"
    referer = "https://www.unitedstateszipcodes.org/{zipcode}/".format(
        zipcode=zipcode.zfill(5)
    )
    headers = {
        "user-agent": ua.random,
        "origin": origin,
        "referer": referer,
    }
    data = {"q": zipcode}
    res = requests.post(origin, headers=headers, data=data)
    return res.content


def is_standard_html(html: str) -> bool:
    """
    Standard HTML means that it has LineChart, PieChart or BarChat

    Example: https://www.unitedstateszipcodes.org/78065/
    """
    return (
        ("var LineChart" in html)
        or ("var PieChart" in html)
        or ("var BarChart" in html)
    )


def is_non_standard_html(html: str, zipcode: str) -> bool:
    """
    Non Standard HTML means that it has very basic info but no demographic info.

    Example: https://www.unitedstateszipcodes.org/78049/
    """
    pattern = f"Stats and other demographics information for ZIP code {zipcode} are not available"
    return pattern in html


def is_reached_limit_html(html: str) -> bool:
    """
    It means that you hit the limitation and get banned.

    If you hit the 1000 limitation for the website, you will see this information.
    """
    pattern = "You have reached your limit for the day.Consider purchasing a copy of the ZIP code database to make this many lookups"
    return pattern in html


def download_zipcode_html(zipcode: str):
    exec_ctx: st.ExecutionContext
    with Task.start(task_id=zipcode, detailed_error=True, debug=True) as exec_ctx:
        content = get(zipcode=zipcode)
        html = content.decode("utf-8", errors="ignore")
        print("------ 1 -------")
        print(html)
        if is_standard_html(html):
            task: Task = exec_ctx.task
            s3_put_time = get_utc_now()
            task.create_large_attribute_item(
                s3_client=bsm.s3_client,
                pk=task.task_id,
                sk=None,
                kvs=dict(detail_html=content),
                bucket=config.s3dir_detail_html.bucket,
                prefix=config.s3dir_detail_html.key,
                update_at=s3_put_time,
                attributes={},
                clean_up_when_failed=True,
            )
        else:
            content = post(zipcode=zipcode)
            html = content.decode("utf-8", errors="ignore")
            print("------ 2 -------")
            print(html)
            if is_non_standard_html(html, zipcode):
                raise HtmlDetailIsNotStandardError
            elif is_reached_limit_html(html):
                raise CrawlTooFastError
            else:
                raise NoDataError
