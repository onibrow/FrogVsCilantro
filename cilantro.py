from entity import *
import pygame
import math
import random


class cilantro(entity):

    def __init__(self, name, x, y, img1, img2, img3, vel, playerPos, maxX, maxY):
        entity.__init__(self, name, x, y, img1)
        self.img1 = pygame.image.load(img1)
        self.img2 = pygame.image.load(img2)
        self.img3 = pygame.image.load(img3)
        self.maxX = maxX
        self.maxY = maxY
        self.velocity = vel
        self.origX = self.x
        self.origY = self.y
        self.angle = 0
        self.dest = playerPos
        self.xMove, self.ymove = 0, 0
        self.which_image = 0
        x = self.dest[0] - self.getPos()[0] + 0.1
        y = self.dest[1] - self.getPos()[1] + 0.1
        norm = math.sqrt(x * x + y * y)
        rads = math.atan2(-y,x)
        rads %= 2*math.pi
        self.angle = 0
        self.xMove = x * self.velocity
        self.yMove = y * self.velocity

    def move(self):
        self.which_image += 1
        self.selectImage()
        self.x = self.x + self.xMove
        self.y = self.y + self.yMove

    def selectImage(self):
        if self.which_image % 48 == 0:
            self.img = pygame.transform.rotate(self.img1, -self.angle)
        elif self.which_image % 24 == 0:
            self.img = pygame.transform.rotate(self.img2, -self.angle)
        elif self.which_image % 12 == 0:
            self.img = pygame.transform.rotate(self.img3, -self.angle)

    def refresh(self, playerPos):
        if (self.x < 0 or self.x > self.maxX or self.y < 0 or self.y > self.maxY):
            self.x, self.y = self.origX, self.origY
            self.velocity = random.randrange(3, 8)
            x = playerPos[0] - self.getPos()[0] + 0.1
            y = playerPos[1] - self.getPos()[1] + 0.1
            norm = math.sqrt(x * x + y * y)
            x, y = x / norm, y / norm
            self.xMove = x * self.velocity
            self.yMove = y * self.velocity

    def setVelocity(self, velocity):
        self.velocity = velocity
