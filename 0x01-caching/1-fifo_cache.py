#!/usr/bin/env python3
"""
Module defining class BasicCache
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Class inheriting from BaseCahing
    """

    def __init__(self):
        """
        init method which is inherited from parent
        """
        super().__init__()
        self.fifo_array = []

    def put(self, key, item):
        """
        overriding put method from parent
        """
        if not key or not item:
            return

        if len(list(self.cache_data.keys())) < self.MAX_ITEMS:
            # self.fifo_array.append({ key: item })
            self.cache_data[key] = item
        elif len(list(self.cache_data.keys())) == self.MAX_ITEMS:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                discard_key = list(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(discard_key))
                self.cache_data.pop(discard_key)
                self.cache_data[key] = item
                assert len(list(self.cache_data.keys())) == self.MAX_ITEMS, "somethingwrong"

    def get(self, key):
        """
        overriding get method from parent
        """
        if not key or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
