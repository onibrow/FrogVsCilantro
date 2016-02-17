from entity import *
import pygame

class player(entity):

    def __init__(self, name, x, y, img, xb, yb):
        entity.__init__(self, name, x, y, img)
        self.x_bound, self.y_bound = xb, yb

    def move(self, left, right, up, down):
        if left:
            self.x = max(self.x - 5, 0)
        elif right:
            self.x = min(self.x + 5, self.x_bound - self.size[0])
        if up:
            self.y = max(self.y - 5, 0)
        elif down:
            self.y = min(self.y + 5, self.y_bound - self.size[1])
