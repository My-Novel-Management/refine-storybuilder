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
                pass
            elif cmdargs.arg0 in ('e', 'episode'):
                pass
            elif cmdargs.arg0 in ('s', 'scene'):
                pass
            elif cmdargs.arg0 in ('n', 'note'):
                pass
            elif cmdargs.arg0 in ('p', 'person'):
                pass
            elif cmdargs.arg0 in ('t', 'stage'):
                pass
            elif cmdargs.arg0 in ('i', 'item'):
                pass
            elif cmdargs.arg0 in ('w', 'word'):
                pass
            else:
                logger.error("Unknown Add command argument!: %s", cmdargs.arg0)
                result = False
        elif cmdargs.cmd in ('e', 'edit'):
            # Edit
            if cmdargs.arg0 in ('b', 'book'):
                pass
            elif cmdargs.arg0 in ('o', 'order'):
                pass
            elif cmdargs.arg0 in ('c', 'chapter'):
                pass
            elif cmdargs.arg0 in ('e', 'episode'):
                pass
            elif cmdargs.arg0 in ('s', 'scene'):
                pass
            elif cmdargs.arg0 in ('n', 'note'):
                pass
            elif cmdargs.arg0 in ('p', 'person'):
                pass
            elif cmdargs.arg0 in ('t', 'stage'):
                pass
            elif cmdargs.arg0 in ('i', 'item'):
                pass
            elif cmdargs.arg0 in ('w', 'word'):
                pass
            else:
                logger.error("Unknown Add command argument!: %s", cmdargs.arg0)
                result = False
        elif cmdargs.cmd in ('d', 'delete'):
            # Delete
            if cmdargs.arg0 in ('c', 'chapter'):
                pass
            elif cmdargs.arg0 in ('e', 'episode'):
                pass
            elif cmdargs.arg0 in ('s', 'scene'):
                pass
            elif cmdargs.arg0 in ('n', 'note'):
                pass
            elif cmdargs.arg0 in ('p', 'person'):
                pass
            elif cmdargs.arg0 in ('t', 'stage'):
                pass
            elif cmdargs.arg0 in ('i', 'item'):
                pass
            elif cmdargs.arg0 in ('w', 'word'):
                pass
            else:
                logger.error("Unknown Add command argument!: %s", cmdargs.arg0)
                result = False
        elif cmdargs.cmd in ('r', 'rename'):
            # Rename
            if cmdargs.arg0 in ('c', 'chapter'):
                pass
            elif cmdargs.arg0 in ('e', 'episode'):
                pass
            elif cmdargs.arg0 in ('s', 'scene'):
                pass
            elif cmdargs.arg0 in ('n', 'note'):
                pass
            elif cmdargs.arg0 in ('p', 'person'):
                pass
            elif cmdargs.arg0 in ('t', 'stage'):
                pass
            elif cmdargs.arg0 in ('i', 'item'):
                pass
            elif cmdargs.arg0 in ('w', 'word'):
                pass
            else:
                logger.error("Unknown Add command argument!: %s", cmdargs.arg0)
                result = False
        elif cmdargs.cmd in ('l', 'list'):
            # List
            if cmdargs.arg0 in ('c', 'chapter'):
                pass
            elif cmdargs.arg0 in ('e', 'episode'):
                pass
            elif cmdargs.arg0 in ('s', 'scene'):
                pass
            elif cmdargs.arg0 in ('n', 'note'):
                pass
            elif cmdargs.arg0 in ('p', 'person'):
                pass
            elif cmdargs.arg0 in ('t', 'stage'):
                pass
            elif cmdargs.arg0 in ('i', 'item'):
                pass
            elif cmdargs.arg0 in ('w', 'word'):
                pass
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
    def on_add_chapter(self) -> bool:
        logger.debug("Command: Add Chapter: start")
        return True

    def on_add_episode(self) -> bool:
        logger.debug("Command: Add Episode: start")
        return True

    def on_add_scene(self) -> bool:
        logger.debug("Command: Add Scene: start")
        return True

    def on_add_note(self) -> bool:
        logger.debug("Command: Add Note: start")
        return True

    def on_add_person(self) -> bool:
        logger.debug("Command: Add Person: start")
        return True

    def on_add_stage(self) -> bool:
        logger.debug("Command: Add Stage: start")
        return True

    def on_add_item(self) -> bool:
        logger.debug("Command: Add Item: start")
        return True

    def on_add_word(self) -> bool:
        logger.debug("Command: Add Word: start")
        return True

    def on_delete_chapter(self) -> bool:
        logger.debug("Command: Delete Chapter: start")
        return True

    def on_delete_episode(self) -> bool:
        logger.debug("Command: Delete Episode: start")
        return True

    def on_delete_scene(self) -> bool:
        logger.debug("Command: Delete Scene: start")
        return True

    def on_delete_note(self) -> bool:
        logger.debug("Command: Delete Note: start")
        return True

    def on_delete_person(self) -> bool:
        logger.debug("Command: Delete Person: start")
        return True

    def on_delete_stage(self) -> bool:
        logger.debug("Command: Delete Stage: start")
        return True

    def on_delete_item(self) -> bool:
        logger.debug("Command: Delete Item: start")
        return True

    def on_delete_word(self) -> bool:
        logger.debug("Command: Delete Word: start")
        return True

    def on_edit_book(self) -> bool:
        logger.debug("Command: Edit Book: start")
        return True

    def on_edit_order(self) -> bool:
        logger.debug("Command: Edit Book: start")
        return True

    def on_edit_chapter(self) -> bool:
        logger.debug("Command: Edit Chapter: start")
        return True

    def on_edit_episode(self) -> bool:
        logger.debug("Command: Edit Episode: start")
        return True

    def on_edit_scene(self) -> bool:
        logger.debug("Command: Edit Scene: start")
        return True

    def on_edit_note(self) -> bool:
        logger.debug("Command: Edit Note: start")
        return True

    def on_edit_person(self) -> bool:
        logger.debug("Command: Edit Person: start")
        return True

    def on_edit_stage(self) -> bool:
        logger.debug("Command: Edit Stage: start")
        return True

    def on_edit_item(self) -> bool:
        logger.debug("Command: Edit Item: start")
        return True

    def on_edit_word(self) -> bool:
        logger.debug("Command: Edit Word: start")
        return True

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

    def on_list_chapter(self) -> bool:
        logger.debug("Command: List Chapter: start")
        return True

    def on_list_episode(self) -> bool:
        logger.debug("Command: List Episode: start")
        return True

    def on_list_scene(self) -> bool:
        logger.debug("Command: List Scene: start")
        return True

    def on_list_note(self) -> bool:
        logger.debug("Command: List Note: start")
        return True

    def on_list_person(self) -> bool:
        logger.debug("Command: List Person: start")
        return True

    def on_list_stage(self) -> bool:
        logger.debug("Command: List Stage: start")
        return True

    def on_list_item(self) -> bool:
        logger.debug("Command: List Item: start")
        return True

    def on_list_word(self) -> bool:
        logger.debug("Command: List Word: start")
        return True

    def on_rename_chapter(self) -> bool:
        logger.debug("Command: Rename Chapter: start")
        return True

    def on_rename_episode(self) -> bool:
        logger.debug("Command: Rename Episode: start")
        return True

    def on_rename_scene(self) -> bool:
        logger.debug("Command: Rename Scene: start")
        return True

    def on_rename_note(self) -> bool:
        logger.debug("Command: Rename Note: start")
        return True

    def on_rename_person(self) -> bool:
        logger.debug("Command: Rename Person: start")
        return True

    def on_rename_stage(self) -> bool:
        logger.debug("Command: Rename Stage: start")
        return True

    def on_rename_item(self) -> bool:
        logger.debug("Command: Rename Item: start")
        return True

    def on_rename_word(self) -> bool:
        logger.debug("Command: Rename Word: start")
        return True

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
        if not self.fm.create_book_file(BOOKFILE_NAME, self.tmp_creator.get_book_template()):
            logger.error("Failure create a default BOOK file!")
            return False

        if not self.fm.create_order_file(ORDERFILE_NAME, self.tmp_creator.get_order_template()):
            logger.error("Failure create a default ORDER file!")
            return False

        if not self.fm.create_chapter_file("main.yml", self.tmp_creator.get_chapter_template()):
            logger.error("Failure create a default CHAPTER file!")
            return False

        if not self.fm.create_episode_file("main.yml", self.tmp_creator.get_episode_template()):
            logger.error("Failure create a default EPISODE file!")
            return False

        if not self.fm.create_scene_file("main.md", self.tmp_creator.get_scene_template()):
            logger.error("Failure create a default SCENE file!")
            return False

        if not self.fm.create_note_file("main.md", self.tmp_creator.get_note_template()):
            logger.error("Failure create a default NOTE file!")
            return False

        if not self.fm.create_person_file("main.yml", self.tmp_creator.get_person_template()):
            logger.error("Failure create a default PERSON file!")
            return False

        if not self.fm.create_stage_file("main.yml", self.tmp_creator.get_stage_template()):
            logger.error("Failure create a default STAGE file!")
            return False

        if not self.fm.create_item_file("main.yml", self.tmp_creator.get_item_template()):
            logger.error("Failure create a default ITEM file!")
            return False

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

