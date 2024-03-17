#!/usr/bin/env python3
from enum import Enum
from datetime import datetime

import pygame

#Import Scenes Here
from .scene1 import scene1
from .scene2 import scene2
from .scene3 import scene3
from .scene4 import scene4

class app:
    def __init__(self):
        """ App object initialization function, here you set variables default values"""
        self.windowWidth = 800
        self.windowHeight = 600

        self.WINDOW_SIZE = (self.windowWidth, self.windowHeight)
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

        #Add different scenes
        self.create_scenes()

        #Enable the control loop 
        self._running = True

    def create_scenes(self):
        #Load scene with Menu 
        aScene = scene2()
        self.add_scene(aScene)

        #Load scenes with Random Rectangle
        aScene = scene1()
        self.add_scene(aScene)

        #New scene
        aScene = scene3()
        self.add_scene(aScene)

        #Button scene
        aScene = scene4()
        self.add_scene(aScene)

        #Set active scene
        self.active_scene = self.scenes["menu"]


    def add_scene(self, aScene):
        aScene.size = self.WINDOW_SIZE
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
                    raise Exception('Scene: ' + event.__dict__["goto"] + " not found")

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