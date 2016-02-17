from entity import *
import pygame
from Math import *

class cilantro(entity):

    def __init__(self, name, x, y, img1, img2, img3, vel, playerPos):
        entity.__init__(self, name, x, y, img1)
        self.img2 = pygame.image.load(img2)
        self.img3 = pygame.image.load(img3)
        self.velocity = vel
        self.angle = 0
        self.dest = playerPos
        self.xMove = 0
        self.yMove = 0

    def calcDisplace(self):
        x = self.dest[0] - self.getPos()[0]
        y = self.dest[1] - self.gotPos()[1] 
        x, y = x // min(x, y), y // min(x,y)
        self.xMove = x * self.velocity
        self.yMove = y * self.velocity 

    def move(self):
        self.x = self.x + self.xMove
        self.y = self.y + self.yMove
