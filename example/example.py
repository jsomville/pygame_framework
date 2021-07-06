#!/usr/bin/env python3
from enum import Enum
from datetime import datetime

import pygame
from pygame.locals import *

#Import Scene Here
from .example_Scene1 import Scene1
from .example_SceneMenu import Scene_Menu

class App:

    def __init__(self):
        """ App object initialization function, here you set variables default values"""
        self.windowWidth = 1152
        self.windowHeight = 768
        self.FPS = 10

        self._running = True
        self._display_surf = None
        self.image = None
        self.frame_per_sec = None

        self.scenes = dict()
        self.active_scene = None


    def on_init(self):
        """Game initialisation function, here you load scenes, images, sounds, etc."""
        
        #pygame initialisation
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.frame_per_sec = pygame.time.Clock()

        #Set the window caption
        pygame.display.set_caption("pygame_template Example")

        #*************************************
        #SCENE Declaration !!!

        #Load scene with Menu 
        aScene = Scene_Menu()
        aScene.size = (self.windowWidth, self.windowHeight)
        self.add_scene(aScene)

        #Load scenes with Random Rectangle
        aScene = Scene1()
        aScene.size = (self.windowWidth, self.windowHeight)
        self.add_scene(aScene)


        #Set active scene
        self.active_scene = self.scenes["menu"]
        #**************************************

        #Enable the control loop 
        self._running = True


    def add_scene(self, aScene):
        aScene.on_init()
        self.scenes[aScene.name] = aScene


    def on_event(self, event):
        """Function designed to hanlde events such as user input (keyboard, mouse, etc"""

        #Quit Event
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.USEREVENT:
            #Switch scene event
            if "goto" in event.__dict__:
                # Scene on_event
                print("Goto : " + event.__dict__["goto"])

                if event.__dict__["goto"] in self.scenes:
                    self.active_scene = self.scenes[event.__dict__["goto"]]
                else:
                    raise Exception('Scene' + event.__dict__["goto"] + " not found")

        #Force on_event management on active scene
        if self.active_scene != None:
            if self.active_scene.inited:
                self.active_scene.on_event(event)


    def on_loop(self):
        """Function to specify the game logic"""

        #Force on_loop on active scene
        if self.active_scene != None:
            self.active_scene.on_loop()

            self.active_scene = self.active_scene.next

            if self.active_scene == None:
                self._running = False


    def on_render(self):
        """Function specialized for surface rendering only"""

        #Force on_render on active scene
        if self.active_scene != None:
            self.active_scene.on_render(self._display_surf)

        #Refresh Surface
        rect = self._display_surf.get_rect()
        pygame.display.update(rect)


    def on_cleanup(self):
        """Function to handle app uninitialized"""
        print("Application Cleanup")
        pygame.quit()


    def on_execute(self):
        """Main Execute function and main loop, calls on_init, on_event, on_loop, on_logic  """
        
        #Init application and load scenes
        self.on_init()

        #Main Loop
        while (self._running):
            #Handle Events
            for event in pygame.event.get():
                self.on_event(event)

            #Game Logic
            self.on_loop()

            #Render code
            self.on_render()

            #Ensure FPS is respected (try at least)
            self.frame_per_sec.tick(self.FPS)
        
        #On cleanup
        self.on_cleanup()


if __name__ == "__main__":
    """Program entry function"""
    theApp = App()
    theApp.on_execute()
