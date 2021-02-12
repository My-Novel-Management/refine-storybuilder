"""Internal settings for storybuilder."""

# official libraries
import os

# my modules
from storybuilder import __version__


PROJECT = "StoryBuilder"
"""str: application name."""

VERSION = __version__
"""str: application version."""

COPYRIGHT = "(c)2020,2021 N.T.WORKS"
"""str: application copyright."""

AUTHORS = ["N.T.WORKS",]
"""list[str]: application authors."""


HOME = os.environ['HOME']
"""str: path of HOME directory."""

USR_CACHE_DIR = os.path.join(HOME, '.cache')
"""str: path of user cache directory."""

BUILDER_CACHE_DIR = os.path.join(USR_CACHE_DIR, 'storybuilder')
"""str: path of this application cache directory."""


# check and create directory
if not os.path.exists(BUILDER_CACHE_DIR):
    os.makedirs(BUILDER_CACHE_DIR)


USR_CONFIG_DIR = os.path.join(HOME, '.config')
"""str: path of user config directory."""

BUILDER_CONFIG_DIR = os.path.join(USR_CONFIG_DIR, 'storybuilder')
"""str: path of this application config directory."""


# check and create directory
if not os.path.exists(BUILDER_CONFIG_DIR):
    os.makedirs(BUILDER_CONFIG_DIR)

