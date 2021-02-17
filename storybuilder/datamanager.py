"""Data management utility module for YAML and Storybuilder data."""

# official libraries
import copy
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
        tmp = copy.deepcopy(orderdata)
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
            logger.error("Invalid order data!: %s", tmp)
            return orderdata
        return tmp

    def remove_episode_from_chapter_in_order(self, orderdata: dict, episodename) -> dict:
        tmp = copy.deepcopy(orderdata)
        # check exists
        if not 'book' in tmp.keys():
            logger.error("Invalid order data!: %s", tmp)
            return orderdata
        if not self._has_episode_in_book(tmp['book'], episodename):
            logger.error("Missing the episode removed target!: %s", episodename)
            return orderdata
        # remove process
        for ch_record in tmp['book']:
            for ch_data in ch_record.values():
                updated = []
                for ep_record in ch_data:
                    if not episodename in ep_record.keys():
                        updated.append(ep_record)
            for key in ch_record.keys():
                ch_record[key] = updated
        return tmp

    def remove_scene_from_episode_in_order(self, orderdata: dict, scenename: str) -> dict:
        tmp = copy.deepcopy(orderdata)
        print("##", orderdata)
        # check exists
        if not 'book' in tmp.keys():
            logger.error("Invalid order data!: %s", tmp)
            return orderdata
        if not self._has_scene_in_book(tmp['book'], scenename):
            logger.error("Missing the target scene!: %s", scenename)
            return orderdata
        # remove process
        for ch_record in tmp['book']:
            for ch_data in ch_record.values():
                for ep_record in ch_data:
                    for ep_data in ep_record.values():
                        updated = []
                        for sc_name in ep_data:
                            if sc_name != scenename:
                                updated.append(sc_name)
                    for key in ep_record.keys():
                        ep_record[key] = updated
        return tmp

    def set_chapter_to_book_in_order(self, orderdata: dict, chaptername: str) -> dict:
        tmp = copy.deepcopy(orderdata)
        if 'book' in tmp.keys():
            if not tmp['book']:
                tmp['book'] = []
            if not self._has_chapter(tmp['book'], chaptername):
                tmp['book'].append({chaptername:[]})
        else:
            logger.error("Invalid order data!: %s", tmp)
            return orderdata
        return tmp

    def set_episode_to_chapter_in_order(self, orderdata: dict, episodename: str,
            chaptername: str) -> dict:
        tmp = copy.deepcopy(orderdata)
        if not 'book' in tmp.keys():
            logger.error("Invalid order data!: %s", tmp)
            return orderdata
        if not self._has_chapter(tmp['book'], chaptername):
            logger.error("Missing target chapter name!: %s", chaptername)
            return orderdata
        ch_data = self._get_chapter(tmp['book'], chaptername)
        if not self._has_episode(ch_data, episodename):
            idx = self._get_chapter_index(tmp['book'], chaptername)
            tmp['book'][idx][chaptername].append({episodename:[]})
        return tmp

    def set_scene_to_episode_in_order(self, orderdata: dict, scenename: str,
            episodename: str) -> dict:
        tmp = copy.deepcopy(orderdata)
        if not 'book' in tmp.keys():
            logger.error("Invalid order data!: %s", tmp)
            return orderdata
        for ch_data in tmp['book']:
            for val in ch_data.values():
                for ep_data in val:
                    if episodename in ep_data.keys():
                        ep_data[episodename].append(scenename)
        return tmp

    # private methods
    def _get_chapter(self, bookdata: list, chaptername: str) -> list:
        for data in bookdata:
            if chaptername in data:
                return data
        return []

    def _get_chapter_index(self, bookdata: list, chaptername: str) -> int:
        idx = 0
        for data in bookdata:
            if chaptername in data:
                return idx
            idx += 1
        return 0

    def _get_episode(self, chapterdata: list, episodename: str) -> list:
        for data in chapterdata:
            if episodename in data:
                return data
        return []

    def _get_episode_index(self, chapterdata: list, episodename: str) -> int:
        idx = 0
        for data in chapterdata:
            if episodename in data:
                return idx
            idx += 1
        return 0

    def _has_chapter(self, bookdata: list, chaptername: str) -> bool:
        for data in bookdata:
            if chaptername in data:
                return True
        return False

    def _has_episode(self, chapterdata: list, episodename: str) -> bool:
        for data in chapterdata:
            if episodename in data:
                return True
        return False

    def _has_episode_in_book(self, bookdata: list, episodename: str) -> bool:
        for ch_data in bookdata:
            for val in ch_data.values():
                for ep_data in val:
                    if episodename in ep_data.keys():
                        return True
        return False

    def _has_scene(self, episodedata: list, scenename: str) -> bool:
        for data in episodedata:
            if scenename in data:
                return True
        return False

    def _has_scene_in_book(self, bookdata: list, scenename: str) -> bool:
        for ch_record in bookdata:
            for ch_data in ch_record.values():
                for ep_record in ch_data:
                    for ep_data in ep_record.values():
                        for scene_name in ep_data:
                            if scenename == scene_name:
                                return True
        return False
