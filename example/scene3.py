import random
import pygame

from pygame_framework.Scene import Scene
from pygame_framework.Colors import Colors
from pygame_framework.Util import Util

class Point():
    x : int
    y : int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return (self.x == other .x) and (self.y == other.y)

class scene3(Scene):
    def on_init(self):
        self.name = "Scene 3"
        self.counter = 0

        self.grid = Point(80, 80)
        self.block_lenght = 5
        
        x = (self.width - (self.grid.x * self.block_lenght)) // 2
        y = (self.height - (self.grid.y * self.block_lenght)) // 2
        self.offset = Point(x, y)

        self.reset_snake()

        self.snake_color = Colors.RED

        self.game_over = False
        self.counter = 0
        self.game_over_counter_max = 30
        self.level = 0

        self.generate_target()

        #Redefinie Background color
        self.BACKGROUND = Colors.DARK_GRAY

        #Title
        self.title = "Dont hit the wall or your tail !"
        self.title_font = pygame.font.SysFont("Arial", 24)

        self.inited = True

    def reset_snake(self):
        start_x = self.grid.x //2
        start_y = self.grid.y //2
        self.snake_lenght = 5
        self.snake_direction = "RIGHT"
        self.snake = list()
        for i in range(self.snake_lenght):
            p = Point(start_x - i, start_y)
            self.snake.append(p)

    def move_snake(self):
        
        #Index previous positions
        for i in range(self.snake_lenght - 1, 0, -1):
            self.copy_values(i, i-1)

        #Get new position
        if self.snake_direction == "RIGHT":
            self.snake[0].x += 1
        elif self.snake_direction == "LEFT":
            self.snake[0].x -= 1
        elif self.snake_direction == "UP":
            self.snake[0].y -= 1
        elif self.snake_direction == "DOWN":
            self.snake[0].y += 1

    def copy_values(self, a,b):
        self.snake[a].x = self.snake[b].x
        self.snake[a].y = self.snake[b].y

    def on_event(self, event):
        if event.type == pygame.USEREVENT:
            #Switch scene event
            if "goto" in event.__dict__:
                self.reset_snake()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.snake_direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                self.snake_direction = "RIGHT"
            if event.key == pygame.K_UP:
                self.snake_direction = "UP"
            if event.key == pygame.K_DOWN:
                self.snake_direction = "DOWN"
            if event.key == pygame.K_SPACE:
                self.grow_snake(3)
            if event.key == pygame.K_ESCAPE:
                self.fire_goto_event("menu")

    def on_loop(self):
        if not self.game_over:
            #Move snake
            self.move_snake()

            #Check if out of board
            p = self.snake[0]
            if p.x < 0 or p.x > self.grid.x:
                self.set_game_over()
            elif p.y < 0 or p.y > self.grid.y:
                self.set_game_over()

            #Check if snake is within himself
            check = self.snake[1 :self.snake_lenght-1]
            print("***")
            #print(self.snake[0])
            print(check)
            if self.snake[0] in check:
                self.set_game_over()
                
            #Check if target is reached
            if self.snake[0] == self.target:
                print("target reached")
                self.level += 1
                self.generate_target()
                self.grow_snake(3)
                
        else:
            self.counter += 1
            if self.counter > self.game_over_counter_max:
                self.fire_goto_event("menu")

    def set_game_over(self):
        print("Game over")
        self.game_over = True
        self.counter = 0

    def grow_snake(self, lenght):
        last_point = self.snake[self.snake_lenght -1]
        for i in range(lenght):
            p = Point(last_point.x, last_point.y)
            self.snake.append(p)
        
        self.snake_lenght += lenght

    def generate_target(self):
        x = random.randint(1, self.grid.x - 1)
        y = random.randint(1, self.grid.y - 1)
        self.target = Point(x,y)
        print(self.target)

    def on_render(self, surface):
        surface.fill(self.BACKGROUND)

        #Draw Title on center surface x
        Util().draw_text_center_x(surface, self.title, self.title_font, Colors.BLACK, 15)

        #Draw Title on center surface x
        level = "Level :" + str(self.level)
        Util().draw_text_center_y(surface, level, self.title_font, Colors.BLACK, 60)

        #Draw grid
        width = self.grid.x * self.block_lenght
        height = self.grid.y * self.block_lenght
        r = pygame.Rect(self.offset.x, self.offset.y, width, height)
        pygame.draw.rect(surface, Colors.LIGHT_GRAY, r)

        #Draw Snake
        for i in range(self.snake_lenght):
            x = self.offset.x + self.snake[i].x * self.block_lenght
            y = self.offset.y + self.snake[i].y * self.block_lenght
            r = pygame.Rect(x, y, self.block_lenght, self.block_lenght)
            pygame.draw.rect(surface, self.snake_color, r)
        
        #Draw Target
        x = self.offset.x + self.target.x * self.block_lenght
        y = self.offset.y + self.target.y * self.block_lenght
        r = pygame.Rect(x, y, self.block_lenght, self.block_lenght)
        pygame.draw.rect(surface, Colors.GREEN, r)

        if self.game_over:
             Util().draw_text_center(surface, "Game Over !!", self.title_font, Colors.BLACK)
        