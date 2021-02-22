"""Database Manager for storybuilder."""

# official libraries

# my modules
from storybuilder.util.log import logger


class DBManager(object):

    """DB manager for storybuilder."""

    def __init__(self):
        self.names = {}

    # methods
    def add_person_name(self, key: str, name: str, fullname: str) -> bool:
        lastname, firstname = fullname.split(',') if ',' in fullname else (name, name)
        _first = firstname if firstname else name
        _last = lastname if lastname else name
        _full = f"{_last}{_first}" if firstname else name
        _efull = f"{_first}・{_last}" if firstname else name
        return self._add_name_to_namedb(key, name) \
                and self._add_name_to_namedb(f"p_{key}", name) \
                and self._add_name_to_namedb(f"fn_{key}", _first) \
                and self._add_name_to_namedb(f"ln_{key}", _last) \
                and self._add_name_to_namedb(f"full_{key}", _full) \
                and self._add_name_to_namedb(f"efull_{key}", _efull)

    def add_stage_name(self, key: str, name: str) -> bool:
        return self._add_name_to_namedb(key, name) and self._add_name_to_namedb(f"st_{key}", name)

    def add_item_name(self, key: str, name: str) -> bool:
        return self._add_name_to_namedb(key, name) and self._add_name_to_namedb(f"i_{key}", name)

    def add_word_name(self, key: str, name: str) -> bool:
        return self._add_name_to_namedb(key, name) and self._add_name_to_namedb(f"w_{key}", name)

    def sort_db(self) -> bool:
        self.names = dict(sorted(self.names.items()))
        return True

    # private methods
    def _add_name_to_namedb(self, key: str, name: str) -> bool:
        self.names[key] = name
        return True
