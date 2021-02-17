"""File manager for a project."""

# official libraries
import glob
import os
import shutil
import subprocess

# my module
from storybuilder.util.log import logger
from storybuilder import BASE_ENCODING
from storybuilder import PROJECTFILE_NAME
from storybuilder import EDITOR
from storybuilder import CHAPTER_DIR, EPISODE_DIR, SCENE_DIR, NOTE_DIR
from storybuilder import PERSON_DIR, STAGE_DIR, ITEM_DIR, WORD_DIR
from storybuilder import PROJECTFILE_EXT, BOOKFILE_EXT, ORDERFILE_EXT
from storybuilder import PROJECTFILE_NAME, BOOKFILE_NAME, ORDERFILE_NAME
from storybuilder import CHAPTERFILE_EXT, EPISODEFILE_EXT, SCENEFILE_EXT, NOTEFILE_EXT
from storybuilder import PERSONFILE_EXT, STAGEFILE_EXT, ITEMFILE_EXT, WORDFILE_EXT
from storybuilder import TRASH_DIR
from storybuilder.datamanager import DataManager
from storybuilder.fileparser import FileParser
from storybuilder.util.filepath import add_extention, conv_filenames_from_fullpaths, has_extention


class ProjectFileManager(object):

    """File manager for a project."""

    def __init__(self, project_base_path: str):
        """Initialize project file manager.

        Arguments:
            project_base_path: the base path for this project.
        """
        self.fp = FileParser()
        self.dm = DataManager()
        # path setting
        self.base_path = project_base_path
        self.chapters = os.path.join(self.base_path, CHAPTER_DIR)
        self.episodes = os.path.join(self.base_path, EPISODE_DIR)
        self.scenes = os.path.join(self.base_path, SCENE_DIR)
        self.notes = os.path.join(self.base_path, NOTE_DIR)
        self.persons = os.path.join(self.base_path, PERSON_DIR)
        self.stages = os.path.join(self.base_path, STAGE_DIR)
        self.items = os.path.join(self.base_path, ITEM_DIR)
        self.words = os.path.join(self.base_path, WORD_DIR)
        self.trash = os.path.join(self.base_path, TRASH_DIR)
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

    def check_and_create_trash_dir(self) -> bool:
        if not os.path.exists(self.trash):
            os.makedirs(self.trash)
        return True

    def clear_trashbox(self) -> bool:
        for file in glob.glob(os.path.join(self.trash, '*')):
            os.remove(file)
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

    def delete_chapter_file(self, fname: str) -> bool:
        return self._delete_file(self.validate_chapter_file_path(fname))

    def delete_episode_file(self, fname: str) -> bool:
        return self._delete_file(self.validate_episode_file_path(fname))

    def delete_scene_file(self, fname: str) -> bool:
        return self._delete_file(self.validate_scene_file_path(fname))

    def delete_note_file(self, fname: str) -> bool:
        return self._delete_file(self.validate_note_file_path(fname))

    def delete_person_file(self, fname: str) -> bool:
        return self._delete_file(self.validate_person_file_path(fname))

    def delete_stage_file(self, fname: str) -> bool:
        return self._delete_file(self.validate_stage_file_path(fname))

    def delete_item_file(self, fname: str) -> bool:
        return self._delete_file(self.validate_item_file_path(fname))

    def delete_word_file(self, fname: str) -> bool:
        return self._delete_file(self.validate_word_file_path(fname))

    def edit_book_file(self) -> bool:
        return self._edit_file(BOOKFILE_NAME)

    def edit_order_file(self) -> bool:
        return self._edit_file(ORDERFILE_NAME)

    def edit_chapter_file(self, fname: str) -> bool:
        return self._edit_file(self.validate_chapter_file_path(fname))

    def edit_episode_file(self, fname: str) -> bool:
        return self._edit_file(self.validate_episode_file_path(fname))

    def edit_scene_file(self, fname: str) -> bool:
        return self._edit_file(self.validate_scene_file_path(fname))

    def edit_note_file(self, fname: str) -> bool:
        return self._edit_file(self.validate_note_file_path(fname))

    def edit_person_file(self, fname: str) -> bool:
        return self._edit_file(self.validate_person_file_path(fname))

    def edit_stage_file(self, fname: str) -> bool:
        return self._edit_file(self.validate_stage_file_path(fname))

    def edit_item_file(self, fname: str) -> bool:
        return self._edit_file(self.validate_item_file_path(fname))

    def edit_word_file(self, fname: str) -> bool:
        return self._edit_file(self.validate_word_file_path(fname))

    def get_ordered_chapters(self) -> list:
        return []

    def get_ordered_episodes(self) -> list:
        return []

    def get_ordered_scenes(self) -> list:
        return []

    def get_order_data(self) -> dict:
        return self.fp.get_from_yaml(ORDERFILE_NAME)

    def get_order_data_by_yaml(self) -> str:
        return self.fp.conv_dumpdata_as_yaml(self.get_order_data())

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

    def overwrite_order_file(self, data: str) -> bool:
        logger.debug("TEST: %s", data)
        with open(ORDERFILE_NAME, 'w', encoding=BASE_ENCODING) as file:
            file.write(data)
        return True

    def push_chapter_to_book(self, fname: str) -> bool:
        # TODO: check file exists
        order_data = self.fp.get_from_yaml(ORDERFILE_NAME)
        updated = self.dm.set_chapter_to_book_in_order(order_data, self.dm.conv_chapterdata_name(fname))
        return self.overwrite_order_file(self.fp.conv_dumpdata_as_yaml(updated))

    def push_episode_to_chapter(self, fname: str, target: str) -> bool:
        # TODO: check file exists
        order_data = self.fp.get_from_yaml(ORDERFILE_NAME)
        updated = self.dm.set_episode_to_chapter_in_order(order_data,
                self.dm.conv_episodedata_name(fname),
                self.dm.conv_chapterdata_name(target))
        return self.overwrite_order_file(self.fp.conv_dumpdata_as_yaml(updated))

    def push_scene_to_episode(self, fname: str, target: str) -> bool:
        # TODO: check file exists
        order_data = self.get_order_data()
        updated = self.dm.set_scene_to_episode_in_order(order_data,
                self.dm.conv_scenedata_name(fname),
                self.dm.conv_episodedata_name(target))
        return self.overwrite_order_file(self.fp.conv_dumpdata_as_yaml(updated))

    def reject_chapter_from_book(self, fname: str) -> bool:
        # TODO: check file exists
        order_data = self.fp.get_from_yaml(ORDERFILE_NAME)
        updated = self.dm.remove_chapter_from_book_in_order(order_data, self.dm.conv_chapterdata_name(fname))
        return self.overwrite_order_file(self.fp.conv_dumpdata_as_yaml(updated))

    def reject_episode_from_chapter(self, fname: str) -> bool:
        # TODO: check file exists
        order_data = self.fp.get_from_yaml(ORDERFILE_NAME)
        updated = self.dm.remove_episode_from_chapter_in_order(order_data, self.dm.conv_episodedata_name(fname))
        return self.overwrite_order_file(self.fp.conv_dumpdata_as_yaml(updated))

    def reject_scene_from_episode(self, fname: str) -> bool:
        # TODO: check file exists
        order_data = self.get_order_data()
        updated = self.dm.remove_scene_from_episode_in_order(order_data, self.dm.conv_scenedata_name(fname))
        return self.overwrite_order_file(self.fp.conv_dumpdata_as_yaml(updated))

    def rename_chapter_file(self, fname: str, newname: str) -> bool:
        vpath = self.validate_chapter_file_path(fname)
        vnew = self.validate_chapter_file_path(newname)
        if self._is_exists_path(vpath) and self._is_safepath(vnew):
            os.rename(vpath, vnew)
            return True
        return False

    def rename_episode_file(self, fname: str, newname: str) -> bool:
        vpath = self.validate_episode_file_path(fname)
        vnew = self.validate_episode_file_path(newname)
        if self._is_exists_path(vpath) and self._is_safepath(vnew):
            os.rename(vpath, vnew)
            return True
        return False

    def rename_scene_file(self, fname: str, newname: str) -> bool:
        vpath = self.validate_scene_file_path(fname)
        vnew = self.validate_scene_file_path(newname)
        if self._is_exists_path(vpath) and self._is_safepath(vnew):
            os.rename(vpath, vnew)
            return True
        return False

    def rename_note_file(self, fname: str, newname: str) -> bool:
        vpath = self.validate_note_file_path(fname)
        vnew = self.validate_note_file_path(newname)
        if self._is_exists_path(vpath) and self._is_safepath(vnew):
            os.rename(vpath, vnew)
            return True
        return False

    def rename_person_file(self, fname: str, newname: str) -> bool:
        vpath = self.validate_person_file_path(fname)
        vnew = self.validate_person_file_path(newname)
        if self._is_exists_path(vpath) and self._is_safepath(vnew):
            os.rename(vpath, vnew)
            return True
        return False

    def rename_stage_file(self, fname: str, newname: str) -> bool:
        vpath = self.validate_stage_file_path(fname)
        vnew = self.validate_stage_file_path(newname)
        if self._is_exists_path(vpath) and self._is_safepath(vnew):
            os.rename(vpath, vnew)
            return True
        return False

    def rename_item_file(self, fname: str, newname: str) -> bool:
        vpath = self.validate_item_file_path(fname)
        vnew = self.validate_item_file_path(newname)
        if self._is_exists_path(vpath) and self._is_safepath(vnew):
            os.rename(vpath, vnew)
            return True
        return False

    def rename_word_file(self, fname: str, newname: str) -> bool:
        vpath = self.validate_word_file_path(fname)
        vnew = self.validate_word_file_path(newname)
        if self._is_exists_path(vpath) and self._is_safepath(vnew):
            os.rename(vpath, vnew)
            return True
        return False

    def validate_chapter_file_path(self, fname: str) -> str:
        _fname = fname if has_extention(fname, CHAPTERFILE_EXT) else add_extention(fname, CHAPTERFILE_EXT)
        return os.path.join(self.chapters, os.path.basename(_fname))

    def validate_episode_file_path(self, fname: str) -> str:
        _fname = fname if has_extention(fname, EPISODEFILE_EXT) else add_extention(fname, EPISODEFILE_EXT)
        return os.path.join(self.episodes, os.path.basename(_fname))

    def validate_scene_file_path(self, fname: str) -> str:
        _fname = fname if has_extention(fname, SCENEFILE_EXT) else add_extention(fname, SCENEFILE_EXT)
        return os.path.join(self.scenes, os.path.basename(_fname))

    def validate_note_file_path(self, fname: str) -> str:
        _fname = fname if has_extention(fname, NOTEFILE_EXT) else add_extention(fname, NOTEFILE_EXT)
        return os.path.join(self.notes, os.path.basename(_fname))

    def validate_person_file_path(self, fname: str) -> str:
        _fname = fname if has_extention(fname, PERSONFILE_EXT) else add_extention(PERSONFILE_EXT)
        return os.path.join(self.persons, os.path.basename(_fname))

    def validate_stage_file_path(self, fname: str) -> str:
        _fname = fname if has_extention(fname, STAGEFILE_EXT) else add_extention(STAGEFILE_EXT)
        return os.path.join(self.stages, os.path.basename(_fname))

    def validate_item_file_path(self, fname: str) -> str:
        _fname = fname if has_extention(fname, ITEMFILE_EXT) else add_extention(ITEMFILE_EXT)
        return os.path.join(self.items, os.path.basename(_fname))

    def validate_word_file_path(self, fname: str) -> str:
        _fname = fname if has_extention(fname, WORDFILE_EXT) else add_extention(WORDFILE_EXT)
        return os.path.join(self.words, os.path.basename(_fname))

    # private methods
    def _delete_file(self, fname: str) -> bool:
        shutil.move(fname, self.trash)
        return True

    def _edit_file(self, fname: str) -> bool:
        proc = subprocess.run([EDITOR, fname])
        if proc.returncode != 0:
            logger.error("Subprocess Error!: %s", proc.returncode)
            return False
        return True

    def _get_current_file_list(self, dirname: str, ext: str) -> list:
        return glob.glob(os.path.join(dirname, f"*.{ext}"))

    def _filename_only_basename(self, filename: str) -> str:
        basename, ext = os.path.splitext(filename)
        return basename

    def _filename_validated_with_extention(self, filename: str, default_ext: str) -> str:
        basename, ext = os.path.splitext(filename)
        if ext:
            return filename
        else:
            return f"{basename}.{default_ext}"

    def _is_exists_path(self, path: str) -> bool:
        return os.path.exists(path)

    def _is_safepath(self, filename: str) -> bool:
        return not os.path.exists(filename)

