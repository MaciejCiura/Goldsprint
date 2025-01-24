import pygame
from util.constant import Colors

class Entity:
    def __init__(self, x=0, y=0, height=10, width=10, color=Colors.BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.active = True
        self.visible = True

    def update(self):
        pass

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))