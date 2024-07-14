import pygame


class Position(pygame.Vector2):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'({self.x}, {self.y})'
