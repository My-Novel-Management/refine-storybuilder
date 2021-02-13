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
            if not has_project:
                # create project file
                if not self.create_project_file():
                    logger.error("Error in create project file!")
                    result = False
            else:
                if not self.create_project_templates():
                    logger.error("Error in create project templates!")
                    result = False
            if not result:
                logger.error("Error and Exit! [in initialize phase]")
                exit_code = 1
                return exit_code

        # switch by command

        # check result
        if not result:
            exit_code = 1

        return exit_code

    # methods (command)
    def on_init_project(self) -> bool:
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

        return True

    # private methods
    def _has_project_file(self) -> bool:
        cwd = os.getcwd()
        path = os.path.join(cwd, PROJECTFILE_NAME)
        return os.path.exists(path)

