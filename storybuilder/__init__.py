"""Main StoryBuilder Package"""

# official libraries
import os


# Application data
__version__ = "0.0.1"
"""str: this application version number."""

# Sahred setting
BASE_ENCODING = 'utf-8'
"""str: base encoding."""

YAML_EXT = 'yml'
"""str: extention of YAML file."""

MARKDOWN_EXT = 'md'
"""str: extention of Markdown file."""


# Base paths
HOME = os.environ['HOME']
"""str: path of user home directory."""

USR_CACHE_DIR = os.path.join(HOME, '.cache')
"""str: path of user cache directory."""

USR_CONFIG_DIR = os.path.join(HOME, '.config')
"""str: path of user config directory."""

PROJECTFILE_NAME = f"project.{YAML_EXT}"
"""str: the file name of project."""

CHAPTER_DIR = 'chapters'
"""str: directory name of chapter files."""

EPISODE_DIR = 'episodes'
"""str: directory name of episode files."""

SCENE_DIR = 'scenes'
"""str: directory name of scene files."""

NOTE_DIR = 'notes'
"""str: directory name of note files."""

PERSON_DIR = 'persons'
"""str: directory name of person files."""

STAGE_DIR = 'stages'
"""str: directory name of stage files."""

ITEM_DIR = 'items'
"""str: directory name of item files."""

WORD_DIR = 'words'
"""str: directory name of word files."""

