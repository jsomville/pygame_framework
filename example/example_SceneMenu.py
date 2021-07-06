#!/usr/bin/env python3
import pygame
import random

from SceneMenu import SceneMenu
from Colors import Colors
from Util import Util
from MenuHOrientation import MenuHOrientation
from MenuVOrientation import MenuVOrientation
from MenuTheme import MenuTheme
from MenuUtil import MenuUtil
from MenuObjectType import MenuObjectType

class Scene_Menu(SceneMenu):
    
    def on_init(self):
        self.name = "menu"
        self.inited = True

        #Redefinie Background color
        self.BACKGROUND = Colors.BLACK

        #Title
        self.title = "This is a menu, click any button"
        self.title_font = pygame.font.SysFont("Arial", 24)

        #Menu Init
        SceneMenu.on_init(self)
        self.v_orientation = MenuVOrientation.CENTER
        self.h_orientation = MenuHOrientation.CENTER
        self.theme = MenuTheme()
        self.menu_util = MenuUtil()

        #****************************************
        #Menu Content
        self.addLabel("lblMenu", "This is a Title" )

        self.addMenu("btn1", "Click Rectangle", "Scene 1")

        self.addMenu("btnQuit", "Quit", None) # btnQuit : This is a reserved word

        #****************************************

        #Load pygame image
        img = "images/pygame.png"
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(center = (self.width //2, 600))

        #Last step of intitialisation
        self.menu_util.on_init(self.size, self.menu_list, self.v_orientation, self.h_orientation)
        self.inited = True

    def on_event(self, event):
        SceneMenu.on_event(self, event)

    def on_loop(self):
        pass
       
    def on_render(self, surface):
        surface.fill(self.BACKGROUND)

        SceneMenu.on_render(self, surface)

        #Draw Title on center surface x
        Util().draw_text_center_x(surface, self.title, self.title_font, Colors.BLACK, 15)

        #Draw pygame Logo
        surface.blit(self.image, self.rect)


