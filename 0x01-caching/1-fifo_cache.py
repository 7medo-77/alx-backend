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
            pass

        if len(list(self.cache_data.keys())) < 4:
            # self.fifo_array.append({ key: item })
            self.cache_data[key] = item
        # elif len(self.fifo_array) == 4 and { key: item } not in self.cache_data.items():
        elif len(list(self.cache_data.keys())) == 4:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                print('DISCARD: {}'.format(list(self.cache_data.keys())[0]))
                self.cache_data.pop(list(self.cache_data.keys())[0])
                self.cache_data[key] = item
                assert len(list(self.cache_data.keys())) == 4, "somethingwrong"

    def get(self, key):
        """
        overriding get method from parent
        """
        if not key or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
