"""Main application for storybuilder."""

# official libraries
import os

# my modules
from storybuilder.commandlineparser import CommandlineParser
from storybuilder.projectfilemanager import ProjectFileManager
from storybuilder.templatecreator import TemplateCreator
from storybuilder.util.log import logger
from storybuilder import PROJECTFILE_NAME


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

        result = False
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
                    result = False
            else:
                result = self.create_project_templates()

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
        # create temp files
        return True

    # private methods
    def _has_project_file(self) -> bool:
        cwd = os.getcwd()
        path = os.path.join(cwd, PROJECTFILE_NAME)
        return os.path.exists(path)

