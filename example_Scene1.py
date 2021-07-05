#!/usr/bin/env python3
import pygame
import random

from Scene import Scene
from Colors import Colors
from Util import Util

class Scene1(Scene):
    
    def on_init(self):
        self.name = "Scene 1"
        
        #Redefinie Background color
        self.BACKGROUND = Colors.LIGHT_GRAY

        #Title
        self.title = "Click on the rectangle to exit this scene"
        self.title_font = pygame.font.SysFont("Arial", 24)

        #Rectangle Generation 
        self.counter = 0
        self.counter_max = 30
        self.sampleRect = pygame.Rect(40, 40, 100,100)

        #Last step of intitialisation
        self.inited = True


    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            pass
            #print ("keydown")

        elif event.type == pygame.KEYUP:
            #print ("keyup")
            pass

        elif event.type == pygame.MOUSEBUTTONUP:
            #print ("mouse button up")
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Click on rectangle to exit
            if event.button == 1:
                if self.sampleRect.collidepoint(event.pos):
                    print("You clicked on the rectangle")
                    
                    #Go to Menu Scene
                    self.fire_goto_event("menu")


    def on_loop(self):
        #Update Rect's position every counter_max
        self.counter += 1
        if self.counter >= self.counter_max:
            self.counter = 0

            #Random Rect Position
            x = random.randint(30, self.width - 100)
            y = random.randint(5, self.height - 100)

            #Update Rectangle position
            self.sampleRect.center = (x,y)

    def on_render(self, surface):
        surface.fill(self.BACKGROUND)

        #Draw Title on center surface x
        Util().draw_text_center_x(surface, self.title, self.title_font, Colors.BLACK, 15)

        #Draw Rect
        pygame.draw.rect(surface, Colors.GRAY, self.sampleRect)
