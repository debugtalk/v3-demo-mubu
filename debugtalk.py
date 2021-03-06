import time

import requests
from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def gen_request_id():
    return f"HRUN-{int(time.time() * 1000)}"


def sleep(n_secs):
    time.sleep(n_secs)


def get_expected_status_code(a, b):
    return a + b


def wait_until_complete():

    while True:
        resp = requests.get("xxx")
        if not resp.json()["ok"]:
            time.sleep(10)
            continue

        break
