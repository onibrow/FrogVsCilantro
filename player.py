from entity import *
import pygame

class player(entity):

    def __init__(self, name, x, y, img, img2, img3, img4, xb, yb):
        entity.__init__(self, name, x, y, img)
        self.img2 = pygame.image.load(img2)
        self.front1, self.front2 = pygame.image.load(img), pygame.image.load(img2)
        self.back1, self.back2 = pygame.image.load(img3), pygame.image.load(img4)
        self.x_bound, self.y_bound = xb, yb
        self.isMovingForward, self.isMovingBack, self.movecount = False, False, 0
        self.which_image = 1

    def move(self, left, right, up, down):
        self.isMovingForward, self.isMovingBack = False, False

        if left:
            self.x = max(self.x - 3, 0)
            self.isMovingForward = True
        elif right:
            self.x = min(self.x + 3, self.x_bound - self.size[0])
            self.isMovingForward = True
        if up:
            self.y = max(self.y - 3, 0)
            self.isMovingBack = True
        elif down:
            self.y = min(self.y + 3, self.y_bound - self.size[1])
            self.isMovingForward = True

    def toggleImage(self):
        if self.isMovingBack:
            self.img, self.img2 = self.back1, self.back2
            self.movecount += 1
            if self.movecount > 16:
                self.which_image *= -1
                self.movecount = 0
        elif self.isMovingForward:
            self.img, self.img2 = self.front1, self.front2
            self.movecount += 1
            if self.movecount > 16:
                self.which_image *= -1
                self.movecount = 0
        else:
            self.which_image = 1

    def getImage(self):
        self.toggleImage()
        if self.which_image == 1:
            return self.img
        else:
            return self.img2
