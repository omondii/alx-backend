#!/usr/bin/env python3
import csv
import math
from typing import List
""" 1-simple_pagination.py """


def index_range(page: int, page_size: int) -> tuple:
    """ Returns a tuple of size two containing a start index and an end index """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


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
            """ takes two integer arguments page and page_size
            and return the appropriate page of the dataset 
            """
            assert isinstance(page, int) and page > 0, "Type Error"
            assert isinstance(page_size, int) and page_size > 0, "Type Error"
            with open(self.DATA_FILE) as f:
                 reader = csv.reader(f)
                 data = list(reader)

            start, end = index_range(page, page_size)
            return data[start:end] if start < len(data) else []