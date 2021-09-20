import time

import requests

from config import *
from log import Log


class Extract:

    def __init__(self, url):
        self.logger = Log.init_logger(LOG_ID, LOG_FILE_TEMPLATE)
        self.url = url
        self.logger.info(MESSAGE_REQUEST_INIT)

    def get_list(self):
        page = 1
        out_list = []
        retry_count = 0

        while True:
            response = requests.get(self.url, data = {EXTRACT_PARAM: f'{page}'})
            if  response.status_code == requests.status_codes.codes.OK:
                self.logger.info(MESSAGE_REQUEST_SUCCESS.format(page))
                in_list = response.json()
                if len(in_list) == 0:
                    self.logger.info(MESSAGE_REQUEST_LAST_PAGE.format(page))
                    break

                out_list.extend(in_list)
                retry_count = 0
                page += 1
            else:
                self.logger.error(MESSAGE_REQUEST_ERROR.format(retry_count, page, response.status_code, response.reason))
                time.sleep(RETRY_INTERVAL)
                retry_count += 1

                if retry_count >= RETRY_MAX_COUNT:
                    self.logger.error(MESSAGE_REQUEST_MAX_RETRIES.format(retry_count))

        return out_list


if __name__ == '__main__':
    extract = Extract(EXTRACT_ADDRESS)
    extract.get_list()