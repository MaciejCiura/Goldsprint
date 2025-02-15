import pygame
from ui.entities.entity import Entity
from ui.entities.text import Text
from ui.entities.progressbar import Progressbar
from util.constant import Bike, Colors


class PlayerView(Entity):
    def __init__(self, player, x, y, color):
        super().__init__(x=x, y=y,
                         height=Bike.BIKE_HEIGHT, width=Bike.BIKE_WIDTH, color=Colors.BLACK)
        self.player = player
        self.color = color
        self.placeholder = None
        self.name_txt = None
        self.speed_txt = None
        self.time_txt = None
        self.progressbar = Progressbar(self)
        self._set_player_view()
        self._set_text()

    def _set_player_view(self):
        self.placeholder = pygame.Surface((self.width, self.height))
        if self.player.is_winner:
            self.placeholder.fill(Colors.GOLD)
        else:
            self.placeholder.fill(self.color)

    def _set_text(self):
        self.name_txt = Text(text=self.player.player.name, x=self.x, y=self.y + 50, font_size=32)
        self.speed_txt = Text(text=str(self.player.speed), x=self.x, y=self.y + 110)
        self.time_txt = Text(text=str(self.player.finish_time), x=self.x, y=self.y + 120)
        self.name_txt.visible = True
        self.speed_txt.visible = False
        self.time_txt.visible = False

    def update(self):
        self.progressbar.update()
        if not self.player.is_racing:
            self._set_player_view()
            self.time_txt.set(str(self.player.finish_time), visible=True)

    def draw(self, screen):
        screen.blit(self.placeholder, (self.x + self.player.distance / 1, self.y))
        self.progressbar.draw(screen)
        self.time_txt.draw(screen)
        self.speed_txt.draw(screen)
        self.name_txt.draw(screen)
