"""Format module for storybuilder output."""

# official libraries


# my modules
from storybuilder.util.log import logger


class StoryFormatter(object):

    """Format module for storybuilder."""

    def __init__(self):
        pass

    # methods
    def conv_contents_list_format(self, contents_list: list) -> list:
        tmp = []
        tmp.append(f"{contents_list[0]}\n")
        tmp.append('====\n\n')
        tmp.append("## Contents\n\n")
        for line in contents_list[1:]:
            tmp.append(f"{line}\n")
        return tmp

    def conv_outline_format(self, level: str, titles: list, outlines: list) -> list:
        tmp = []
        if level == 'book':
            tmp.append("## BOOK outline\n\n")
        elif level == 'chapter':
            tmp.append("## Chapter outlines\n\n")
        elif level == 'episode':
            tmp.append("## Episode outlines\n\n")
        elif level == 'scene':
            tmp.append("## Scene outlines\n\n")
        else:
            tmp.append("## outlines\n\n")

        for title, outline in zip(titles, outlines):
            tmp.append(f"**{title}**\n")
            tmp.append(f"    {outline}\n\n")
        return tmp

    def conv_plot_format(self, level: str, titles: list, plots: list) -> list:
        tmp = []
        if level == 'book':
            tmp.append("## BOOK plots\n\n")
        elif level == 'chapter':
            tmp.append("## Chapter plots\n\n")
        elif level == 'episode':
            tmp.append("## Episode plots\n\n")
        elif level == 'scene':
            tmp.append("## Scene plots\n\n")
        else:
            tmp.append("## plots\n\n")

        for title, plot in zip(titles, plots):
            tmp.append(f"**{title}**\n")
            tmp.append(f"    {plot['setup']}\n")
            tmp.append(f"    ↓←{plot['tp1st']}\n")
            tmp.append(f"    {plot['develop']}\n")
            tmp.append(f"    ↓←{plot['tp2nd']}\n")
            tmp.append(f"    {plot['climax']}\n")
            tmp.append(f"    ↓\n")
            tmp.append(f"    {plot['resolve']}\n\n")
        return tmp

    def conv_script_format(self) -> list:
        tmp = []
        return tmp

    def conv_novel_format(self) -> list:
        tmp = []
        return tmp

    def get_break_line(self) -> str:
        return "--------" * 8 + '\n'

