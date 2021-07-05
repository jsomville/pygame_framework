#!/usr/bin/env python3

import pygame
from pygame.locals import *

from pygame_framework.MenuHOrientation import MenuHOrientation
from pygame_framework.MenuVOrientation import MenuVOrientation
from pygame_framework.MenuObjectType import MenuObjectType
from pygame_framework.MenuTheme import MenuTheme


class MenuUtil:
    BASE_MENU_OFFSET = 4
    TITLE_BAR_HEIGHT = 20
    CLICK_OFFSET = 2

    def __init__(self):
        self.theme = MenuTheme()

        self.menu_font = pygame.font.SysFont(self.theme["font"], 30)
        self.label_font = pygame.font.SysFont(self.theme["font"], 20)

    def on_init(self, window_size, menu, v_orientation, h_orientation):
        menu_pos = self.get_menu_position(window_size, len(menu), v_orientation, h_orientation)

        x_value = menu_pos[0]
        y_value = menu_pos[1]

        for control in menu:
            # Control Position
            control["rect"] = pygame.Rect((x_value, y_value), self.theme["base_size"])

            if control["type"] == MenuObjectType.TITLE:
                control["back_color"] = self.theme["title_back_color"]
                control["text_color"] = self.theme["title_text_color"]
                control["font"] = self.menu_font
            elif control["type"] == MenuObjectType.BUTTON:
                control["back_color"] = self.theme["btn_back_color"]
                control["text_color"] = self.theme["btn_text_color"]
                control["font"] = self.menu_font
                control["mouse_down"] = False
                control["click"] = False
            elif control["type"] == MenuObjectType.LABEL:
                control["back_color"] = self.theme["lbl_back_color"]
                control["text_color"] = self.theme["lbl_text_color"]
                control["font"] = self.label_font
            elif control["type"] == MenuObjectType.CONTAINER:
                control["back_color"] = self.theme["lbl_back_color"]
                control["text_color"] = self.theme["lbl_text_color"]

            y_value += self.theme["base_size"][1] + 4

    def get_menu_position(self, window_size, menu_control_count, v_orientation, h_orientation):

        control_width = self.theme["base_size"][0]
        control_height = self.theme["base_size"][1]

        menu_height = menu_control_count * control_height
        center_x = window_size[0] // 2
        center_y = window_size[1] // 2

        y_start = 0
        if v_orientation == MenuVOrientation.TOP:
            y_start = self.BASE_MENU_OFFSET
        elif v_orientation == MenuVOrientation.CENTER:
            y_start = center_y - menu_height // 2
        elif v_orientation == MenuVOrientation.BOTTOM:
            y_start = window_size[1] - menu_height - MenuUtil.BASE_MENU_OFFSET  # 20 for space of Title Bar

        x_start = 0
        if h_orientation == MenuHOrientation.LEFT:
            x_start = MenuUtil.BASE_MENU_OFFSET
        if h_orientation == MenuHOrientation.CENTER:
            x_start = center_x - control_width // 2
        if h_orientation == MenuHOrientation.RIGHT:
            x_start = window_size[0] - control_width - self.BASE_MENU_OFFSET

        return x_start, y_start

    def on_event(self, event, menu):
        if event.type == pygame.MOUSEMOTION:
            for control in menu:
                if control["type"] == MenuObjectType.BUTTON:
                    if control["rect"].collidepoint(event.pos):
                        control["hover"] = True
                        control["back_color"] = self.theme["btn_back_hover_color"]
                    else:
                        control["hover"] = False
                        control["mouse_down"] = False
                        control["back_color"] = self.theme["btn_back_color"]

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for control in menu:
                if control["type"] == MenuObjectType.BUTTON:
                    if control["rect"].collidepoint(event.pos):
                        control["mouse_down"] = True
                    else:
                        control["mouse_down"] = False

        if event.type == pygame.MOUSEBUTTONUP:
            for control in menu:
                if control["type"] == MenuObjectType.BUTTON:
                    if control["mouse_down"]:
                        # This is a click
                        control["mouse_down"] = False
                        control["click"] = True

    def draw_menu(self, surface, menu):
        for control in menu:

            # Handle Click
            control_center = control["rect"].center
            if control["type"] == MenuObjectType.BUTTON:
                if control["mouse_down"]:
                    control_center = (control_center[0] + self.CLICK_OFFSET, control_center[1] + self.CLICK_OFFSET)

            # Draw background
            pygame.draw.rect(surface, control["back_color"], control["rect"])

            # Draw Text
            if "text" in control:
                text = control["text"]
                text_surface =  control["font"].render(text, False, control["text_color"])
                text_rect = text_surface.get_rect()
                text_rect.center = control_center
                surface.blit(text_surface, text_rect)
