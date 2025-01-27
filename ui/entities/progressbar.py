import pygame

from ui.entities.entity import Entity
from util.constant import Screen


class Progressbar(Entity):
    def __init__(self, player_view, height=Screen.PROGRESSBAR_HEIGHT, width=Screen.PROGRESSBAR_WIDTH):
        super().__init__(player_view.x, player_view.y + 80, height, width)
        self.value = player_view.player.distance  # TODO change to %
        self.player_view = player_view

    def update(self):
        self.value = self.player_view.player.distance

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.player_view.color, (self.x, self.y, self.value + self.player_view.width, self.height))
