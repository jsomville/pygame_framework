#!/usr/bin/env python3
import pygame
from pygame.locals import *

from Colors import Colors
from Scene import Scene
import random


class Scene1(Scene):
    name = "Scene 1"

    rect_list = list()
    exit = False

    def __init__(self):
        Scene.__init__(self)

        pygame.font.init()

        #Set the background color
        self.BACKGROUND = Colors.BLACK

        #If font is not installed, use another one
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

        #Load Images
        self.image = pygame.image.load("images/pygame.png").convert_alpha()

    def on_event(self, event):

        if event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #Add a rectangle where clicked
                aRect = Rect(0, 0, 100, 100)
                aRect.center = event.pos
                self.rect_list.append(aRect)

                #Click on logo --> exit flag
                rect = self.image.get_rect()
                rect.center = self.center
                if rect.collidepoint(event.pos):
                    self.exit = True
            
        elif event.type == pygame.MOUSEBUTTONUP:
            pass

    def on_loop(self):

        # Handle shapes size modification
        for r in self.rect_list:
            c = r.center
            r.width -= 2
            r.height -= 2
            r.center = c
            if r.width < 4:
                self.rect_list.remove(r)

        #Exit flag
        if len(self.rect_list) == 0:
            if self.exit:
                self.next = None

    def on_render(self, surface):
        #Fill Background color
        surface.fill(self.BACKGROUND)

        #Draw pygame image
        img = self.image
        rect = img.get_rect()
        rect.center = self.center
        surface.blit(self.image, rect)

        #Draw pygame version
        version = 'Version : ' + str(pygame.version.ver)
        text_surface = self.myfont.render(version, False, Colors.WHITE)
        text_size = self.myfont.size(version)
        text_position = self.centerx - text_size[0]//2, self.centery + 30
        surface.blit(text_surface, text_position)

        #Display additional shapes
        for r in self.rect_list:
            #Generate Random Color
            c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            #Draw a circle for each shape
            pygame.draw.circle(surface, c, r.center, r.width)

        #Display update instruction
        rect = surface.get_rect()
        pygame.display.update(rect)
		