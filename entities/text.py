import pygame
from entities.entity import Entity
from util.constant import Colors, Screen
from util.position import Position


class Text(Entity):
    def __init__(self, text: str = "Default text", x=0 , y=0, font: pygame.font.Font = None):
        super().__init__(x, y)
        self.text = text
        if font is None:
            font = pygame.font.Font(None, Screen.FONT_SIZE)
        self.font = font
        self.antialiasing = True
        self.colour = Colors.BLACK
        self.background = None
        self.img = self.font.render(self.text, self.antialiasing, self.colour, self.background)
        self.rect = self.img.get_rect(topleft=(self.x, self.y))

    def set(self, string):
        self.text = string
        self.img = self.font.render(self.text, self.antialiasing, self.colour, self.background)
        self.rect = self.img.get_rect(topleft=(self.x, self.y))

    def center(self):
        self.rect = self.img.get_rect(center=(Screen.SCREEN_WIDTH / 2, Screen.FONT_SIZE/2))

    def draw(self, screen):
        if self.visible:
            screen.blit(self.img, self.rect)
