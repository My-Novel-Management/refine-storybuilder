#!/usr/bin/env python3
from setuptools import setup, find_packages
import sys

from storybuilder import __version__ as VERSION

setup(
        name='storybuilder',
        version=VERSION,
        license='MIT',
        author='N.T.WORKS',
        author_email='nagisc007@yahoo.co.jp',
        packages=find_packages(),
        scripts=['bin/storybuilder'],
        description='Story Building Helper',
        long_description="""StoryBuilder is the helper for story building such as novel, movie screenplay etc.
        """,
)
