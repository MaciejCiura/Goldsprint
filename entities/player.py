import pygame
from entities.entity import Entity
from entities.text import Text
from entities.progressbar import Progressbar
from util.constant import Bike, Colors, Screen


class Player(Entity):
    def __init__(self, player_id, name, x=Screen.STARTING_POSITION, y=Screen.BIKE1_Y,
                 hight=Bike.BIKE_HEIGHT, width=Bike.BIKE_WIDTH, color=Colors.BLACK):
        super().__init__(x, y, hight, width)
        self.id = player_id
        self.name = name
        self.distance = 0
        self.speed = 0
        self.racing = False
        self.time = None
        self.won = False
        self.color = color
        self.placeholder = pygame.Surface((self.width, self.height))
        self.placeholder.fill(color)
        self.progressbar = Progressbar(self)
        self.name_txt = Text(text=name, x=self.x, y=self.y + 30)
        self.speed_txt = Text(x=self.x, y=self.y + 90)
        self.time_txt = Text(x=self.x, y=self.y + 120)
        self.name_txt.visible = True
        self.speed_txt.visible = False
        self.time_txt.visible = False
        self.log_data = None

    def update(self):
        # get distance from sensor
        if self.distance >= Screen.MAX_DISTANCE - 200:  # TODO change to dynamic distance parameter
            if self.racing:
                self.racing = False
                self.time = pygame.time.get_ticks() - self.time
                self.time_txt.set(str(self.time))
            self.progressbar.visible = False
            self.time_txt.visible = True
        self.progressbar.update()
        if self.won:
            self.placeholder.fill(Colors.GOLD)

    def log(self, timestamp, speed, distance):
        pass

    def set_name(self, name):
        self.name = name

    def set_time(self, time):
        self.time = time

    def check_win(self):
        return

    def move(self, distance):
        self.distance += distance

    def draw(self, screen):
        screen.blit(self.placeholder, (self.x + self.distance / 1, self.y))
        self.progressbar.draw(screen)
        self.time_txt.draw(screen)
        self.speed_txt.draw(screen)
        self.name_txt.draw(screen)