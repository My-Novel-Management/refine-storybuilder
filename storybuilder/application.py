"""Main application for storybuilder."""

# official libraries
import os

# my modules
from storybuilder.commandlineparser import CommandlineParser
from storybuilder.projectfilemanager import ProjectFileManager
from storybuilder.templatecreator import TemplateCreator
from storybuilder.util.log import logger
from storybuilder import PROJECTFILE_NAME, BOOKFILE_NAME, ORDERFILE_NAME


# Alias
StatusCode = int


class Application(object):

    """Application for storybuilder."""

    def __init__(self):
        # base setting
        self.fm = ProjectFileManager(os.getcwd())
        self.tmp_creator = TemplateCreator()
        logger.debug("Initialized: Application")

    # main method
    def run(self) -> StatusCode:
        logger.debug("Start Running: Application")

        exit_code = 0
        """int: if 0 is successfull, other is failure"""

        result = True
        """bool: if True is successfull result to proceed, False is any failure in process."""

        has_project = True
        """bool: if True exist a project file, False is nothing file."""

        # get command
        cmdline_parser = CommandlineParser()
        cmdargs = cmdline_parser.get_commandline_arguments()

        # check project
        if not self._has_project_file():
            has_project = False

        # if command init
        if cmdargs.cmd == 'init':
            result = self.on_init_project(has_project)
            if not result:
                logger.error("Error and Exit! [in initialize phase]")
                exit_code = 1
                return exit_code
            logger.debug("Exit code: %s", exit_code)
            return exit_code

        # switch by command
        if cmdargs.cmd in ('b', 'build'):
            # Build
            pass
        elif cmdargs.cmd in ('a', 'add'):
            # Add
            if cmdargs.arg0 in ('c', 'chapter'):
                result = self.on_add_chapter(cmdargs.arg1)
            elif cmdargs.arg0 in ('e', 'episode'):
                result = self.on_add_episode(cmdargs.arg1)
            elif cmdargs.arg0 in ('s', 'scene'):
                result = self.on_add_scene(cmdargs.arg1)
            elif cmdargs.arg0 in ('n', 'note'):
                result = self.on_add_note(cmdargs.arg1)
            elif cmdargs.arg0 in ('p', 'person'):
                result = self.on_add_person(cmdargs.arg1)
            elif cmdargs.arg0 in ('t', 'stage'):
                result = self.on_add_stage(cmdargs.arg1)
            elif cmdargs.arg0 in ('i', 'item'):
                result = self.on_add_item(cmdargs.arg1)
            elif cmdargs.arg0 in ('w', 'word'):
                result = self.on_add_word(cmdargs.arg1)
            else:
                logger.error("Unknown Add command argument!: %s", cmdargs.arg0)
                result = False
        elif cmdargs.cmd in ('e', 'edit'):
            # Edit
            if cmdargs.arg0 in ('b', 'book'):
                result = self.on_edit_book()
            elif cmdargs.arg0 in ('o', 'order'):
                result = self.on_edit_order()
            elif cmdargs.arg0 in ('c', 'chapter'):
                result = self.on_edit_chapter(cmdargs.arg1)
            elif cmdargs.arg0 in ('e', 'episode'):
                result = self.on_edit_episode(cmdargs.arg1)
            elif cmdargs.arg0 in ('s', 'scene'):
                result = self.on_edit_scene(cmdargs.arg1)
            elif cmdargs.arg0 in ('n', 'note'):
                result = self.on_edit_note(cmdargs.arg1)
            elif cmdargs.arg0 in ('p', 'person'):
                result = self.on_edit_person(cmdargs.arg1)
            elif cmdargs.arg0 in ('t', 'stage'):
                result = self.on_edit_stage(cmdargs.arg1)
            elif cmdargs.arg0 in ('i', 'item'):
                result = self.on_edit_item(cmdargs.arg1)
            elif cmdargs.arg0 in ('w', 'word'):
                result = self.on_edit_word(cmdargs.arg1)
            else:
                logger.error("Unknown Add command argument!: %s", cmdargs.arg0)
                result = False
        elif cmdargs.cmd in ('d', 'delete'):
            # Delete
            if cmdargs.arg0 in ('c', 'chapter'):
                result = self.on_delete_chapter(cmdargs.arg1)
            elif cmdargs.arg0 in ('e', 'episode'):
                result = self.on_delete_episode(cmdargs.arg1)
            elif cmdargs.arg0 in ('s', 'scene'):
                result = self.on_delete_scene(cmdargs.arg1)
            elif cmdargs.arg0 in ('n', 'note'):
                result = self.on_delete_note(cmdargs.arg1)
            elif cmdargs.arg0 in ('p', 'person'):
                result = self.on_delete_person(cmdargs.arg1)
            elif cmdargs.arg0 in ('t', 'stage'):
                result = self.on_delete_stage(cmdargs.arg1)
            elif cmdargs.arg0 in ('i', 'item'):
                result = self.on_delete_item(cmdargs.arg1)
            elif cmdargs.arg0 in ('w', 'word'):
                result = self.on_delete_word(cmdargs.arg1)
            else:
                logger.error("Unknown Add command argument!: %s", cmdargs.arg0)
                result = False
        elif cmdargs.cmd in ('r', 'rename'):
            # Rename
            if cmdargs.arg0 in ('c', 'chapter'):
                result = self.on_rename_chapter(cmdargs.arg1)
            elif cmdargs.arg0 in ('e', 'episode'):
                result = self.on_rename_episode(cmdargs.arg1)
            elif cmdargs.arg0 in ('s', 'scene'):
                result = self.on_rename_scene(cmdargs.arg1)
            elif cmdargs.arg0 in ('n', 'note'):
                result = self.on_rename_note(cmdargs.arg1)
            elif cmdargs.arg0 in ('p', 'person'):
                result = self.on_rename_person(cmdargs.arg1)
            elif cmdargs.arg0 in ('t', 'stage'):
                result = self.on_rename_stage(cmdargs.arg1)
            elif cmdargs.arg0 in ('i', 'item'):
                result = self.on_rename_item(cmdargs.arg1)
            elif cmdargs.arg0 in ('w', 'word'):
                result = self.on_rename_word(cmdargs.arg1)
            else:
                logger.error("Unknown Add command argument!: %s", cmdargs.arg0)
                result = False
        elif cmdargs.cmd in ('l', 'list'):
            # List
            if cmdargs.arg0 in ('c', 'chapter'):
                result = self.on_list_chapter(cmdargs.arg1)
            elif cmdargs.arg0 in ('e', 'episode'):
                result = self.on_list_episode(cmdargs.arg1)
            elif cmdargs.arg0 in ('s', 'scene'):
                result = self.on_list_scene(cmdargs.arg1)
            elif cmdargs.arg0 in ('n', 'note'):
                result = self.on_list_note(cmdargs.arg1)
            elif cmdargs.arg0 in ('p', 'person'):
                result = self.on_list_person(cmdargs.arg1)
            elif cmdargs.arg0 in ('t', 'stage'):
                result = self.on_list_stage(cmdargs.arg1)
            elif cmdargs.arg0 in ('i', 'item'):
                result = self.on_list_item(cmdargs.arg1)
            elif cmdargs.arg0 in ('w', 'word'):
                result = self.on_list_word(cmdargs.arg1)
            else:
                logger.error("Unknown Add command argument!: %s", cmdargs.arg0)
                result = False
        else:
            logger.error("Unimplement command!: %s", cmdargs.cmd)

        # check result
        if not result:
            exit_code = 1

        return exit_code

    # methods (command)
    def on_add_chapter(self, fname: str) -> bool:
        logger.debug("Command: Add Chapter: start")
        _fname = fname if fname else input("Enter a new chapter file name: ")
        res = self.fm.create_chapter_file(_fname, self.tmp_creator.get_chapter_template())
        if not res:
            logger.error("Failure: create a new chapter! %s", _fname)
            return False
        return self.on_edit_chapter(_fname)

    def on_add_episode(self, fname: str) -> bool:
        logger.debug("Command: Add Episode: start")
        _fname = fname if fname else input("Enter a new episode file name: ")
        res = self.fm.create_episode_file(_fname, self.tmp_creator.get_episode_template())
        if not res:
            logger.error("Failure: create a new episode! %s", _fname)
            return False
        return self.on_edit_episode(_fname)

    def on_add_scene(self, fname: str) -> bool:
        logger.debug("Command: Add Scene: start")
        _fname = fname if fname else input("Enter a new scene file name: ")
        res = self.fm.create_scene_file(_fname, self.tmp_creator.get_scene_template())
        if not res:
            logger.error("Failure: create a new scene! %s", _fname)
            return False
        return self.on_edit_scene(_fname)

    def on_add_note(self, fname: str) -> bool:
        logger.debug("Command: Add Note: start")
        _fname = fname if fname else input("Enter a new note file name: ")
        res = self.fm.create_note_file(_fname, self.tmp_creator.get_note_template())
        if not res:
            logger.error("Failure: create a new note! %s", _fname)
            return False
        return self.on_edit_note(_fname)

    def on_add_person(self, fname: str) -> bool:
        logger.debug("Command: Add Person: start")
        _fname = fname if fname else input("Enter a new person file name: ")
        res = self.fm.create_person_file(_fname, self.tmp_creator.get_person_template())
        if not res:
            logger.error("Failure: create a new person! %s", _fname)
            return False
        return self.on_edit_person(_fname)

    def on_add_stage(self, fname: str) -> bool:
        logger.debug("Command: Add Stage: start")
        _fname = fname if fname else input("Enter a new stage file name: ")
        res =  self.fm.create_stage_file(_fname, self.tmp_creator.get_stage_template())
        if not res:
            logger.error("Failure: create a new stage! %s", _fname)
            return False
        return self.on_edit_stage(_fname)

    def on_add_item(self, fname: str) -> bool:
        logger.debug("Command: Add Item: start")
        _fname = fname if fname else input("Enter a new item file name: ")
        res = self.fm.create_item_file(_fname, self.tmp_creator.get_item_template())
        if not res:
            logger.error("Failure: create a new item! %s", _fname)
            return False
        return self.on_edit_item(_fname)

    def on_add_word(self, fname: str) -> bool:
        logger.debug("Command: Add Word: start")
        _fname = fname if fname else input("Enter a new word file name: ")
        res = self.fm.create_word_file(_fname, self.tmp_creator.get_word_template())
        if not res:
            logger.error("Failure: create a new word! %s", _fname)
            return False
        return self.on_edit_word(_fname)

    def on_delete_chapter(self, fname: str) -> bool:
        logger.debug("Command: Delete Chapter: start")
        return True

    def on_delete_episode(self, fname: str) -> bool:
        logger.debug("Command: Delete Episode: start")
        return True

    def on_delete_scene(self, fname: str) -> bool:
        logger.debug("Command: Delete Scene: start")
        return True

    def on_delete_note(self, fname: str) -> bool:
        logger.debug("Command: Delete Note: start")
        return True

    def on_delete_person(self, fname: str) -> bool:
        logger.debug("Command: Delete Person: start")
        return True

    def on_delete_stage(self, fname: str) -> bool:
        logger.debug("Command: Delete Stage: start")
        return True

    def on_delete_item(self, fname: str) -> bool:
        logger.debug("Command: Delete Item: start")
        return True

    def on_delete_word(self, fname: str) -> bool:
        logger.debug("Command: Delete Word: start")
        return True

    def on_edit_book(self) -> bool:
        logger.debug("Command: Edit Book: start")
        return self.fm.edit_book_file()

    def on_edit_order(self) -> bool:
        logger.debug("Command: Edit Book: start")
        return self.fm.edit_order_file()

    def on_edit_chapter(self, fname: str) -> bool:
        logger.debug("Command: Edit Chapter: start")
        return self.fm.edit_chapter_file(fname)

    def on_edit_episode(self, fname: str) -> bool:
        logger.debug("Command: Edit Episode: start")
        return self.fm.edit_episode_file(fname)

    def on_edit_scene(self, fname: str) -> bool:
        logger.debug("Command: Edit Scene: start")
        return self.fm.edit_scene_file(fname)

    def on_edit_note(self, fname: str) -> bool:
        logger.debug("Command: Edit Note: start")
        return self.fm.edit_note_file(fname)

    def on_edit_person(self, fname: str) -> bool:
        logger.debug("Command: Edit Person: start")
        return self.fm.edit_person_file(fname)

    def on_edit_stage(self, fname: str) -> bool:
        logger.debug("Command: Edit Stage: start")
        return self.fm.edit_stage_file(fname)

    def on_edit_item(self, fname: str) -> bool:
        logger.debug("Command: Edit Item: start")
        return self.fm.edit_item_file(fname)

    def on_edit_word(self, fname: str) -> bool:
        logger.debug("Command: Edit Word: start")
        return self.fm.edit_word_file(fname)

    def on_init_project(self, has_project: bool) -> bool:
        logger.debug("Command: Init project: start")

        if not has_project:
            # create project file
            if not self.create_project_file():
                logger.error("Error in create project file!")
                return False

        if not self.create_project_templates():
            logger.error("Error in create project templates!")
            return False

        return True

    def on_list_chapter(self, fname: str) -> bool:
        logger.debug("Command: List Chapter: start")
        print(self._serialized_namelist_of(self.fm.get_chapter_name_list(), False))
        return True

    def on_list_episode(self, fname: str) -> bool:
        logger.debug("Command: List Episode: start")
        print(self._serialized_namelist_of(self.fm.get_episode_name_list(), False))
        return True

    def on_list_scene(self, fname: str) -> bool:
        logger.debug("Command: List Scene: start")
        print(self._serialized_namelist_of(self.fm.get_scene_name_list(), False))
        return True

    def on_list_note(self, fname: str) -> bool:
        logger.debug("Command: List Note: start")
        print(self._serialized_namelist_of(self.fm.get_note_name_list(), False))
        return True

    def on_list_person(self, fname: str) -> bool:
        logger.debug("Command: List Person: start")
        print(self._serialized_namelist_of(self.fm.get_person_name_list(), False))
        return True

    def on_list_stage(self, fname: str) -> bool:
        logger.debug("Command: List Stage: start")
        print(self._serialized_namelist_of(self.fm.get_stage_name_list(), False))
        return True

    def on_list_item(self, fname: str) -> bool:
        logger.debug("Command: List Item: start")
        print(self._serialized_namelist_of(self.fm.get_item_name_list(), False))
        return True

    def on_list_word(self, fname: str) -> bool:
        logger.debug("Command: List Word: start")
        print(self._serialized_namelist_of(self.fm.get_word_name_list(), False))
        return True

    def on_rename_chapter(self, fname: str) -> bool:
        logger.debug("Command: Rename Chapter: start")
        _fname = fname if fname else self._input_with_namelist("Enter a target chapter file: ", self.fm.get_chapter_name_list())
        _new = input("Enter a new chapter file name for changing: ")
        return self.fm.rename_chapter_file(_fname, _new)

    def on_rename_episode(self, fname: str) -> bool:
        logger.debug("Command: Rename Episode: start")
        _fname = fname if fname else self._input_with_namelist("Enter a target episode file: ", self.fm.get_episode_name_list())
        _new = input("Enter a new episode file name for changing: ")
        return self.fm.rename_episode_file(_fname, _new)

    def on_rename_scene(self, fname: str) -> bool:
        logger.debug("Command: Rename Scene: start")
        _fname = fname if fname else self._input_with_namelist("Enter a target scene file: ", self.fm.get_scene_name_list())
        _new = input("Enter a new scene file name for changing: ")
        return self.fm.rename_scene_file(_fname, _new)

    def on_rename_note(self, fname: str) -> bool:
        logger.debug("Command: Rename Note: start")
        _fname = fname if fname else self._input_with_namelist("Enter a target note file: ", self.fm.get_note_name_list())
        _new = input("Enter a new note file name for changing: ")
        return self.fm.rename_note_file(_fname, _new)

    def on_rename_person(self, fname: str) -> bool:
        logger.debug("Command: Rename Person: start")
        _fname = fname if fname else self._input_with_namelist("Enter a target person file: ", self.fm.get_person_name_list())
        _new = input("Enter a new person file name for changing: ")
        return self.fm.rename_person_file(_fname, _new)

    def on_rename_stage(self, fname: str) -> bool:
        logger.debug("Command: Rename Stage: start")
        _fname = fname if fname else self._input_with_namelist("Enter a target stage file: ", self.fm.get_stage_name_list())
        _new = input("Enter a new stage file name for changing: ")
        return self.fm.rename_stage_file(_fname, _new)

    def on_rename_item(self, fname: str) -> bool:
        logger.debug("Command: Rename Item: start")
        _fname = fname if fname else self._input_with_namelist("Enter a target item file: ", self.fm.get_item_name_list())
        _new = input("Enter a new item file name for changing: ")
        return self.fm.rename_item_file(_fname, _new)

    def on_rename_word(self, fname: str) -> bool:
        logger.debug("Command: Rename Word: start")
        _fname = fname if fname else self._input_with_namelist("Enter a target word file: ", self.fm.get_word_name_list())
        _new = input("Enter a new word file name for changing: ")
        return self.fm.rename_word_file(_fname, _new)

    # methods
    def create_project_file(self) -> bool:
        return self.fm.create_project_file(PROJECTFILE_NAME,
                self.tmp_creator.get_project_template())

    def create_project_templates(self) -> bool:
        # create dirs
        if not self.fm.check_and_create_chapter_dir():
            logger.error("Failure check or create chapter directory!")
            return False

        if not self.fm.check_and_create_episode_dir():
            logger.error("Failure check or create episode directory!")
            return False

        if not self.fm.check_and_create_scene_dir():
            logger.error("Failure check or create scene directory!")
            return False

        if not self.fm.check_and_create_note_dir():
            logger.error("Failure check or create note directory!")
            return False

        if not self.fm.check_and_create_person_dir():
            logger.error("Failure check or create person directory!")
            return False

        if not self.fm.check_and_create_stage_dir():
            logger.error("Failure check or create stage directory!")
            return False

        if not self.fm.check_and_create_item_dir():
            logger.error("Failure check or create item directory!")
            return False

        if not self.fm.check_and_create_word_dir():
            logger.error("Failure check or create word directory!")
            return False

        logger.debug("Created: template directories")

        # create temp files
        if not self.fm.is_exists_book_file():
            if not self.fm.create_book_file(BOOKFILE_NAME, self.tmp_creator.get_book_template()):
                logger.error("Failure create a default BOOK file!")
                return False

        if not self.fm.is_exists_order_file():
            if not self.fm.create_order_file(ORDERFILE_NAME, self.tmp_creator.get_order_template()):
                logger.error("Failure create a default ORDER file!")
                return False

        if not self.fm.is_exists_chapter_file("main.yml"):
            if not self.fm.create_chapter_file("main.yml", self.tmp_creator.get_chapter_template()):
                logger.error("Failure create a default CHAPTER file!")
                return False

        if not self.fm.is_exists_episode_file("main.yml"):
            if not self.fm.create_episode_file("main.yml", self.tmp_creator.get_episode_template()):
                logger.error("Failure create a default EPISODE file!")
                return False

        if not self.fm.is_exists_scene_file("main.md"):
            if not self.fm.create_scene_file("main.md", self.tmp_creator.get_scene_template()):
                logger.error("Failure create a default SCENE file!")
                return False

        if not self.fm.is_exists_note_file("main.md"):
            if not self.fm.create_note_file("main.md", self.tmp_creator.get_note_template()):
                logger.error("Failure create a default NOTE file!")
                return False

        if not self.fm.is_exists_person_file("main.yml"):
            if not self.fm.create_person_file("main.yml", self.tmp_creator.get_person_template()):
                logger.error("Failure create a default PERSON file!")
                return False

        if not self.fm.is_exists_stage_file("main.yml"):
            if not self.fm.create_stage_file("main.yml", self.tmp_creator.get_stage_template()):
                logger.error("Failure create a default STAGE file!")
                return False

        if not self.fm.is_exists_item_file("main.yml"):
            if not self.fm.create_item_file("main.yml", self.tmp_creator.get_item_template()):
                logger.error("Failure create a default ITEM file!")
                return False

        if not self.fm.is_exists_word_file("main.yml"):
            if not self.fm.create_word_file("main.yml", self.tmp_creator.get_word_template()):
                logger.error("Failure create a default WORD file!")
                return False

        logger.debug("Created: template files")
        return True

    # private methods
    def _has_project_file(self) -> bool:
        cwd = os.getcwd()
        path = os.path.join(cwd, PROJECTFILE_NAME)
        return os.path.exists(path)

    def _input_with_namelist(self, message: str, namelist: list) -> str:
        print(self._serialized_namelist_of(namelist))
        return input(message)

    def _serialized_namelist_of(self, names: list, with_num: bool=True) -> str:
        tmp = []
        idx = 0
        for name in names:
            tmp.append(f"{idx}:{name}" if with_num else name)
            idx += 1
        return " ".join(tmp)
