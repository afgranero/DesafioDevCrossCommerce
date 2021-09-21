import unittest

from config import *
from log import Log
from transform import Transform


class TransformTest(unittest.TestCase):
    def setUp(self):
        self.logger = Log.init_logger(LOG_ID, LOG_FILE_TEMPLATE)

    def is_ordered(self, l):
        prev_e = None
        ordered = True
        for e in l:
            if prev_e is not None:
                if e < prev_e:
                    ordered = False
                    break

            prev_e = e

        return ordered

    def test_is_ordered(self):
        # YES! I am testing my own test auxiliary method here, get over this
        ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertTrue(self.is_ordered(ordered_list))

        unordered_list = [12, 18, 16, 1, 7, 13, 14, 10, 4, 9, 6, 2, 20, 17, 3, 15, 19, 11, 8, 5]
        self.assertFalse(self.is_ordered(unordered_list))

    def test_sort(self):
        unordered_list = [12, 18, 16, 1, 7, 13, 14, 10, 4, 9, 6, 2, 20, 17, 3, 15, 19, 11, 8, 5]
        transform = Transform(self.logger)

        ordered_list = transform.sort(unordered_list)
        assert(self.is_ordered(ordered_list))

    def test_run_sort(self):
        unordered_list = [12, 18, 16, 1, 7, 13, 14, 10, 4, 9, 6, 2, 20, 17, 3, 15, 19, 11, 8, 5]
        transform = Transform(self.logger)

        ordered_list = transform.run_sort(unordered_list)
        assert(self.is_ordered(ordered_list))

    def test_get_min_max(self):
        unordered_list = [12, 18, 16, 1, 7, 13, 14, 10, 4, 9, 6, 2, 20, 17, 3, 15, 19, 11, 8, 5]
        transform = Transform(self.logger)

        min, max = transform.get_min_max(unordered_list)
        assert(min == 1)
        assert(max == 20)


if __name__ == '__main__':
    unittest.main(verbosity=2)
