from objects import *
from colors import *
import pygame

class player:

    player_image = pygame.image.load("player.png")

    def __init__(self, health, x, y):
        self.health = health
        self.x = x
        self.y = y

    def getImage(self):
        return self.player_image 

    def getPos(self):
        return [self.x, self.y]

    def move(self, left, right, up, down):
        if left:
            self.x -= 5
        elif right:
            self.x += 5
        if up:
            self.y -= 5
        elif down:
            self.y += 5

    def damage(self, d):
        self.health -= d
