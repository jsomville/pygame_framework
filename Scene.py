#!/usr/bin/env python3
import pygame
from pygame.locals import *


class Scene(pygame.Rect):
    """This scene class is a pygame rectangle and can handle event, loop, render"""
    name = "default scene"
    inited = False

    def __init__(self):
        self.next = self

        print("Init " + self.name + " scene")

    def on_init(self):
        raise Exception('Scene on_init function needs to be override')

    def on_event(self, event):
        raise Exception('Scene on_event function needs to be override')

    def on_loop(self):
        raise Exception('Scene on_loop function needs to be override')

    def on_render(self, surface):
        raise Exception('Scene on_render function needs to be override')

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def fire_goto_event(self, where):

        event_dict = dict()
        event_dict["goto"] = where
        new_event = pygame.event.Event(pygame.USEREVENT, event_dict)
        pygame.event.post(new_event)

