"""Build module for story builder project."""

# official libraries
from dataclasses import dataclass

# my modules
from typing import Any
from storybuilder.datamanager import DataManager, ActionRecord
from storybuilder.dbmanager import DBManager
from storybuilder.formatter import StoryFormatter
from storybuilder.projectfilemanager import ProjectFileManager
from storybuilder.util import assertion
from storybuilder.util.filepath import conv_only_basename
from storybuilder.util.log import logger


@dataclass
class BuildRecord(object):
    rcd_type: str
    name: str
    data: dict
    body: Any=None


class ProjectBuilder(object):

    """Build module for project."""

    def __init__(self, project_fil_manager: ProjectFileManager):
        self.fm = project_fil_manager
        self.dm = DataManager()
        self.dbm = DBManager()
        self.fomatter = StoryFormatter()

    # methods
    def build(self) -> bool:
        # create db
        self._create_tagname_db()

        # get order data
        order_data = assertion.is_dict(self.fm.get_order_data())

        # serialized
        serialized = assertion.is_list(self._get_serialized_order_fnames(order_data))

        # build each container data
        story_records = self._get_story_record_list(serialized)

        # outline data output
        result = self.on_outline_output(story_records)

        # plot data output
        #result = self.on_plot_output(story_records)

        # script data output
        #result = self.on_script_output(story_records)

        # novel data output
        #result = self.on_novel_output(story_records)
        return True

    # about outline
    def on_outline_output(self, story_records: list) -> bool:
        logger.debug("Build: outline: start")
        book_outlines = []
        book_titles = []
        chapter_outlines = []
        chapter_titles = []
        episode_outlines = []
        episode_titles = []
        scene_outlines = []
        scene_titles = []
        outputs = []

        # create data
        for rcd in story_records:
            if rcd.rcd_type == 'book':
                book_outlines.append(rcd.data['outline'])
                book_titles.append(rcd.data['title'])
            elif rcd.rcd_type == 'chapter':
                chapter_outlines.append(rcd.data['outline'])
                chapter_titles.append(rcd.data['title'])
            elif rcd.rcd_type == 'episode':
                episode_outlines.append(rcd.data['outline'])
                episode_titles.append(rcd.data['title'])
            elif rcd.rcd_type == 'scene':
                scene_outlines.append(rcd.data['outline'])
                scene_titles.append(rcd.data['title'])
            else:
                continue

        # get contents list
        contents = self._get_contents_list(story_records)

        # create output data
        outputs = self.fomatter.conv_contents_list_format(contents)

        outlines = self.fomatter.conv_outline_format('book', book_titles, book_outlines) \
                + [self.fomatter.get_break_line()] \
                + self.fomatter.conv_outline_format('chapter', chapter_titles, chapter_outlines) \
                + [self.fomatter.get_break_line()] \
                + self.fomatter.conv_outline_format('episode', episode_titles, episode_outlines) \
                + [self.fomatter.get_break_line()] \
                + self.fomatter.conv_outline_format('scene', scene_titles, scene_outlines)
        output_data = outputs + [self.fomatter.get_break_line()] + outlines

        # output data
        return self.fm.output_as_outline(output_data)

    # about plot
    def on_plot_output(self, story_records: list) -> bool:
        logger.debug("Build: plot: start")
        book_plots = []
        book_titles = []
        chapter_plots = []
        chapter_titles = []
        episode_plots = []
        episode_titles = []
        scene_plots = []
        scene_titles = []

        for rcd in story_records:
            if rcd.rcd_type == 'book':
                book_plots.append(rcd.data['plot'])
                book_titles.append(rcd.data['title'])
            elif rcd.rcd_type == 'chapter':
                chapter_plots.append(rcd.data['plot'])
                chapter_titles.append(rcd.data['title'])
            elif rcd.rcd_type == 'episode':
                episode_plots.append(rcd.data['plot'])
                episode_titles.append(rcd.data['title'])
            elif rcd.rcd_type == 'scene':
                scene_plots.append(rcd.data['plot'])
                scene_titles.append(rcd.data['title'])
            else:
                continue
        logger.debug(">> BOOK: %s", book_titles)
        logger.debug(">> BOOK plot: %s", book_plots)
        logger.debug(">> CHAPTER: %s", chapter_titles)
        logger.debug(">> CHAPTER plot: %s", chapter_plots)
        logger.debug(">> EPISODE: %s", episode_titles)
        logger.debug(">> EPISODE plot: %s", episode_plots)
        logger.debug(">> SCENE: %s", scene_titles)
        logger.debug(">> SCENE plot: %s", scene_plots)

        return True

    # about script
    def on_script_output(self, story_records: list) -> bool:
        logger.debug("Build: script: start")
        # get action records
        act_records = self._get_action_records(story_records)
        # get story codes
        codes = []
        for rcd in act_records:
            ret = self.dm.conv_storycode_from_action_record(rcd, True)
            if ret:
                codes.append(ret)
        # check
        for r in codes:
            logger.debug("#>code> %s", r)
        # check
        contents_list = self._get_contents_list(story_records)
        logger.debug("@> %s", contents_list)
        return True

    # about novel
    def on_novel_output(self, story_records: list) -> bool:
        logger.debug("Build: novel: start")
        # get action records
        act_records = self._get_action_records(story_records)
        # get story codes
        codes = []
        for rcd in act_records:
            ret = self.dm.conv_storycode_from_action_record(rcd)
            if ret:
                codes.append(ret)
        # check
        for r in codes:
            logger.debug("#_novel_ %s", r)
        contents_list = self._get_contents_list(story_records)
        return True

    # private methods
    def _get_contents_list(self, story_records: list) -> list:
        tmp = []
        ch_idx, ep_idx, sc_idx = 1, 1, 1

        for rcd in story_records:
            if rcd.rcd_type == 'book':
                # main title
                tmp.append(rcd.data['title'])
            elif rcd.rcd_type == 'chapter':
                # chapter title
                tmp.append(f"{ch_idx}. {rcd.data['title']}")
                ch_idx += 1
            elif rcd.rcd_type == 'episode':
                tmp.append(f"    {ep_idx}. {rcd.data['title']}")
                ep_idx += 1
            elif rcd.rcd_type == 'scene':
                tmp.append(f"        {sc_idx}. {rcd.data['title']}")
                sc_idx += 1
            else:
                continue
        return tmp

    def _create_tagname_db(self) -> bool:
        # get each list(filepaths)
        word_list = self.fm.get_word_list()
        item_list = self.fm.get_item_list()
        stage_list = self.fm.get_stage_list()
        person_list = self.fm.get_person_list()
        # word
        for fname in word_list:
            data = self.fm.get_data_from_word_file(fname)
            self.dbm.add_word_name(conv_only_basename(fname), data['name'])
        # item
        for fname in item_list:
            data = self.fm.get_data_from_item_file(fname)
            self.dbm.add_item_name(conv_only_basename(fname), data['name'])
        # stage
        for fname in stage_list:
            data = self.fm.get_data_from_stage_file(fname)
            self.dbm.add_stage_name(conv_only_basename(fname), data['name'])
        # person
        for fname in person_list:
            data = self.fm.get_data_from_person_file(fname)
            self.dbm.add_person_name(conv_only_basename(fname), data['name'], data['fullname'])
        self.dbm.sort_db()
        return True

    def _get_action_records(self, story_records: list) -> list:
        tmp = []

        for rcd in story_records:
            if rcd.rcd_type == 'book':
                tmp.append(ActionRecord(
                    "book-title", rcd.data['title'],
                    ))
            elif rcd.rcd_type == 'chapter':
                tmp.append(ActionRecord(
                    "chapter-title", rcd.data['title'],
                    ))
            elif rcd.rcd_type == 'episode':
                tmp.append(ActionRecord(
                    "episode-title", rcd.data['title'],
                    ))
            elif rcd.rcd_type == 'scene':
                tmp.append(ActionRecord(
                    "scene-title", rcd.data['title'],
                    ))
                tmp.append(ActionRecord(
                    "scene-camera", rcd.data['camera'],
                    ))
                tmp.append(ActionRecord(
                    "scene-stage", rcd.data['stage'],
                    ))
                tmp.append(ActionRecord(
                    "scene-year", rcd.data['year'],
                    ))
                tmp.append(ActionRecord(
                    "scene-date", rcd.data['date'],
                    ))
                tmp.append(ActionRecord(
                    "scene-time", rcd.data['time'],
                    ))
                sc_data = rcd.data['markdown']
                for line in sc_data:
                    ret = self.dm.conv_action_record(line)
                    if ret:
                        tmp.append(ret)
            else:
                continue
        # check
        for r in tmp:
            logger.debug("##> %s", r)
        return tmp

    def _get_serialized_order_fnames(self, order_data: dict) -> list:
        tmp = []
        for ch_record in order_data['book']:
            # chapter level
            for key in ch_record.keys():
                tmp.append(key)
            for ep_record in ch_record.values():
                # episode level
                for ep_data in ep_record:
                    for key in ep_data.keys():
                        tmp.append(key)
                    for sc_record in ep_data.values():
                        for sc_data in sc_record:
                            tmp.append(sc_data)
        return tmp

    def _get_story_record_list(self, serialized_order_names: list) -> list:
        tmp = []
        ## book
        tmp.append(BuildRecord('book', 'book', self.fm.get_data_from_book()))
        for record in serialized_order_names:
            tmp.append(
                    BuildRecord(
                        self.fm.get_category_from_ordername(record),
                        self.fm.get_basename_from_ordername(record),
                        self.fm.get_data_from_ordername(record)))
        return tmp
