import unittest
import requests

from config import *
from log import Log
from load import app, numbers


class LoadTest(unittest.TestCase):
    def setUp(self):
        self.logger = Log.init_logger(LOG_ID, LOG_FILE_TEMPLATE)
        self.sorted_list = list(range(1, 2 * LOAD_PAGE_SIZE + 1))

        self.app = app
        self.app.config['logger'] = self.logger
        self.app.config['sorted_list'] = self.sorted_list

    def get_min_max_index(self, page):
        min = (page - 1) * LOAD_PAGE_SIZE
        max = min + LOAD_PAGE_SIZE
        return min, max

    def test_real_load_page(self):
        # page 1
        page = 1
        min, max = self.get_min_max_index(page)

        with app.app_context():
            response = numbers(page)

        self.assertTrue(response.status_code == requests.status_codes.codes.OK)
        result = response.json

        keys = result.keys()
        self.assertTrue(len(keys) == 1)
        self.assertTrue('numbers' in keys)
        self.assertTrue(result['numbers'] == self.sorted_list[min:max])

        # page 2
        page = 2
        min, max = self.get_min_max_index(page)

        with app.app_context():
            response = numbers(page)

        self.assertTrue(response.status_code == requests.status_codes.codes.OK)

        result = response.json
        keys = result.keys()
        self.assertTrue(len(keys) == 1)
        self.assertTrue('numbers' in keys)
        self.assertTrue(result['numbers'] == self.sorted_list[min:max])

        # page 3
        page = 3

        with app.app_context():
            response = numbers(page)

        self.assertTrue(response.status_code == requests.status_codes.codes.OK)

        result = response.json
        keys = result.keys()
        self.assertTrue(len(keys) == 1)
        self.assertTrue('numbers' in keys)
        self.assertTrue(len(result['numbers']) == 0)

        # page invalid
        page = 'aaa'

        with app.app_context():
            response = numbers(page)

        self.assertTrue(response.status_code == requests.status_codes.codes.OK)

        result = response.json
        keys = result.keys()
        self.assertTrue(len(keys) == 1)
        self.assertTrue('error' in keys)
        self.assertTrue(result['error'] == MESSAGE_LOAD_REQUEST_ERROR.format(page))


if __name__ == '__main__':
    unittest.main(verbosity=2)