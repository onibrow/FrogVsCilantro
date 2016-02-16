from entity import *
from objects import *
from colors import *
import pygame

class player(entity):

    def __init__(self, name, x, y, img):
        entity.__init__(self, name, x, y, img)

    def move(self, left, right, up, down):
        if left:
            self.x -= 5
        elif right:
            self.x += 5
        if up:
            self.y -= 5
        elif down:
            self.y += 5
