"""Main StoryBuilder Package"""

# official libraries
import os


# Define public constants
__version__ = "0.0.1"
"""str: this application version number."""

HOME = os.environ['HOME']
"""str: path of user home directory."""

USR_CACHE_DIR = os.path.join(HOME, '.cache')
"""str: path of user cache directory."""

USR_CONFIG_DIR = os.path.join(HOME, '.config')
"""str: path of user config directory."""

