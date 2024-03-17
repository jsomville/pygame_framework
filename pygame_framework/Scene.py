#!/usr/bin/env python3
import pygame
from pygame.locals import *

from pygame_framework import UI_Button

from .Colors import Colors
from .UI_Button import UI_Button
from .UI_Position import UI_Position
from .UI_Size import UI_Size
from .MenuObjectType import MenuObjectType

class Scene(pygame.Rect):
    """This scene class is a pygame rectangle and can handle event, loop, render"""

    def __init__(self):
        """ DO NOT REDEFINE THIS METHOD"""
        self.next = self
        self.name = "default"
        self.inited = False
        self.BACKGROUND = Colors.BLACK

        self.controls = list()
    

    def addControl(self, control):
        control.on_init()
        self.controls.append(control)

    def on_init(self):
        """ Redefine this method in your own class"""
        raise Exception('Scene on_init function needs to be override')

    def on_event(self, event):
        """ Redefine this method in your own class"""
        raise Exception('Scene on_event function needs to be override')

    def on_loop(self):
        """ Redefine this method in your own class"""
        raise Exception('Scene on_loop function needs to be override')

    def on_render(self, surface):
        """ Redefine this method in your own class"""
        raise Exception('Scene on_render function needs to be override')

    def switch_to_scene(self, next_scene):
        """ DO NOT REDEFINE THIS METHOD"""
        self.next = next_scene

    def fire_goto_event(self, where):
        """ DO NOT REDEFINE THIS METHOD"""
        event_dict = dict()
        event_dict["goto"] = where
        new_event = pygame.event.Event(pygame.USEREVENT, event_dict)
        pygame.event.post(new_event)
    
    def render_controls(self, surface):
        for control in self.controls:
            control.on_render(surface)


    def event_controls(self, event):
        for control in self.controls:
            control.on_loop(event)
