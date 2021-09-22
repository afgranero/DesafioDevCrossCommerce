import unittest

from config import *
from log import Log
from extract import Extract


class ExtractTest(unittest.TestCase):
    def setUp(self):
        self.logger = Log.init_logger(LOG_ID, LOG_FILE_TEMPLATE)

    def test_real_extract(self):
        extract = Extract(self.logger, EXTRACT_ADDRESS)
        extract.run()
        self.assertEqual(extract.status, EXTRACT_STATUS_ENDED)
        self.assertTrue(len(extract.out_list) == 1000000)


if __name__ == '__main__':
    unittest.main(verbosity=2)
