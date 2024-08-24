#!/usr/bin/env python3
"""
Module defining class BasicCache
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Class inheriting from BaseCahing
    """

    def __init__(self):
        """
        init method which is inherited from parent
        """
        super().__init__()
        self.freq_dict = {}

    def put(self, key, item):
        """
        overriding put method from parent
        """
        if not key or not item:
            return

        if key in self.cache_data:
            del self.cache_data[key]
            self.cache_data[key] = item
        else:
            if len(list(self.cache_data.keys())) < self.MAX_ITEMS:
                self.cache_data[key] = item
                self.freq_dict[key] = 1
                for key_dict in self.freq_dict.keys():
                    if key_dict != key:
                        self.freq_dict[key_dict] += 1
            elif len(list(self.cache_data.keys())) == self.MAX_ITEMS:
                ordered_dict = sorted(list(self.freq_dict.items()), \
                                      key=lambda tup: tup[1], reverse=True)
                discard_key = ordered_dict[0][0]
                # print('-'* 50)
                print('DISCARD: {}'.format(discard_key))
                # print('self.freq_dict: {}'.format(ordered_dict))

                self.cache_data.pop(discard_key)
                self.freq_dict.pop(discard_key)

                self.cache_data[key] = item
                self.freq_dict[key] = 1

                for key_dict in self.freq_dict.keys():
                    if key_dict != key:
                        self.freq_dict[key_dict] += 1

                assert len(list(self.cache_data.keys())) \
                    == self.MAX_ITEMS, "somethingwrong"

    def get(self, key):
        """
        overriding get method from parent
        """
        if not key or key not in self.cache_data.keys():
            return None
        else:
            self.freq_dict[key] = 0
            return self.cache_data[key]

