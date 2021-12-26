import requests
from retrying import retry


@retry(stop_max_attempt_number=3)
def http(method, url, **kwargs):
    if not kwargs.get('timeout'):
        kwargs['timeout'] = 60

    req_func = getattr(requests, method)
    resp = req_func(url, **kwargs)
    status_code = resp.status_code
    if status_code != 200:
        raise Exception(f'{status_code}: 异常请求 ')
    return resp
