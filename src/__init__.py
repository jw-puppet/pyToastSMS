import requests

from config import api, secret

import functools


def rest_wrap(func):
    """
    구현된 API 메서드를 config.api 를 참조해 REST API Request 를 생성해 요청하고 json response 를 반환..

    :param func: 요청할 API 메서드
    :return: json response.
    """

    @functools.wraps(func)
    def func_wrapper(*args, **kwargs) -> dict:

        # assemble_target_url
        url = api['host']
        url += "/sms/" + api['version']
        url += "/appKeys/" + secret['app_key']
        url += api[func.__name__]['path']

        # assemble_json_body
        body = func(*args, **kwargs)

        method = api[func.__name__]['method']
        if method == "GET":
            conn = requests.get(url, params=body)
        elif method == "POST":
            conn = requests.post(url, json=body)
        elif method == "DELETE":
            conn = requests.delete(url, params=body)
        else:
            # exception handler 미구현.
            raise NotImplementedError()
        response = conn.json()
        return response

    return func_wrapper
