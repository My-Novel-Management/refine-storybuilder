"""Create templates."""

# official libraries
import os

# my module
from storybuilder.settings import COPYRIGHT, VERSION
from storybuilder import BASE_ENCODING
from storybuilder.util.log import logger


PROJECT_TEMP_FILE = 'project_tmp.yml'
"""str: file name of project template."""

BOOK_TEMP_FILE = 'book_tmp.yml'
"""str: file name of book template."""

ORDER_TEMP_FILE = 'order_tmp.yml'
"""str: file name of order template."""

CHAPTER_TEMP_FILE = 'chapter_tmp.yml'
"""str: file name of chapter template."""

EPISODE_TEMP_FILE = 'episode_tmp.yml'
"""str: file name of episode template."""

SCENE_TEMP_FILE = 'scene_tmp.md'
"""str: file name of scene template."""

NOTE_TEMP_FILE = 'note_tmp.md'
"""str: file name of note template."""

PERSON_TEMP_FILE = 'person_tmp.yml'
"""str: file name of person template."""

STAGE_TEMP_FILE = 'stage_tmp.yml'
"""str: file name of stage template."""

ITEM_TEMP_FILE = 'item_tmp.yml'
"""str: file name of item template."""

WORD_TEMP_FILE = 'word_tmp.yml'
"""str: file name of word template."""

PLOT_TEMP_FILE = 'plot_tmp.yml'
"""str: file name of plot template."""


class TemplateCreator(object):

    """Create for project templates."""

    def __init__(self):
        data_path = os.path.join(os.path.dirname(__file__), 'data')
        self.project_tmp = os.path.join(data_path, PROJECT_TEMP_FILE)
        self.book_tmp = os.path.join(data_path, BOOK_TEMP_FILE)
        self.order_tmp = os.path.join(data_path, ORDER_TEMP_FILE)
        self.chapter_tmp = os.path.join(data_path, CHAPTER_TEMP_FILE)
        self.episode_tmp = os.path.join(data_path, EPISODE_TEMP_FILE)
        self.scene_tmp = os.path.join(data_path, SCENE_TEMP_FILE)
        self.note_tmp = os.path.join(data_path, NOTE_TEMP_FILE)
        self.person_tmp = os.path.join(data_path, PERSON_TEMP_FILE)
        self.stage_tmp = os.path.join(data_path, STAGE_TEMP_FILE)
        self.item_tmp = os.path.join(data_path, ITEM_TEMP_FILE)
        self.word_tmp = os.path.join(data_path, WORD_TEMP_FILE)
        self.plot_tmp = os.path.join(data_path, PLOT_TEMP_FILE)
        logger.debug("Initialized: Template Creator")

    # methods
    def get_project_template(self) -> str:
        tmp = ""
        with open(self.project_tmp, 'r', encoding=BASE_ENCODING) as file:
            tmp = file.read()
        return tmp.replace('{VERSION}', VERSION).replace('{COPYRIGHT}', COPYRIGHT)

    def get_book_template(self) -> str:
        tmp = ""
        plot = ""
        with open(self.book_tmp, 'r', encoding=BASE_ENCODING) as file:
            tmp = file.read()
        with open(self.plot_tmp, 'r', encoding=BASE_ENCODING) as pfile:
            plot = pfile.read()
        return tmp.replace('{PLOT}', plot.rstrip('\n\r'))

    def get_order_template(self) -> str:
        tmp = ""
        with open(self.order_tmp, 'r', encoding=BASE_ENCODING) as file:
            tmp = file.read()
        return tmp

    def get_chapter_template(self) -> str:
        tmp = ""
        plot = ""
        with open(self.chapter_tmp, 'r', encoding=BASE_ENCODING) as file:
            tmp = file.read()
        with open(self.plot_tmp, 'r', encoding=BASE_ENCODING) as pfile:
            plot = pfile.read()
        return tmp.replace('{PLOT}', plot.rstrip('\n\r'))

    def get_episode_template(self) -> str:
        tmp = ""
        plot = ""
        with open(self.episode_tmp, 'r', encoding=BASE_ENCODING) as file:
            tmp = file.read()
        with open(self.plot_tmp, 'r', encoding=BASE_ENCODING) as pfile:
            plot = pfile.read()
        return tmp.replace('{PLOT}', plot.rstrip('\n\r'))

    def get_scene_template(self) -> str:
        tmp = ""
        plot = ""
        with open(self.scene_tmp, 'r', encoding=BASE_ENCODING) as file:
            tmp = file.read()
        with open(self.plot_tmp, 'r', encoding=BASE_ENCODING) as pfile:
            plot = pfile.read()
        return tmp.replace('{PLOT}', plot.rstrip('\n\r'))

    def get_note_template(self) -> str:
        tmp = ""
        with open(self.note_tmp, 'r', encoding=BASE_ENCODING) as file:
            tmp = file.read()
        return tmp

    def get_person_template(self) -> str:
        tmp = ""
        with open(self.person_tmp, 'r', encoding=BASE_ENCODING) as file:
            tmp = file.read()
        return tmp

    def get_stage_template(self) -> str:
        tmp = ""
        with open(self.stage_tmp, 'r', encoding=BASE_ENCODING) as file:
            tmp = file.read()
        return tmp

    def get_item_template(self) -> str:
        tmp = ""
        with open(self.item_tmp, 'r', encoding=BASE_ENCODING) as file:
            tmp = file.read()
        return tmp

    def get_word_template(self) -> str:
        tmp = ""
        with open(self.word_tmp, 'r', encoding=BASE_ENCODING) as file:
            tmp = file.read()
        return tmp

