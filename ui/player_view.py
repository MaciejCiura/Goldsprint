import pygame
from ui.entity import Entity
from ui.text import Text
from ui.progressbar import Progressbar
from util.constant import Bike, Colors, Screen


class PlayerView(Entity):
    def __init__(self, player, x, y, color):
        super().__init__(x=x, y=y,
                         height=Bike.BIKE_HEIGHT, width=Bike.BIKE_WIDTH, color=Colors.BLACK)
        self.player = player
        self.color = color
        self.placeholder = pygame.Surface((self.width, self.height))
        self.placeholder.fill(color)
        self.progressbar = Progressbar(self)
        self.name_txt = Text(text=self.player.name, x=self.x, y=self.y + 30)
        self.speed_txt = Text(x=self.x, y=self.y + 90)
        self.time_txt = Text(x=self.x, y=self.y + 120)
        self.name_txt.visible = True
        self.speed_txt.visible = False
        self.time_txt.visible = False

    def update(self):
        # get distance from sensor
        if self.player.racing:
            self.progressbar.update()
        else:
            self.progressbar.visible = False
            self.time_txt.set(str(self.player.time))
            self.time_txt.visible = True
            if self.player.won:
                self.placeholder.fill(Colors.GOLD)

    def draw(self, screen):
        screen.blit(self.placeholder, (self.x + self.player.distance / 1, self.y))
        self.progressbar.draw(screen)
        self.time_txt.draw(screen)
        self.speed_txt.draw(screen)
        self.name_txt.draw(screen)