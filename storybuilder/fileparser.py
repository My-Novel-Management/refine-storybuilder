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

    def get_from_markdown(self, fname: str) -> dict:
        tmp = []
        fronts =[]
        res = []
        in_frontmatter = False
        with open(fname, 'r', encoding=BASE_ENCODING) as file:
            tmp = file.readlines()
        for line in tmp:
            _line = line.rstrip('\r\n')
            if _line == '---':
                if in_frontmatter:
                    in_frontmatter = False
                    continue
                else:
                    in_frontmatter = True
            if in_frontmatter:
                fronts.append(_line)
            else:
                res.append(_line)
        if fronts:
            _res = yaml.safe_load("\n".join(fronts))
            return {**_res, **{'markdown': res}}
        else:
            return {'markdown': res}

    def get_from_yaml(self, fname: str) -> dict:
        with open(fname, 'r', encoding=BASE_ENCODING) as file:
            tmp = yaml.safe_load(file)
            return tmp

    # private methods
    def _rid_null_status(self, txt: str) -> str:
        return txt.replace('null', '')
