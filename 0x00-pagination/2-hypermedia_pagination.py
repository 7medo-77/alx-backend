#!/usr/bin/env python3
"""
Main file
"""


from typing import List, Dict
import csv
import math
index_range = __import__('0-simple_helper_function').index_range


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
                if index >= indexTuple[0] and index < indexTuple[1]:
                    resultList.append(line)

        return resultList

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary object that is HATEOAS compliant
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        length = len(self.dataset())
        total_pages = math.ceil(length / page_size)
        data = self.get_page(page, page_size)

        response_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if (page + 1) <= total_pages else None,
            'prev_page': page - 1 if page - 1 > 0 else None,
            'total_pages': total_pages,
        }

        return response_dict
