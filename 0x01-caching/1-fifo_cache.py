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

        if len(self.fifo_array) < 4:
            self.fifo_array.append(key)
            self.cache_data[key] = item
        elif len(self.fifo_array) == 4 and key not in self.fifo_array:
            key_to_delete = self.fifo_array[0]
            print('DISCARD: {}'.format(key_to_delete))
            self.cache_data.pop(key_to_delete)
            self.fifo_array.pop(0)

            self.fifo_array.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        overriding get method from parent
        """
        if not key or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
