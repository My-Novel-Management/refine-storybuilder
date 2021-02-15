"""Utility module for file paths."""

# official libraries
import os


def conv_filenames_from_fullpaths(paths: list) -> list:
    '''Get file name list that converted from fullpath list.
    '''
    tmp = []
    for name in paths:
        tmp.append(conv_only_basename(name))
    sorted_tmp = sorted(tmp)
    return sorted_tmp


def conv_only_basename(filepath: str) -> str:
    '''Get file name only, except extention and directory name.
    '''
    return os.path.splitext(os.path.basename(filepath))[0]

