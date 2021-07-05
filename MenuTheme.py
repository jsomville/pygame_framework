#!/usr/bin/env python3

from Colors import Colors


class MenuTheme(dict):

    def __init__(self):
        self["window_width"] = 1152
        self["window_height"] = 768

        self["base_size"] = (250, 40)
        self["space"] = 10
        self["font"] = 'arial'

        self["heading"] = dict()
        self["heading"][1] = 30
        self["heading"][2] = 25
        self["heading"][3] = 20

        self["btn_back_color"] = Colors.DARK_GRAY
        self["btn_back_hover_color"] = Colors.CHOCOLATE
        self["btn_text_color"] = Colors.WHITE

        self["title_back_color"] = Colors.DARK_GRAY
        self["title_text_color"] = Colors.ORANGE

        self["lbl_back_color"] = Colors.LIGHT_GRAY
        self["lbl_text_color"] = Colors.BLACK
