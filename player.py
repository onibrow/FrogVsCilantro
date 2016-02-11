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

    def move(self, x, y):
        self.x = x
        self.y = y

    def damage(self, d):
        self.health -= d
