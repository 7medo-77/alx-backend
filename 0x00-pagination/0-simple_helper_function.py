#!/usr/bin/env python3
"""
Module which defines a function that returns
a tuple of start and end indexes
"""


def index_range(page, page_size):
    """
    function returning a range of indexes
    """
    startIndex = page_size * (page - 1)
    endIndex = page_size * page + page_size
    return tuple((startIndex, endIndex))
