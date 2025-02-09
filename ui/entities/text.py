import pygame
from ui.entities.entity import Entity
from util.constant import Colors, Screen


class Text(Entity):
    def __init__(self, text: str = "Default text", x=0 , y=0, font_size=None):
        super().__init__(x, y)
        self.text = text
        if not font_size:
            font_size = Screen.FONT_SIZE
        font = pygame.font.Font(None, font_size)
        self.font = font
        self.antialiasing = True
        self.colour = Colors.BLACK
        self.background = None
        self.img = self.font.render(self.text, self.antialiasing, self.colour, self.background)
        self.rect = self.img.get_rect(topleft=(self.x, self.y))

    def set(self, string, visible=True):
        self.text = string
        self.img = self.font.render(self.text, self.antialiasing, self.colour, self.background)
        self.rect = self.img.get_rect(topleft=(self.x, self.y))
        self.visible = visible

    def center(self):
        self.rect = self.img.get_rect(center=(Screen.SCREEN_WIDTH / 2, Screen.FONT_SIZE/2))

    def draw(self, screen):
        if self.visible:
            screen.blit(self.img, self.rect)
