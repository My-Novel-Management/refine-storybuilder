#!/usr/bin/env python3
from setuptools import setup, find_packages

from storybuilder import __version__ as VERSION


# Define constants
PACKAGE_NAME = 'storybuilder'
LICENSE = 'MIT'
AUTHOR = 'N.T.WORKS'
EMAIL = 'nagisc007@yahoo.co.jp'
SHORT_DESCRIPTION = 'Helper application to build your story'
LONG_DESCRITPYION = """StoryBuilder is the helper application that build your story, novel, screenplay or game scripts.
"""

setup(
        name=PACKAGE_NAME,
        version=VERSION,
        license=LICENSE,
        author=AUTHOR,
        author_email=EMAIL,
        packages=find_packages(),
        scripts=['bin/storybuilder'],
        description=SHORT_DESCRIPTION,
        long_description=LONG_DESCRITPYION,
        tests_require=['pytest',],
)
