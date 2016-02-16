from objects import *
from colors import *
import pygame

class entity():

    def __init__(self, name, x, y, img):
        self.name = name
        self.x = x
        self.y = y
        self.img = img

    def getName(self):
        return name

    def getPos(self):
        return [self.x, self.y]

    def getImage(self):
        return self.img
