"""File manager for a project."""

# official libraries
import os

# my module
from storybuilder.util.log import logger
from storybuilder import BASE_ENCODING
from storybuilder import PROJECTFILE_NAME
from storybuilder import CHAPTER_DIR, EPISODE_DIR, SCENE_DIR, NOTE_DIR
from storybuilder import PERSON_DIR, STAGE_DIR, ITEM_DIR, WORD_DIR


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
    def create_project_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.base_path, os.path.basename(filename))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_book_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.base_path, os.path.basename(filename))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_chapter_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.chapters, os.path.basename(filename))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_episode_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.episodes, os.path.basename(filename))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_scene_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.scenes, os.path.basename(filename))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_note_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.notes, os.path.basename(filename))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_person_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.persons, os.path.basename(filename))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_stage_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.stages, os.path.basename(filename))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_item_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.items, os.path.basename(filename))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

    def create_word_file(self, filename: str, default_txt: str) -> bool:
        path = os.path.join(self.words, os.path.basename(filename))
        with open(path, 'w', encoding=BASE_ENCODING) as file:
            for line in default_txt:
                file.write(line)
        return True

