import pygame
from colors import *

class stickman:

    col = colors()

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self, screen, x, y):
        # Head
        pygame.draw.ellipse(self.screen, self.col.BLACK(), [1+x,y,10,10], 0)
     
        # Legs
        pygame.draw.line(self.screen, self.col.BLACK(),[5+x,17+y], [10+x,27+y], 2)
        pygame.draw.line(self.screen, self.col.BLACK(), [5+x,17+y], [x,27+y], 2)
     
        # Body
        pygame.draw.line(self.screen, self.col.RED(), [5+x,17+y], [5+x,7+y], 2)
     
        # Arms
        pygame.draw.line(self.screen, self.col.RED(), [5+x,7+y], [9+x,17+y], 2)
        pygame.draw.line(self.screen, self.col.RED(), [5+x,7+y], [1+x,17+y], 2)

    def move(self, left, right, up, down):
        if left:
            self.x -= 5
        elif right:
            self.x += 5
        if up:
            self.y -= 5
        elif down:
            self.y += 5
