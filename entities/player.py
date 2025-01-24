import pygame
from entities.entity import Entity
from entities.text import Text
from entities.progressbar import Progressbar
from util.constant import Bike, Colors, Screen


class Player(Entity):
    def __init__(self,
                 x=Screen.STARTING_POSITION, y=Screen.BIKE1_Y,
                 hight=Bike.BIKE_HEIGHT, width=Bike.BIKE_WIDTH,
                 color=Colors.BLACK):
        super().__init__(x, y, hight, width)
        self.name = None
        self.distance = 0
        self.speed = 0
        self.racing = False
        self.time = 0
        self.won = False
        self.color = color
        self.placeholder = pygame.Surface((self.width, self.height))
        self.placeholder.fill(color)
        self.progressbar = Progressbar(self)
        self.name_txt = Text(x=self.x, y=self.y + 60)
        self.time_txt = Text(x=self.x, y=self.y + 120)

    def update(self):
        # get distance from sensor
        if self.distance >= Screen.MAX_DISTANCE - 200:  # TODO change to dynamic distance parameter
            self.racing = False
        self.progressbar.update()

    def set_name(self, name):
        self.name = name

    def check_win(self):
        return

    def move(self, distance):
        self.distance += distance

    def draw(self, screen):
        screen.blit(self.placeholder, (self.x + self.distance / 1, self.y))
        if self.racing:
            self.progressbar.draw(screen)
        else:
            self.time_txt.draw(screen)
            self.name_txt.draw(screen)