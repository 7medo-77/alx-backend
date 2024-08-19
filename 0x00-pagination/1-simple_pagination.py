#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Gets a list of all lines in an index
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        resultList = []
        indexTuple = index_range(page, page_size)

        with open(self.DATA_FILE) as file:
            readerObject = csv.reader(file)
            readerObject.__next__()
            for index, line in enumerate(readerObject):
                if index >= int(indexTuple[0]) and index < int( indexTuple[1] ):
                    resultList.append(line)

        return resultList
