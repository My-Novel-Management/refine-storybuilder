"""Data management utility module for YAML and Storybuilder data."""

# official libraries
import os

# my modules
from storybuilder.util.log import logger
from storybuilder.util.filepath import conv_only_basename


class DataManager(object):

    """Data manager for storybuilder's data."""

    def __init__(self):
        pass

    # methods
    def conv_chapterdata_name(self, basename: str) -> str:
        return f"chapter/{conv_only_basename(basename)}"

    def conv_episodedata_name(self, basename: str) -> str:
        return f"episode/{conv_only_basename(basename)}"

    def conv_scenedata_name(self, basename: str) -> str:
        return f"scene/{conv_only_basename(basename)}"

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
            if not self._has_chapter(tmp['book'], chaptername):
                tmp['book'].append({chaptername:[]})
        else:
            logger.error("Invalid order data! %s", tmp)
            return orderdata
        return tmp

    # private methods
    def _has_chapter(self, bookdata: list, chaptername: str) -> bool:
        for data in bookdata:
            if chaptername in data:
                return True
        return False
