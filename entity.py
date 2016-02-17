import pygame
from PIL import Image

class entity():

    def __init__(self, name, x, y, img):
        self.name = name
        self.x = x
        self.y = y
        self.img = pygame.image.load(img)
        self.size = Image.open(img).size

    def getName(self):
        return name

    def getPos(self):
        return (self.x, self.y)

    def getImage(self):
        return self.img

    def getCorners(self):
        top_right = (self.x + (self.size[0] // 2), self.y + (self.size[1] // 2))
        top_left = (self.x - (self.size[0] // 2), self.y + (self.size[1] // 2))
        bottom_right = (self.x + (self.size[0] // 2), self.y - (self.size[1] // 2))
        bottom_left = (self.x - (self.size[0] // 2), self.y - (self.size[1] // 2))

        return (top_right, top_left, bottom_right, bottom_left)

    @staticmethod
    def pointInArea(point, area):
        x = point[0] < area[0][0] and point[0] > area[1][0]
        y = point[1] < area[0][1] and point[1] > area[2][1]
        return x and y

    @staticmethod
    def areaInArea(a1, a2):
        x = True
        for i in a1.getCorners():
            x = x and pointIntArea(i, a2)
        for j in a2.getCorners():
            x = x and pointIntArea(j, a1)
        return x
                 
    def collide(self, other):
        return areaInArea(self.getCorners(), other.getCorners()) 
