#!/usr/bin/env python3
""" MRU caching system """
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ Implement a LFU caching system
    Removes the last used item
    """
    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: str, item: str) -> None:
        """ assign to the dictionary self.cache_data the item
        item for the key key """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # Find the key with the least frequency.
                    delKey = min(self.cache_data.keys(), key=lambda k:
                                 self.cache_data[k][0])
                    print(f'DISCARD: {delKey}')
                    self.cache_data.pop(delKey)

        self.cache_data[key] = item

    def get(self, key: str) -> str:
        """ Return the item in self.cache_data linked to key """
        if key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key, None)
