import pygame
from util.constant import Colors, Screen
from util.position import Position


class Text:
    def __init__(self, text: str = "Default text", position: Position = None, font: pygame.font.Font = None):
        self.text = text
        if position is None:
            position = Position(0, 0)
        self.position = position
        if font is None:
            font = pygame.font.Font(None, Screen.FONT_SIZE)
        self.font = font
        self.antialiasing = True
        self.colour = Colors.BLACK
        self.background = None
        self.img = self.font.render(self.text, self.antialiasing, self.colour, self.background)
        self.rect = self.img.get_rect(topleft=(self.position.x, self.position.y))

    def center(self):
        self.rect = self.img.get_rect(center=(Screen.SCREEN_WIDTH / 2, Screen.FONT_SIZE/2))

    def blit(self, screen):
        screen.blit(self.img, self.rect)
