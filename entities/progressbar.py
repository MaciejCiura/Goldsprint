import pygame

from util.constant import Screen
from util.position import Position


class Progressbar:
    def __init__(self, color, position: Position):
        self.height = Screen.PROGRESSBAR_HEIGHT
        self.width = Screen.PROGRESSBAR_WIDTH
        self.position = position
        self.value = position.x
        self.color = color

    def update(self, value):
        self.value = value

    def display(self, screen):
        pygame.draw.rect(screen, self.color, (self.position.x, self.position.y, self.value, self.height))
