""" Classes of the snake game """
import pygame
from pygame.locals import *
from random import randint
import math

Pi = math.pi

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

    def __init__(self, size, center, shield_angle, limit):
        super().__init__()
        # Own attributes
        self.center = center
        self.last_move = 0
        self.x = center[0]
        self.y = center[1]
        self.size = size
        self.shield_box = pygame.Rect(self.x-self.size, self.y-self.size, 2*size, 2*size)
        self.radius = 25
        self.shield_angle = shield_angle
        self.shields = []
        for x in range(0,360,shield_angle):
                adj = math.cos(x*Pi/180) * self.radius
                opp = math.sin(x*Pi/180) * self.radius
                self.shields.append(((self.x+adj, self.y+opp)))

        self.In_danger = False
        self.angle = 0
        self.speed = 0
        self.limit = limit


    def __repr__(self):
        print("Player is in danger ? {} ".format(self.In_danger))


    def draw_player(self, screen):
        pygame.draw.rect(screen, colors['aqua'], self.shield_box, 2)
        pygame.draw.circle(screen, colors['red'], (int(self.x), int(self.y)), self.size)

    def draw_lines(self, screen):
        for shield in self.shields:
            pygame.draw.line(screen, colors['blue'], self.center, shield)

    def update_borders(self):
        self.shield_box = pygame.Rect(self.x-self.size, self.y-self.size, 2*self.size, 2*self.size)
        r = self.radius
        self.shields = []
        for x in range(0,360, self.shield_angle):
            adj = math.cos((x-self.angle)*Pi/180) * r
            opp = math.sin((x-self.angle)*Pi/180) * r
            self.shields.append(((self.x+adj, self.y+opp)))

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
        if pressed[pygame.K_UP]: self.speed += speed/30
        if pressed[pygame.K_DOWN]: self.speed -= speed/30

        self.y += self.speed * math.cos(self.angle * math.pi/180)
        self.x += self.speed * math.sin(self.angle * math.pi/180)
        self.center = (self.x , self.y)
        self.update_borders()

    def move_joystick_test(self, speed = 0, sensibility = 3):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: self.angle += sensibility
        if pressed[pygame.K_RIGHT]: self.angle -= sensibility
        if pressed[pygame.K_UP]: self.speed += speed/30
        if pressed[pygame.K_DOWN]: self.speed -= speed/30

        self.y += self.speed * math.cos(self.angle * math.pi/180)
        self.x += self.speed * math.sin(self.angle * math.pi/180)
        # print(self.x, self.y, self.angle, self.speed)
        self.center = (self.x , self.y)
        self.update_borders()


    def out_of_boundaries(self, screen):
        dangers = [self.shield_box.topleft, self.shield_box.midtop, self.shield_box.topright,
                    self.shield_box.midright, self.shield_box.bottomright, self.shield_box.midbottom,
                    self.shield_box.bottomleft, self.shield_box.midleft]
        for d in dangers:
            if screen.get_at(d) == (0, 0, 0, 255): # black pixel
                return True
        
        return False
