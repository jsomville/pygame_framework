import pygame

class Util():

    def draw_text(self, surface, text, font, text_col, x, y):
        """Draw Text Function"""
        img = font.render(text, True, text_col)
        surface.blit(img, (x, y))
    
    def draw_text_center(self, surface, text, font, text_col):
        """Draw Text Centered"""
        x = surface.get_rect().width //2
        y = surface.get_rect().height //2
        img = font.render(text, True, text_col)
        text_rect = img.get_rect(center = (x,y))
        surface.blit(img, text_rect)

    def draw_text_center_x(self, surface, text, font, text_col, y):
        """Draw Text Centered"""
        x = surface.get_rect().width //2
        img = font.render(text, True, text_col)
        text_rect = img.get_rect(center = (x,y))
        surface.blit(img, text_rect)
    
    def draw_text_center_y(self, surface, text, font, text_col, x):
        """Draw Text Centered"""
        y = surface.get_rect().height //2
        img = font.render(text, True, text_col)
        text_rect = img.get_rect(center = (x, y))
        surface.blit(img, text_rect)