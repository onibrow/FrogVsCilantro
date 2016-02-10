import pygame
from colors import *

class objects:

    col = colors()

    def __init__(self):
        self.name = "tree"
         
    def draw_tree(self, screen, x, y):
        """Draws a tree in screen at position x, y"""
        pygame.draw.rect(screen, self.col.BROWN(), [60+x, 400+y, 30, 45])
        pygame.draw.polygon(screen, self.col.GREEN(), [[150+x, 400+y], [75+x, 250+y], [x, 400+y]])
        pygame.draw.polygon(screen, self.col.GREEN(), [[140+x, 350+y], [75+x, 230+y], [10+x, 350+y]])

    def draw_snowman(self, screen, x, y):
        """Draws a snowman in screen at position x, y"""
        pygame.draw.ellipse(screen, self.col.WHITE(), [35+x, 0+y, 25, 25])
        pygame.draw.ellipse(screen, self.col.WHITE(), [23+x, 20+y, 50, 50])
        pygame.draw.ellipse(screen, self.col.WHITE(), [0+x, 65+y, 100, 100])
