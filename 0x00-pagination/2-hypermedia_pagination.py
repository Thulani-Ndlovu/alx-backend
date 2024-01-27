#!/usr/bin/env python3
'''Hypermedia pagination'''
from typing import List, Tuple, Dict
import math
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
        return a tuple of size two containing a start index
        and an end index corresponding to the range of
        indexes to return in a list for those particular
        pagination parameters.
    '''
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)


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
        '''return page of dataset'''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        startIndex, endIndex = index_range(page, page_size)
        dataSet = self.dataset()
        if startIndex > len(dataSet):
            return []
        return dataSet[startIndex:endIndex]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''
            returns a dictionary containing the following key-value pairs:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        '''
        pageData = self.get_page(page, page_size)
        startIndex, endIndex = index_range(page, page_size)
        pageTotal = math.ceil(len(self.__dataset) / page_size)
        pageInfo = {
            'page_size': len(pageData),
            'page': page,
            'data': pageData,
            'next_page': page + 1 if endIndex < len(self.__dataset) else None,
            'prev_page': page - 1 if startIndex > 0 else None,
            'total_pages': pageTotal,
        }
        return pageInfo
