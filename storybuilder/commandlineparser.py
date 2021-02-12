"""Commandline arguments and option parser."""

# official libraries
import argparse

# my modules
from storybuilder.util.log import logger


PROGRAM_NAME = 'storybuilder'
"""str: program name for argument parser."""

DESCRIPTION = """
story building manager on cui.
"""
"""str: description for argument parser."""


class CommandlineParser(object):

    """Parser that commandline arguments."""

    def __init__(self):
        self._parser = argparse.ArgumentParser(
                prog=PROGRAM_NAME,
                description=DESCRIPTION,
                )

        # set commands
        self._parser.add_argument('cmd', metavar='command', type=str, help='builder command')
        self._parser.add_argument('arg0', metavar='arg0', type=str, nargs='?', help='sub command or any arguments')
        self._parser.add_argument('arg1', metavar='arg1', type=str, nargs='?', help='any arguments')
        logger.debug("Initialized: Commandline Parser")

    # methods
    def get_commandline_arguments(self) -> argparse.Namespace:
        '''Get commandline arguments and parsed list.

        Arguments:

        Returns:
            The list has commandline arguments.
        '''
        args = self._parser.parse_args()
        return args

