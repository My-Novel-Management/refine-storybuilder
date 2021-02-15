"""File manager for a project."""

# official libraries
import glob
import os

# my module
from storybuilder.util.log import logger
from storybuilder import BASE_ENCODING
from storybuilder import PROJECTFILE_NAME
from storybuilder import CHAPTER_DIR, EPISODE_DIR, SCENE_DIR, NOTE_DIR
from storybuilder import PERSON_DIR, STAGE_DIR, ITEM_DIR, WORD_DIR
from storybuilder import PROJECTFILE_EXT, BOOKFILE_EXT, ORDERFILE_EXT
from storybuilder import PROJECTFILE_NAME, BOOKFILE_NAME, ORDERFILE_NAME
from storybuilder import CHAPTERFILE_EXT, EPISODEFILE_EXT, SCENEFILE_EXT, NOTEFILE_EXT
from storybuilder import PERSONFILE_EXT, STAGEFILE_EXT, ITEMFILE_EXT, WORDFILE_EXT
from storybuilder.util.filepath import conv_filenames_from_fullpaths


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
        if not self._is_safepath(path):
            logger.error("Already exists the project file!")
            return False

        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_book_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.base_path,
                self._filename_validated_with_extention(os.path.basename(filename), BOOKFILE_EXT))
        if not self._is_safepath(path):
            logger.error("Already exists the book file!")
            return False

        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_order_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.base_path,
                self._filename_validated_with_extention(os.path.basename(filename), ORDERFILE_EXT))
        if not self._is_safepath(path):
            logger.error("Already exists the order file!")
            return False

        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_chapter_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.chapters,
                self._filename_validated_with_extention(os.path.basename(filename), CHAPTERFILE_EXT))
        if not self._is_safepath(path):
            logger.error("Already exists the chapter file!: %s", path)
            return False

        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_episode_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.episodes,
                self._filename_validated_with_extention(os.path.basename(filename), EPISODEFILE_EXT))
        if not self._is_safepath(path):
            logger.error("Already exists the episode file!: %s", path)
            return False

        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_scene_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.scenes,
                self._filename_validated_with_extention(os.path.basename(filename), SCENEFILE_EXT))
        if not self._is_safepath(path):
            logger.error("Already exists the sccene file!: %s", path)
            return False

        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_note_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.notes,
                self._filename_validated_with_extention(os.path.basename(filename), NOTEFILE_EXT))
        if not self._is_safepath(path):
            logger.error("Already exists the note file!: %s", path)
            return False

        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_person_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.persons,
                self._filename_validated_with_extention(os.path.basename(filename), PERSONFILE_EXT))
        if not self._is_safepath(path):
            logger.error("Already exists the person file!: %s", path)
            return False

        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_stage_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.stages,
                self._filename_validated_with_extention(os.path.basename(filename), STAGEFILE_EXT))
        if not self._is_safepath(path):
            logger.error("Already exists the stage file!: %s", path)
            return False

        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_item_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.items,
                self._filename_validated_with_extention(os.path.basename(filename), ITEMFILE_EXT))
        if not self._is_safepath(path):
            logger.error("Already exists the item file!: %s", path)
            return False

        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_word_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.words,
                self._filename_validated_with_extention(os.path.basename(filename), WORDFILE_EXT))
        if not self._is_safepath(path):
            logger.error("Already exists the word file!: %s", path)
            return False

        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def get_chapter_list(self) -> list:
        return self._get_current_file_list(self.chapters, CHAPTERFILE_EXT)

    def get_episode_list(self) -> list:
        return self._get_current_file_list(self.episodes, EPISODEFILE_EXT)

    def get_scene_list(self) -> list:
        return self._get_current_file_list(self.scenes, SCENEFILE_EXT)

    def get_note_list(self) -> list:
        return self._get_current_file_list(self.notes, NOTEFILE_EXT)

    def get_person_list(self) -> list:
        return self._get_current_file_list(self.persons, PERSONFILE_EXT)

    def get_stage_list(self) -> list:
        return self._get_current_file_list(self.stages, STAGEFILE_EXT)

    def get_item_list(self) -> list:
        return self._get_current_file_list(self.items, ITEMFILE_EXT)

    def get_word_list(self) -> list:
        return self._get_current_file_list(self.words, WORDFILE_EXT)

    def get_chapter_name_list(self) -> list:
        return conv_filenames_from_fullpaths(self.get_chapter_list())

    def get_episode_name_list(self) -> list:
        return conv_filenames_from_fullpaths(self.get_episode_list())

    def get_scene_name_list(self) -> list:
        return conv_filenames_from_fullpaths(self.get_scene_list())

    def get_note_name_list(self) -> list:
        return conv_filenames_from_fullpaths(self.get_note_list())

    def get_person_name_list(self) -> list:
        return conv_filenames_from_fullpaths(self.get_person_list())

    def get_stage_name_list(self) -> list:
        return conv_filenames_from_fullpaths(self.get_stage_list())

    def get_item_name_list(self) -> list:
        return conv_filenames_from_fullpaths(self.get_item_list())

    def get_word_name_list(self) -> list:
        return conv_filenames_from_fullpaths(self.get_word_list())

    def is_exists_project_file(self) -> bool:
        return self._is_exists_path(PROJECTFILE_NAME)

    def is_exists_book_file(self) -> bool:
        return self._is_exists_path(BOOKFILE_NAME)

    def is_exists_order_file(self) -> bool:
        return self._is_exists_path(ORDERFILE_NAME)

    def is_exists_chapter_file(self, path: str) -> bool:
        return self._is_exists_path(path) or self._is_exists_path(os.path.join(self.chapters, path)) \
                or self._is_exists_path(os.path.join(self.chapters, f"{path}.{CHAPTERFILE_EXT}"))

    def is_exists_episode_file(self, path: str) -> bool:
        return self._is_exists_path(path) or self._is_exists_path(os.path.join(self.episodes, path)) \
                or self._is_exists_path(os.path.join(self.episodes, f"{path}.{EPISODEFILE_EXT}"))

    def is_exists_scene_file(self, path: str) -> bool:
        return self._is_exists_path(path) or self._is_exists_path(os.path.join(self.scenes, path)) \
                or self._is_exists_path(os.path.join(self.scenes, f"{path}.{SCENEFILE_EXT}"))

    def is_exists_note_file(self, path: str) -> bool:
        return self._is_exists_path(path) or self._is_exists_path(os.path.join(self.notes, path)) \
                or self._is_exists_path(os.path.join(self.notes, f"{path}.{NOTEFILE_EXT}"))

    def is_exists_person_file(self, path: str) -> bool:
        return self._is_exists_path(path) or self._is_exists_path(os.path.join(self.persons, path)) \
                or self._is_exists_path(os.path.join(self.persons, f"{path}.{PERSONFILE_EXT}"))

    def is_exists_stage_file(self, path: str) -> bool:
        return self._is_exists_path(path) or self._is_exists_path(os.path.join(self.stages, path)) \
                or self._is_exists_path(os.path.join(self.stages, f"{path}.{STAGEFILE_EXT}"))

    def is_exists_item_file(self, path: str) -> bool:
        return self._is_exists_path(path) or self._is_exists_path(os.path.join(self.items, path)) \
                or self._is_exists_path(os.path.join(self.items, f"{path}.{ITEMFILE_EXT}"))

    def is_exists_word_file(self, path: str) -> bool:
        return self._is_exists_path(path) or self._is_exists_path(os.path.join(self.words, path)) \
                or self._is_exists_path(os.path.join(self.words, f"{path}.{WORDFILE_EXT}"))

    # private methods
    def _is_exists_path(self, path: str) -> bool:
        return os.path.exists(path)

    def _is_safepath(self, filename: str) -> bool:
        return not os.path.exists(filename)

    def _get_current_file_list(self, dirname: str, ext: str) -> list:
        return glob.glob(os.path.join(dirname, f"*.{ext}"))

    def _filename_validated_with_extention(self, filename: str, default_ext: str) -> str:
        basename, ext = os.path.splitext(filename)
        if ext:
            return filename
        else:
            return f"{basename}.{default_ext}"

