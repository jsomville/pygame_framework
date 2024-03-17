
import pygame
from .UI_Control import UI_Control
from .MenuObjectType import MenuObjectType
from .UI_Size import UI_Size
from .UI_Position import UI_Position
from .Colors import Colors

class UI_Button(UI_Control):

    def __init__(self, name):
        super(self.__class__, self).__init__(name)
        
        print("init UI_Button")

        self["type"] = MenuObjectType.BUTTON
        self["mouse_down"] = False
        self["hover"] = False

    def on_init(self):

        #Click Event
        self.CLICK_EVENT = self["name"] + "_click"
        self["click_event"] = pygame.Event(pygame.USEREVENT + 1, UI_Event = self.CLICK_EVENT)

        mouse_down_offset = 2
        self["rect"] = pygame.Rect((self["position"].x, self["position"].y), (self["size"].width, self["size"].height)) 
        self["rect_pressed"] = pygame.Rect((self["position"].x +mouse_down_offset, self["position"].y + mouse_down_offset), (self["size"].width, self["size"].height)) 


    def on_render(self, surface):

        #Determine Rect
        rect = self["rect"] 
        if self["mouse_down"]:
            rect = self["rect_pressed"] 

        #Draw Background
        color = self["back_color"]
        if self["hover"]:
            color = self["hover_back_color"]
        pygame.draw.rect(surface, color, border_radius = self["border_radius"],  rect = rect)
                
        #Draw Border
        pygame.draw.rect(surface, self["fore_color"], width=1, border_radius = self["border_radius"], rect = rect)

        if "text" in self:
            text_surface =  self["font"].render(self["text"], False, self["fore_color"])
            text_rect = text_surface.get_rect()
            text_rect.center = rect.center
            surface.blit(text_surface, text_rect)


    def on_loop(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self["rect"].collidepoint(event.pos):
                self["hover"] = True
            else:
                self["hover"] = False
                self["mouse_down"] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self["rect"].collidepoint(event.pos):
                self["mouse_down"] = True
            else:
                self["mouse_down"] = False

        elif event.type == pygame.MOUSEBUTTONUP:
            if self["mouse_down"]:
                # This is a click
                self["mouse_down"] = False

                #Fire an event
                print("click on button")
                pygame.event.post(self["click_event"])

    
