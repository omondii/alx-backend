#!/usr/bin/env python3
""" A FIFOCaching system """
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ A caching system implemented using FIFO """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item
        value for the key key"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key, _ = self.cache_data.popitem(last=False)
                print(f'DISCARD: {key}')

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is None:
            return None
        else:
            return self.cache_data.get(key, None)
