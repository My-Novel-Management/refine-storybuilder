"""Utility module for text convert."""

# official libraries
import re

# my modules


class TextConverter(object):

    """Utility module for story output."""

    def __init__(self):
        pass

    # methods
    def conv_text_from_tag(self, text: str, tagdb: dict, prefix: str='$') -> str:
        tmp = text
        for key, val in tagdb.items():
            if prefix in tmp:
                tag_key = f"{prefix}{key}"
                if tag_key in tmp:
                    tmp = re.sub(r'\{}{}'.format(prefix, key), val, tmp)
        return tmp
