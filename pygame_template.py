#!/usr/bin/env python3
from enum import Enum
from datetime import datetime
import pygame
from pygame.locals import *

from Colors import Colors
from Scene1 import Scene1

class App:
    windowWidth = 1152
    windowHeight = 768
    FPS = 35

    #Handle scenes
    scenes = dict()
    active_scene = None

    def __init__(self):
        """ App object initialization function, here you set variables default values"""
        self._running = True
        self._display_surf = None
        self.image = None
        self.frame_per_sec = None

    def on_init(self):
        """Game initialisation function, here you load scenes, images, sounds, etc."""
        
        #pygame initialisation
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.frame_per_sec = pygame.time.Clock()

        #Set the window caption
        pygame.display.set_caption("Advanced template for a pygame application")

        #Load scenes
        scene1 = Scene1()
        scene1.size = (self.windowWidth, self.windowHeight)
        self.scenes[scene1.name] = scene1
        self.active_scene = scene1

        #Add another scene here
        #scene2 = aScene()
        #scene2.size = (self.windowWidth, self.windowHeight)
        #self.scenes[scene2.name] = scene2


    def on_event(self, event):
        """Function designed to hanlde events such as user input (keyboard, mouse, etc"""

        #Quit Event
        if event.type == pygame.QUIT:
            self._running = False

        #Scene on_event
        if self.active_scene != None:
            self.active_scene.on_event(event)


    def on_loop(self):
        """Function to specify the game logic"""

        #Scene on_loop
        if self.active_scene != None:
            self.active_scene.on_loop()

            self.active_scene = self.active_scene.next

            if self.active_scene == None:
                self._running = False

    def on_render(self):
        """Function specialized for surface rendering only"""

        #Scene on_render
        if self.active_scene != None:
            self.active_scene.on_render(self._display_surf)

    def on_cleanup(self):
        """Function to handle app uninitialized"""
        pygame.quit()

    def on_execute(self):
        """Main Execute function and main loop, calls on_init, on_event, on_loop, on_logic  """
        #Init application
        if self.on_init() == False:
            self._running = False

        #Main Loop
        while (self._running):
            #Handle Events
            for event in pygame.event.get():
                self.on_event(event)

            #Game Logic
            self.on_loop()

            #Render code
            self.on_render()

            self.frame_per_sec.tick(self.FPS)
        
        self.on_cleanup()


if __name__ == "__main__":
    """Program entry function"""
    theApp = App()
    theApp.on_execute()
