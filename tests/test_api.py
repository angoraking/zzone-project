# -*- coding: utf-8 -*-

from zzone import api


def test():
    _ = api


if __name__ == "__main__":
    from zzone.tests import run_cov_test

    run_cov_test(__file__, "zzone.api", preview=False)
