#!/usr/bin/env python3
import pygame
import random

from Scene import Scene
from Colors import Colors
from Util import Util
from MenuHOrientation import MenuHOrientation
from MenuVOrientation import MenuVOrientation
from MenuTheme import MenuTheme
from MenuUtil import MenuUtil
from MenuObjectType import MenuObjectType

class Scene_Menu(Scene):
    
    def on_init(self):
        self.name = "menu"
        self.inited = True

        #Redefinie Background color
        self.BACKGROUND = Colors.BLACK

        #Title
        self.title = "This is a menu, click any button"
        self.title_font = pygame.font.SysFont("Arial", 24)

        #Menu Init
        self.v_orientation = MenuVOrientation.CENTER
        self.h_orientation = MenuHOrientation.CENTER
        self.menu_list = list()
        self.menu_dict = dict()
        self.theme = MenuTheme()
        self.menu_util = MenuUtil()

        #****************************************
        #Menu Content
        self.addLabel("lblMenu", "This is a Title" )

        self.addMenu("btn1", "Click Rectangle", "Scene 1")

        self.addMenu("btnQuit", "Quit", None)

        #****************************************

        #Last step of intitialisation
        self.menu_util.on_init(self.size, self.menu_list, self.v_orientation, self.h_orientation)
        self.inited = True
   
    def addLabel(self, name, text):
        btn = dict()
        btn["name"] = name
        btn["type"] = MenuObjectType.TITLE
        btn["text"] = text
        self.menu_list.append(btn)

    def addMenu(self, name, text, goto):
        btn = dict()
        btn["name"] = name
        btn["type"] = MenuObjectType.BUTTON
        btn["text"] = text
        btn["goto"] = goto
        self.menu_list.append(btn)
        self.menu_dict[btn["name"]] = btn

    def on_event(self, event):

        #Handle menu specific events
        self.menu_util.on_event(event, self.menu_list)

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


    def on_loop(self):
        pass
       
    def on_render(self, surface):
        surface.fill(self.BACKGROUND)

        #Draw Menu
        self.menu_util.draw_menu(surface, self.menu_list)

        #Draw Title on center surface x
        Util().draw_text_center_x(surface, self.title, self.title_font, Colors.BLACK, 15)

