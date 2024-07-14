import pygame
from entities.progressbar import Progressbar
from util.position import Position
from util.constant import Bike, Colors, Screen


class Player:

    def __init__(self, color, position: Position, progressbar_position=None):
        self.position = position
        self.color = color
        self.width = Bike.BIKE_WIDTH
        self.height = Bike.BIKE_HEIGHT
        self.bike = pygame.Surface((self.width, self.height))
        self.bike.fill(color)
        self.name = None
        if progressbar_position is None:
            progressbar_position = Position(self.position.x, self.position.y + 80)
        self.progressbar = Progressbar(self.color, progressbar_position)

    def set_name(self, name):
        self.name = name

    def check_win(self):
        return self.position.x >= Screen.MAX_DISTANCE

    def move(self, pos_x, pos_y):
        self.position = Position(self.position.x + pos_x, min(self.position.y + pos_y, Screen.MAX_DISTANCE))
        self.progressbar.update(self.position.x)

    def display(self, screen):
        screen.blit(self.bike, (self.position.x, self.position.y))
        self.progressbar.display(screen)
