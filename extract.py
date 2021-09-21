import time

import requests
import asyncio
import aiohttp

from config import *
from log import Log


class Extract:

    def __init__(self, logger, url):
        self.logger = logger
        self.url = url
        self.out_list = []
        self.loop = asyncio.get_event_loop()
        self.logger.info(MESSAGE_REQUEST_INIT)

    async def get_pages(self, page_start, page_stop):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for page in range(page_start, page_stop):
                tasks.append(self.get_page(session=session, page=page))

            in_list = await asyncio.gather(*tasks, return_exceptions=False)
            return in_list

    async def get_page(self, session, page):
        retry_count = 0
        while True:
            params = f'?{EXTRACT_PARAM}={page}'
            async with session.get(self.url + params) as response:
                if response.status == requests.status_codes.codes.OK:
                    self.logger.info(MESSAGE_REQUEST_SUCCESS.format(page))
                    return await response.json()
                else:
                    self.logger.error(MESSAGE_REQUEST_ERROR.format(retry_count, page, response.status, response.reason))

                    # the first retry is immediate
                    if retry_count > 1:
                        time.sleep(RETRY_INTERVAL)

                    retry_count += 1
                    if retry_count >= RETRY_MAX_COUNT:
                        self.logger.error(MESSAGE_REQUEST_MAX_RETRIES.format(retry_count))
                        # TODO permanent failure raise exception

    def run(self):
        page_start = 1
        page_stop = TASK_COUNT
        retry_count = 0
        while True:
            self.logger.info(MESSAGE_REQUESTS_PARALLEL_ROUND.format(TASK_COUNT, page_start, page_stop))

            try:
                result = asyncio.run(self.get_pages(page_start, page_stop))
                retry_count = 0
            except Exception as e:
                self.logger.error(MESSAGE_REQUESTS_PARALLEL_ERROR.format(str(e), page_start, page_stop, retry_count))
                retry_count += 1
                if retry_count >= RETRY_MAX_COUNT:
                    self.logger.error(MESSAGE_REQUEST_MAX_RETRIES.format(retry_count))
                    break

                self.logger.info(MESSAGAGE_SLEEPING.format(RETRY_LONG_INTERVAL))
                time.sleep(RETRY_LONG_INTERVAL)
                continue

            result_lists = [e['numbers'] for e in result]
            self.out_list.extend(sum(result_lists, []))
            if [] in result_lists:
                break

            page_start = page_stop
            page_stop = page_start + TASK_COUNT - 1

        self.logger.info(MESSAGE_SUCCESS.format(len(self.out_list)))
        return self.out_list


if __name__ == '__main__':
    logger = Log.init_logger(LOG_ID, LOG_FILE_TEMPLATE)
    extract = Extract(logger, EXTRACT_ADDRESS)
    extract.run()
