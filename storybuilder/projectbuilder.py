"""Build module for story builder project."""

# official libraries
from dataclasses import dataclass

# my modules
from typing import Any
from storybuilder.datamanager import DataManager, ActionRecord
from storybuilder.projectfilemanager import ProjectFileManager
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

    # methods
    def build(self) -> bool:
        # create serialized order data
        data = self.fm.get_order_data()
        tmp = []
        for ch_record in data['book']:
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

        # build each container data
        story_records = []
        ## book
        story_records.append(BuildRecord('book', 'book', self.fm.get_data_from_book()))
        for record in tmp:
            story_records.append(
                    BuildRecord(
                        self.fm.get_category_from_ordername(record),
                        self.fm.get_basename_from_ordername(record),
                        self.fm.get_data_from_ordername(record)))
        # outline data output
        #result = self.on_outline_output(story_records)

        # plot data output
        #result = self.on_plot_output(story_records)

        # script data output
        result = self.on_script_output(story_records)
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
        logger.debug(">> BOOK: %s", book_titles)
        logger.debug(">> BOOK outline: %s", book_outlines)
        logger.debug(">> CHAPTER: %s", chapter_titles)
        logger.debug(">> CHAPTER outline: %s", chapter_outlines)
        logger.debug(">> EPISODE: %s", episode_titles)
        logger.debug(">> EPISODE outline: %s", episode_outlines)
        logger.debug(">> SCENE: %s", scene_titles)
        logger.debug(">> SCENE outline: %s", scene_outlines)

        return True

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
        #
        return True

    # private methods
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
