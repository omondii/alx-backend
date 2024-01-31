#!/usr/bin/env python3
""" A FIFOCaching system """
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ A caching system implemented using FIFO """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key,item):
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key, value = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(key))