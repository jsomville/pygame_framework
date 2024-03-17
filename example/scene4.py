#!/usr/bin/env python3
import pygame

from pygame_framework import Scene, UI_Button, UI_Position, UI_Size
from pygame_framework.Scene import Scene
from pygame_framework.UI_Button import UI_Button
from pygame_framework.UI_Size import UI_Size
from pygame_framework.UI_Position import UI_Position
from pygame_framework.Colors import Colors
from pygame_framework.Util import Util

class scene4(Scene):
    def on_init(self):
        self.name = "Scene 4"
        self.inited = True

        #Redefinie Background color
        self.BACKGROUND = Colors.BLACK

        #Title
        self.title = "This shows how to use UI_Buttons"
        self.title_font = pygame.font.SysFont("Arial", 24)

        self.addButtons()

        self.inited = True

    def addButtons(self):
        button_with = 180
        button_height = 30
        spacer_y = 20
        base_x = 300
        base_y = 100

        font = pygame.font.SysFont("Arial", 14)

        #Add buttons
        x = base_x
        y = base_y
        btn1 = UI_Button("Button 1")
        btn1["text"] = "Standard Button"
        btn1["font"] = font
        btn1["position"] = UI_Position(x,y)
        btn1["size"] = UI_Size(button_with, button_height)
        btn1["border_radius"] = 0
        btn1["back_color"] = Colors.GRAY
        btn1["hover_back_color"] = Colors.DARK_GRAY
        btn1["fore_color"] = Colors.WHITE
        self.addControl(btn1)

        #Add buttons
        x = base_x
        y = base_y + (button_height + spacer_y)
        btn2 = UI_Button("Button 2")
        btn2["text"] = "Button with round radius"
        btn2["font"] = font
        btn2["position"] = UI_Position(x,y)
        btn2["size"] = UI_Size(button_with, button_height)
        btn2["border_radius"] = 5
        btn2["back_color"] = Colors.GRAY
        btn2["hover_back_color"] = Colors.ORANGE
        btn2["fore_color"] = Colors.WHITE
        self.addControl(btn2)

        #Add buttons
        x = base_x
        y = base_y + (button_height + spacer_y) * 2
        btn3 = UI_Button("Return")
        btn3["text"] = "Return to menu"
        btn3["font"] = font
        btn3["position"] = UI_Position(x,y)
        btn3["size"] = UI_Size(button_with, button_height)
        btn3["border_radius"] = 5
        btn3["back_color"] = Colors.GRAY
        btn3["hover_back_color"] = Colors.ORANGE
        btn3["fore_color"] = Colors.WHITE
        self.addControl(btn3)

    def on_event(self, event):
        self.event_controls(event)

        #Handle the Button click
        if event.type == pygame.USEREVENT + 1:
            if hasattr(event, "UI_Event"):
                if event.UI_Event == "Button 1_click":
                    print("Clicked on Button 1")
                elif event.UI_Event == "Button 2_click":
                    print("Clicked on Button 2")
                elif event.UI_Event == "Return_click":
                    print("Clicked on Return Button")
                    self.fire_goto_event("menu")



    def on_loop(self):
        pass
       
    def on_render(self, surface):
        surface.fill(self.BACKGROUND)

        #Draw Title on center surface x
        Util().draw_text_center_x(surface, self.title, self.title_font, Colors.BLACK, 15)

        #Render Controls
        self.render_controls(surface)



