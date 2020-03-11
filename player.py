""" Classes of the snake game """
import pygame
from pygame.locals import *
from random import randint
import math

colors = {'black':(0,0,0),
'white':(255,255,255),
'gray':(128,128,128),
'aqua':(0,128,128),
'navy blue':(0,0,128),
'green':(0,255,0),
'orange':(255,165,0),
'yellow':(255,255,0),
'red':(255,0,0),
'blue':(0,0,255)}


class Player(pygame.sprite.Sprite):

    def __init__(self, size, center):
        super().__init__()
        # Own attributes
        self.center = center
        self.last_move = 0
        self.x = center[0]
        self.y = center[1]
        self.rect = pygame.Rect(self.x, self.y, size/2, size)
        self.size = (int(size/2), int(size))
        self.shield_down = (self.x, self.y + 100)
        self.shield_up = (self.x, self.y - 100)
        self.shield_left = (self.x - 100, self.y)
        self.shield_right = (self.x + 100, self.y)
        self.In_danger = False
        self.angle = 0

    def __repr__(self):
        print("Player is in danger ? {} ".format(self.In_danger))


    def draw_player(self, screen):
        pygame.draw.circle(screen, colors['red'], (int(self.x), int(self.y)), 15)

    def draw_lines(self, screen):
        pygame.draw.line(screen, colors['red'], self.center, self.shield_down)
        pygame.draw.line(screen, colors['blue'], self.center, self.shield_up)
        pygame.draw.line(screen, colors['blue'], self.center, self.shield_right)
        pygame.draw.line(screen, colors['blue'], self.center, self.shield_left)


    def update_borders(self):
        cos_y = 100 * math.cos(self.angle * math.pi/180)
        tan_x = math.tan(self.angle * math.pi/180)
        self.shield_down = (self.x + cos_y * tan_x, self.y + cos_y)
        self.shield_up = (self.x - cos_y * tan_x, self.y - cos_y)
        self.shield_right = (self.x + cos_y , self.y - cos_y * tan_x)
        self.shield_left = (self.x - cos_y , self.y + cos_y * tan_x)


    def move_arrows(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: self.y -= 5
        if pressed[pygame.K_DOWN]: self.y += 5
        if pressed[pygame.K_LEFT]: self.x -= 5
        if pressed[pygame.K_RIGHT]: self.x += 5
        self.center = (self.x, self.y)
        self.update_borders()

    def move_joystick(self, speed = 5, sensibility = 3):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: self.angle += sensibility
        if pressed[pygame.K_RIGHT]: self.angle -= sensibility
        self.y += speed * math.cos(self.angle * math.pi/180)
        self.x += speed * math.sin(self.angle * math.pi/180)
        self.center = (self.x , self.y)
        self.update_borders()

    def out_of_boundaries(self):
        if self.x < 0 or self.y < 0 or self.y > 800 or self.x > 800:
            return True
        else:
            return False

