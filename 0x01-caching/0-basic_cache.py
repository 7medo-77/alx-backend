#!/usr/bin/env python3
"""
module defining class BasicCache
"""


BaseCaching = __import__("base_cahing").BaseCaching


class BasicCache(BaseCaching):
    """
    Class inheriting from BaseCahing
    """


    def __init__(self):
        """
        init method which is inherited from parent
        """
        super().__init__()

    def put(self, key, item):
        """
        overriding put method from parent
        """
        if not key or not item:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        overriding get method from parent
        """
        if not key or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
