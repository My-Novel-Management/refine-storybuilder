"""Utility module for this application logger."""

# official library
import logging
import logging.handlers
import os
import sys


# Formatters
FILE_FORMATTER = logging.Formatter("[%(levelname)s:%(asctime)s:%(module)s]: %(message)s")
"""Format for a log file."""

SIMPLE_FORMATTER = logging.Formatter("%(asctime)s: %(message)s")
"""Format as a simple style."""

DEBUG_FORMATTER = logging.Formatter("%(levelname)-8s %(asctime)s [%(module)s.%(funcName)s:%(lineno)s]:%(message)s")
"""Format for debug."""


# Directories
HOME = os.environ['HOME']
CACHE_DIR = os.path.join(HOME, '.cache')
BUILER_CACHE_DIR = os.path.join(CACHE_DIR, 'storybuilder')


# check the cache directory
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

if not os.path.exists(BUILER_CACHE_DIR):
    os.makedirs(BUILER_CACHE_DIR)


# Log file setup
LOG_FILENAME = os.path.join(BUILER_CACHE_DIR, "storybuilder.log")
loghandler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20971520, backupCount=5)
loghandler.setFormatter(FILE_FORMATTER)


# Logger setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(loghandler)


# Set the logging level to show debug messages.
console_handler = logging.StreamHandler(stream=sys.stderr)
console_handler.setFormatter(SIMPLE_FORMATTER)
logger.addHandler(console_handler)


# Set the debug level for this application.
if __debug__:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

