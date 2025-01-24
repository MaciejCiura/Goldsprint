import pygame

from entities.entity import Entity
from util.constant import Screen


class Progressbar(Entity):
    def __init__(self, player, height=Screen.PROGRESSBAR_HEIGHT, width=Screen.PROGRESSBAR_WIDTH):
        super().__init__(player.x, player.y + 80, height, width)
        self.value = player.distance  # TODO change to %
        self.player = player

    def update(self):
        self.value = self.player.distance

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.player.color, (self.x, self.y, self.value + self.player.width, self.height))
