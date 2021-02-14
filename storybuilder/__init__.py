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

PROJECTFILE_EXT = YAML_EXT
"""str: extention of project file."""

BOOKFILE_EXT = YAML_EXT
"""str: extention of book file."""

ORDERFILE_EXT = YAML_EXT
"""str: extention of order file."""

CHAPTERFILE_EXT = YAML_EXT
"""str: extention of chapter file."""

EPISODEFILE_EXT = YAML_EXT
"""str: extention of episode file."""

SCENEFILE_EXT = MARKDOWN_EXT
"""str: extention of scene file."""

NOTEFILE_EXT = MARKDOWN_EXT
"""str: extention of note file."""

PERSONFILE_EXT = YAML_EXT
"""str: extention of person file."""

STAGEFILE_EXT = YAML_EXT
"""str: extention of stage file."""

ITEMFILE_EXT = YAML_EXT
"""str: extention of item file."""

WORDFILE_EXT = YAML_EXT
"""str: extention of word file."""

PROJECTFILE_NAME = f"project.{YAML_EXT}"
"""str: the file name of project."""

BOOKFILE_NAME = f"book.{YAML_EXT}"
"""str: file name of book."""

ORDERFILE_NAME = f"order.{YAML_EXT}"
"""str: file name of order."""


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

