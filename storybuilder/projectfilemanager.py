"""File manager for a project."""

# official libraries
import os

# my module
from storybuilder.util.log import logger
from storybuilder import BASE_ENCODING
from storybuilder import PROJECTFILE_NAME
from storybuilder import CHAPTER_DIR, EPISODE_DIR, SCENE_DIR, NOTE_DIR
from storybuilder import PERSON_DIR, STAGE_DIR, ITEM_DIR, WORD_DIR
from storybuilder import PROJECTFILE_EXT, BOOKFILE_EXT, ORDERFILE_EXT
from storybuilder import CHAPTERFILE_EXT, EPISODEFILE_EXT, SCENEFILE_EXT, NOTEFILE_EXT
from storybuilder import PERSONFILE_EXT, STAGEFILE_EXT, ITEMFILE_EXT, WORDFILE_EXT


class ProjectFileManager(object):

    """File manager for a project."""

    def __init__(self, project_base_path: str):
        """Initialize project file manager.

        Arguments:
            project_base_path: the base path for this project.
        """
        self.base_path = project_base_path
        self.chapters = os.path.join(self.base_path, CHAPTER_DIR)
        self.episodes = os.path.join(self.base_path, EPISODE_DIR)
        self.scenes = os.path.join(self.base_path, SCENE_DIR)
        self.notes = os.path.join(self.base_path, NOTE_DIR)
        self.persons = os.path.join(self.base_path, PERSON_DIR)
        self.stages = os.path.join(self.base_path, STAGE_DIR)
        self.items = os.path.join(self.base_path, ITEM_DIR)
        self.words = os.path.join(self.base_path, WORD_DIR)
        logger.debug("Initialized: ProjectFileManager")

    # methods
    def check_and_create_chapter_dir(self) -> bool:
        if not os.path.exists(self.chapters):
            os.makedirs(self.chapters)
        return True

    def check_and_create_episode_dir(self) -> bool:
        if not os.path.exists(self.episodes):
            os.makedirs(self.episodes)
        return True

    def check_and_create_scene_dir(self) -> bool:
        if not os.path.exists(self.scenes):
            os.makedirs(self.scenes)
        return True

    def check_and_create_note_dir(self) -> bool:
        if not os.path.exists(self.notes):
            os.makedirs(self.notes)
        return True

    def check_and_create_person_dir(self) -> bool:
        if not os.path.exists(self.persons):
            os.makedirs(self.persons)
        return True

    def check_and_create_stage_dir(self) -> bool:
        if not os.path.exists(self.stages):
            os.makedirs(self.stages)
        return True

    def check_and_create_item_dir(self) -> bool:
        if not os.path.exists(self.items):
            os.makedirs(self.items)
        return True

    def check_and_create_word_dir(self) -> bool:
        if not os.path.exists(self.words):
            os.makedirs(self.words)
        return True

    def create_project_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.base_path,
                self._filename_validated_with_extention(os.path.basename(filename), PROJECTFILE_EXT))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_book_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.base_path,
                self._filename_validated_with_extention(os.path.basename(filename), BOOKFILE_EXT))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_order_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.base_path,
                self._filename_validated_with_extention(os.path.basename(filename), ORDERFILE_EXT))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_chapter_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.chapters,
                self._filename_validated_with_extention(os.path.basename(filename), CHAPTERFILE_EXT))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_episode_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.episodes,
                self._filename_validated_with_extention(os.path.basename(filename), EPISODEFILE_EXT))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_scene_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.scenes,
                self._filename_validated_with_extention(os.path.basename(filename), SCENEFILE_EXT))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_note_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.notes,
                self._filename_validated_with_extention(os.path.basename(filename), NOTEFILE_EXT))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_person_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.persons,
                self._filename_validated_with_extention(os.path.basename(filename), PERSONFILE_EXT))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_stage_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.stages,
                self._filename_validated_with_extention(os.path.basename(filename), STAGEFILE_EXT))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_item_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.items,
                self._filename_validated_with_extention(os.path.basename(filename), ITEMFILE_EXT))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_word_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.words,
                self._filename_validated_with_extention(os.path.basename(filename), WORDFILE_EXT))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    # private methods
    def _filename_validated_with_extention(self, filename: str, default_ext: str) -> str:
        basename, ext = os.path.splitext(filename)
        if ext:
            return filename
        else:
            return f"{basename}.{default_ext}"

