#!/usr/bin/env python3
""" LRU caching system """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Implement the LRU caching system
    Removes the last used item
    """
    def __init__(self):
        """ Initialize the class """
        super().__init__()

    def put(self, key, value):
        """ assign to the dictionary self.cache_data the item
        value for the key key """
        if key is not None and value is not None:
            self.cache_data[key] = value
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.popitem(last = False)

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key not in self.cache_data:
            return -1
        else:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]