#!/usr/bin/env python3
""" A FIFOCaching system """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ A caching system implemented using FIFO """
    def __init__(self):
        """ Initialize the class """
        super().__init__()

    def put(self, key: str, item: str) -> None:
        """ Assign to the dictionary self.cache_data the item
        value for the key key"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                delKey = list(self.cache_data.keys())[-1]
                print(f'DISCARD: {delKey}')
                del self.cache_data[delKey]
            self.cache_data[key] = item

    def get(self, key: str) -> str:
        """ Return the value in self.cache_data linked to key """
        if key is None:
            return None
        else:
            return self.cache_data.get(key, None)
