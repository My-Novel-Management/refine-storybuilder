"""Data management utility module for YAML and Storybuilder data."""

# official libraries
import copy
import os
from dataclasses import dataclass, field
from typing import Any, Union

# my modules
from storybuilder.util.log import logger
from storybuilder.util.filepath import conv_only_basename


@dataclass
class ActionRecord(object):
    act_type: str
    subject: str
    action: str=""
    outline: str=""
    desc: str=""
    flags: list=field(default_factory=list)
    note: str=""


@dataclass
class StoryCode(object):
    head: str
    body: str
    foot: Any=None


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

    def conv_action_record(self, basedata: str) -> Union[ActionRecord, None]:
        _base = basedata.rstrip('\n\r')
        if _base in ('', '\n', '\n\r'):
            # empty line
            logger.debug("ACT: empty line")
            return None
        elif _base.startswith('# '):
            # comment
            logger.debug("ACT: comment: %s", _base)
            return ActionRecord("comment", _base)
        elif _base.startswith('## '):
            # title
            logger.debug("ACT: title: %s", _base)
            return ActionRecord("head-title", _base[3:])
        elif _base.startswith('['):
            # action
            logger.debug("ACT: action: %s", _base)
            text = ""
            comment = ""
            if '# ' in _base:
                # exists comment
                _, comment = _base.split('# ')
                _base = _
            a, b = _base[1:].split(']')
            if b:
                text = b
            subject, act, outline = a.split(':')
            return ActionRecord('action', subject, act, outline, text, [], comment)
        elif _base:
            # text
            logger.debug("ACT: text: %s", _base)
            return ActionRecord("text", _base)
        else:
            logger.debug("ACT: other: %s", _base)
            return None

    def conv_storycode_from_action_record(self, record: ActionRecord, is_script: bool=False) -> Union[StoryCode, None]:
        if 'book-title' == record.act_type:
            return StoryCode('book-title', record.subject)
        elif 'chapter-title' == record.act_type:
            return StoryCode('chapter-title', record.subject)
        elif 'episode-title' == record.act_type:
            return StoryCode('episode-title', record.subject)
        elif 'scene-title' == record.act_type:
            return StoryCode('scene-title', record.subject)
        elif 'head-title' == record.act_type:
            return StoryCode('head-title', record.subject)
        elif 'scene-camera' == record.act_type:
            return StoryCode('scene-camera', record.subject)
        elif 'scene-stage' == record.act_type:
            return StoryCode('scene-stage', record.subject)
        elif 'scene-year' == record.act_type:
            return StoryCode('scene-year', record.subject)
        elif 'scene-date' == record.act_type:
            return StoryCode('scene-date', record.subject)
        elif 'scene-time' == record.act_type:
            return StoryCode('scene-time', record.subject)
        elif 'action' == record.act_type:
            body = record.outline if is_script else record.desc
            if 'talk' == record.action:
                return StoryCode('dialogue', body, record.subject)
            elif 'think' == record.action:
                return StoryCode('monologue', body, record.subject)
            else:
                return StoryCode('description', body, record.subject)
        elif 'stage' == record.act_type:
            return StoryCode('stage', record.subject)
        else:
            return None

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
