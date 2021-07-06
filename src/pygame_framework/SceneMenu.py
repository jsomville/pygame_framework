#!/usr/bin/env python3
import pygame

from .Scene import Scene
from .Colors import Colors
from .Util import Util
from .MenuHOrientation import MenuHOrientation
from .MenuVOrientation import MenuVOrientation
from .MenuTheme import MenuTheme
from .MenuUtil import MenuUtil
from .MenuObjectType import MenuObjectType

class SceneMenu(Scene):
    
    def on_init(self):
        """ initialize menu objects """
        self.menu_list = list()
        self.menu_dict = dict()

    def addLabel(self, name, text):
        """ add a label in menu list not in menu_dict """
        btn = dict()
        btn["name"] = name
        btn["type"] = MenuObjectType.TITLE
        btn["text"] = text
        self.menu_list.append(btn)

    def addMenu(self, name, text, goto):
        """ add a button in menu list and in menu_dict """
        btn = dict()
        btn["name"] = name
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = text
        btn["goto"] = goto
        self.menu_list.append(btn)
        self.menu_dict[btn["name"]] = btn

    def on_event(self, event):
        """ event for menu specific """

        #Handle menu specific events (Hover, Click)
        self.menu_util.on_event(event, self.menu_list)

        #Handle action specified in menu
        for control in self.menu_list:
            if control["type"] == MenuObjectType.BUTTON:
                if "click" in control:
                    if control["click"]:
                        if control["name"] == "btnQuit":
                            self.next = None
                        else:
                            if control["name"] in self.menu_dict:
                                self.fire_goto_event(control["goto"])

                        #Clear Click Event
                        control["click"] = False          
       
       
    def on_render(self, surface):
        """ Renders the menu """
        #Draw Menu
        self.menu_util.draw_menu(surface, self.menu_list)
