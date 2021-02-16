"""Parser for storybuilder files."""

# official libraries
import yaml

# my modules
from storybuilder import BASE_ENCODING


class FileParser(object):

    """Parser for storybuilder's file."""

    def __init__(self):
        pass

    # methods
    def conv_dumpdata_as_yaml(self, data: dict) -> str:
        tmp = yaml.safe_dump(data, default_flow_style=False)
        return self._rid_null_status(tmp)

    def get_from_yaml(self, fname: str) -> dict:
        with open(fname, 'r', encoding=BASE_ENCODING) as file:
            tmp = yaml.safe_load(file)
            return tmp

    # private methods
    def _rid_null_status(self, txt: str) -> str:
        return txt.replace('null', '')
