#!/usr/bin/env python3
import pygame
import random

from pygame_framework.Colors import Colors
from pygame_framework.Util import Util
from pygame_framework.SceneMenu import SceneMenu
from pygame_framework.MenuHOrientation import MenuHOrientation
from pygame_framework.MenuVOrientation import MenuVOrientation
from pygame_framework.MenuTheme import MenuTheme
from pygame_framework.MenuUtil import MenuUtil
from pygame_framework.MenuObjectType import MenuObjectType

class scene2(SceneMenu):
    
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

        self.addMenu("btn2", "Play Snake", "Scene 3") # btnQuit : This is a reserved word

        self.addMenu("btnQuit", "Quit", None) # btnQuit : This is a reserved word

        #****************************************

        #Load pygame image
        img = "example/images/pygame.png"
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(center = (self.width //2, 440))

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


