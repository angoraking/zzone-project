# -*- coding: utf-8 -*-


class HtmlDetailIsNotStandardError(ValueError):
    """
    有些不是 STANDARD 的 zipcode 的 zipcode detail 页面里面没有任何 demographics 数据.
    检测到这一情况就抛出这个异常.
    """
    pass


class CrawlTooFastError(ValueError):
    """
    当你爬的太快, 服务器就会返回一个静态页面, 你就再也拿不到数据了. 此时就抛出这个异常.
    """
    pass


class NoDataError(ValueError):
    """
    对于有些 zipcode, 直接网站就给你一个广告页面, 没有任何数据. 此时就抛出这个异常.
    """
    pass
