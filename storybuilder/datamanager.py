"""Data management utility module for YAML and Storybuilder data."""

# official libraries

# my modules
from storybuilder.util.log import logger


class DataManager(object):

    """Data manager for storybuilder's data."""

    def __init__(self):
        pass

    # methods
    def remove_chapter_from_book_in_order(self, orderdata: dict, chaptername: str) -> dict:
        tmp = orderdata.copy()
        res = []
        if 'book' in tmp.keys():
            if not tmp['book']:
                tmp['book'] = []
                return tmp
            bookdata = tmp['book']
            for data in bookdata:
                if not chaptername in data:
                    res.append(data)
            tmp['book'] = res
        else:
            logger.error("Invalid order data! %s", tmp)
            return orderdata
        return tmp

    def set_chapter_to_book_in_order(self, orderdata: dict, chaptername: str) -> dict:
        tmp = orderdata.copy()
        if 'book' in tmp.keys():
            if not tmp['book']:
                tmp['book'] = []
            tmp['book'].append({chaptername:[]})
        else:
            logger.error("Invalid order data! %s", tmp)
            return orderdata
        return tmp
