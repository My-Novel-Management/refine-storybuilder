"""Build module for story builder project."""

# official libraries
from dataclasses import dataclass

# my modules
from typing import Any
from storybuilder.projectfilemanager import ProjectFileManager


@dataclass
class BuildRecord(object):
    rcd_type: str
    name: str
    data: dict
    body: Any=None


class ProjectBuilder(object):

    """Build module for project."""

    def __init__(self, project_fil_manager: ProjectFileManager):
        self.fm = project_fil_manager

    # methods
    def build(self) -> bool:
        # create serialized order data
        data = self.fm.get_order_data()
        tmp = []
        for ch_record in data['book']:
            # chapter level
            for key in ch_record.keys():
                tmp.append(key)
            for ep_record in ch_record.values():
                # episode level
                for ep_data in ep_record:
                    for key in ep_data.keys():
                        tmp.append(key)
                    for sc_record in ep_data.values():
                        for sc_data in sc_record:
                            tmp.append(sc_data)

        # build each container data
        story_records = []
        ## book
        story_records.append(BuildRecord('book', 'book', {}))
        for record in tmp:
            story_records.append(
                    BuildRecord(
                        self.fm.get_category_from_ordername(record),
                        self.fm.get_basename_from_ordername(record),
                        self.fm.get_data_from_ordername(record)))
        for rcd in story_records:
            print(rcd)
        return True
