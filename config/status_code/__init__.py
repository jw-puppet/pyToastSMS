import os

import yaml

_CODE_BOOK_PATH = './src/status_code/statusCode.yml'

# Load Status Code book yaml.
assert os.path.exists(_CODE_BOOK_PATH)
with open(_CODE_BOOK_PATH, 'r') as _code_book:
    code_dict = yaml.load(_code_book)


class StatusCode(object):
    def __init__(self, api_res_code: int = None):
        super(StatusCode, self).__init__()
        self._api_response_code = api_res_code

    def explain(self):
        if isinstance(self._api_response_code, int) and \
                self._api_response_code in code_dict['API_RESPONSE_CODE']['resultCode']:
            return code_dict['API_RESPONSE_CODE']['resultCode'][self._api_response_code]