#!/usr/bin/env python3
""" LRU caching system """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Implement a LRU caching system
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
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lruKey = next(iter(self.cache_data))
                print(f'DISCARD: {lruKey}')
                del self.cache_data[lruKey]
            
            self.cache_data[key] = item

    def get(self, key: str) -> str:
        """ Return the item in self.cache_data linked to key """
        if key is None:
            return None
        else:
            return self.cache_data.get(key, None)