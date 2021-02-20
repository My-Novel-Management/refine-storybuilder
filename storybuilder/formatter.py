"""Format module for storybuilder output."""

# official libraries


# my modules
from storybuilder.util.log import logger
from storybuilder.datamanager import StoryCode


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

    def conv_script_format(self, story_codes: list, is_detail: bool=False) -> list:
        # NOTE: 要素がないときに省く
        tmp = []
        scene_data = {
                'camera': "",
                'stage': "",
                'year': "",
                'date': "",
                'time': "",
                }
        for code in story_codes:
            assert isinstance(code, StoryCode)
            if code.head == 'book-title':
                tmp.append(f"# {code.body}\n\n")
            elif code.head == 'chapter-title':
                tmp.append(f"## {code.body}\n\n")
            elif code.head == 'episode-title':
                tmp.append(f"### {code.body}\n\n")
            elif code.head == 'scene-title':
                tmp.append(f"**{code.body}**\n\n")
            elif code.head == 'scene-camera':
                scene_data['camera'] = code.body
            elif code.head == 'scene-stage':
                scene_data['stage'] = code.body
            elif code.head == 'scene-year':
                scene_data['year'] = code.body
            elif code.head == 'scene-date':
                scene_data['date'] = code.body
            elif code.head == 'scene-time':
                scene_data['time'] = code.body
            elif code.head == 'scene-start':
                if not is_detail:
                    tmp.append(f"○　{scene_data['stage']}（{scene_data['time']}）\n")
                else:
                    tmp.append(f"○　{scene_data['stage']}（{scene_data['time']}）／{scene_data['date']}-{scene_data['year']}＜{scene_data['camera']}＞\n")
            elif code.head == 'scene-end':
                tmp.append("\n")
            elif code.head == 'head-title':
                tmp.append(f"{code.body}\n")
            elif code.head == 'description':
                suffix = "" if code.body.endswith(('。', '、')) else "。"
                tmp.append(f"{code.body}{suffix}")
            elif code.head == 'dialogue':
                tmp.append(f"{code.foot}「{code.body}」")
            elif code.head == 'monologue':
                tmp.append(f"{code.foot}Ｍ『{code.body}』")
            elif code.head == 'br':
                tmp.append("\n")
            elif code.head == 'indent':
                tmp.append("　")
            else:
                continue
        return tmp

    def conv_novel_format(self, story_codes: list, shown_sc_title: bool=False) -> list:
        tmp = []
        for code in story_codes:
            assert isinstance(code, StoryCode)
            if code.head == 'book-title':
                tmp.append(f"# {code.body}\n\n")
            elif code.head == 'chapter-title':
                tmp.append(f"## {code.body}\n\n")
            elif code.head == 'episode-title':
                tmp.append(f"### {code.body}\n\n")
            elif code.head == 'scene-title' and shown_sc_title:
                tmp.append(f"**{code.body}**\n\n")
            elif code.head == 'scene-camera':
                continue
            elif code.head == 'scene-stage':
                continue
            elif code.head == 'scene-year':
                continue
            elif code.head == 'scene-date':
                continue
            elif code.head == 'scene-time':
                continue
            elif code.head == 'scene-start':
                continue
            elif code.head == 'scene-end':
                continue
            elif code.head == 'head-title':
                tmp.append(f"{code.body}\n")
            elif code.head in ('description', 'monologue'):
                suffix = "" if code.body.endswith(('。', '、')) else "。"
                tmp.append(f"{code.body}{suffix}")
            elif code.head == 'dialogue':
                tmp.append(f"「{code.body}」")
            elif code.head == 'br':
                tmp.append("\n")
            elif code.head == 'indent':
                tmp.append("　")
            else:
                continue

        return tmp

    def get_break_line(self) -> str:
        return "--------" * 8 + '\n'

