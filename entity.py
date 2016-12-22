import pygame
from PIL import Image

class entity():

    def __init__(self, name, x, y, img):
        self.name = name
        self.x = x
        self.y = y
        self.img = pygame.image.load(img)
        self.size = Image.open(img).size
        self.hitScale = min(self.size[0], self.size[1]) * 0.1

    def getName(self):
        return name

    def getPos(self):
        return (self.x, self.y)

    def getImage(self):
        return self.img

    def getCorners(self):
        top_right = (self.x + self.size[0] - self.hitScale, self.y + self.hitScale)
        top_left = (self.getPos()[0] + self.hitScale, self.getPos()[1] + self.hitScale)
        bottom_right = (self.x + self.size[0] - self.hitScale, self.y + self.size[1] - self.hitScale)
        bottom_left = (self.x + self.hitScale, self.y + self.size[1] - self.hitScale)

        return (top_right, top_left, bottom_right, bottom_left)

    @staticmethod
    def pointInArea(point, area):
        x = point[0] < area[0][0] and point[0] > area[1][0]
        y = point[1] > area[0][1] and point[1] < area[2][1]
        return x and y

    @staticmethod
    def areaInArea(a1, a2):
        x = False
        for i in a1.getCorners():
            x = x or entity.pointInArea(i, a2.getCorners())
        for j in a2.getCorners():
            x = x or entity.pointInArea(j, a1.getCorners())
        return x

    def collide(self, other):
        return entity.areaInArea(self, other)
