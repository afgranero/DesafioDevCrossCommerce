import math
import sys

from config import *
from log import Log

class Transform:
    def __init__(self, logger):
        self.logger = logger
        self.logger.info(MESSAGE_TRANSFORM_INIT)

    def sort(self, l):
        min, max = self.get_min_max(l)
        median = (min + max) / 2

       # create two lists one with the smaller elements and other with the bigger elements ...
        # list comprehensions create generator (as they are lazy evaluated)
        list_bigger =  [e for e in l if e >= median]
        list_smaller = [e for e in l if e < median]

        # sort the two lists recursevelly ...
        # ... lists with one element are already ordered ...
        # ... so only sorts lists with more than one element
        if len(list_bigger) != 1:
            list_bigger = self.sort(list_bigger)

        if len(list_smaller) != 1:
            list_smaller = self.sort(list_smaller)

        return list_smaller + list_bigger

    def get_min_max(self, list):
        # python already has max an min functions for lists but I choose...
        # ...to implement them in the spirit of clarifying the algorithm

        #initial values
        max = sys.float_info.min
        min = sys.float_info.max

        # find max and minimum in one pass
        for e in list:
            if e > max: max = e
            if e < min: min = e

        return min, max


if __name__ == '__main__':
    import random

    unsorted_list = list(range(1, 101))
    random.shuffle(unsorted_list)

    logger = Log.init_logger(LOG_ID, LOG_FILE_TEMPLATE)
    transform = Transform(logger)

    sorted_list = transform.sort(unsorted_list)

