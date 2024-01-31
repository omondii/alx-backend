#!/usr/bin/env python3
""" A FIFOCaching system """
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ A caching system implemented using FIFO """
    def __init__(self):
        """ Initialize the class """
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item
        value for the key key"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = list(self.cache_data.keys())[-1]
                print('DISCARD: {}'.format(discarded_key))
                del self.cache_data[discarded_key]

            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        return self.cache_data[key] if key in self.cache_data else None
