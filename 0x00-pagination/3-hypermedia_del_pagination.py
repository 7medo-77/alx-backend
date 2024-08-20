#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns object with data, resistant to deletion
        """

        assert 0 <= index <= len(self.indexed_dataset())
        assert isinstance(page_size, int) and page_size > 0

        start_index = index if index else 0
        end_index = index + page_size
        data_indexed = self.indexed_dataset() if not\
            self.__indexed_dataset else self.__indexed_dataset
        data_list = []

        # print(start_index, end_index)
        for index_num in range(start_index, end_index):
            if data_indexed.get(index_num):
                data_list.append(data_indexed[index_num])
                # print(index_num)
            else:
                index_num += 1
                end_index += 1

        response_dict = {
            'index': index,
            'data': data_list,
            'page_size': page_size,
            'next_index': end_index,
        }

        return response_dict

        # if index is None:
        #     index = 0
        #
        # # validate the index
        # assert isinstance(index, int)
        # assert 0 <= index < len(self.indexed_dataset())
        # assert isinstance(page_size, int) and page_size > 0
        #
        # data = []  # collect all indexed data
        # next_index = index + page_size
        #
        # for value in range(index, next_index):
        #     if self.indexed_dataset().get(value):
        #         data.append(self.indexed_dataset()[value])
        #     else:
        #         value += 1
        #         next_index += 1
        #
        # return {
        #     'index': index,
        #     'data': data,
        #     'page_size': page_size,
        #     'next_index': next_index
        # }
