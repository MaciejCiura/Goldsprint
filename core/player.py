import pygame
from util.constant import Screen


class Player:
    def __init__(self, player_id, name):
        self.id = player_id
        self.name = name
        self.distance = 0
        self.speed = 0
        self.time = None
        self.racing = False
        self.won = False

    def update(self):
        # get distance from sensor
        if self.distance >= Screen.MAX_DISTANCE - 200:  # TODO change to dynamic distance parameter
            if self.racing:
                self.racing = False
                self.time = pygame.time.get_ticks() - self.time

    def log(self, timestamp, speed, distance):
        pass

    def set_name(self, name):
        self.name = name

    def set_time(self, time):
        self.time = time

    def check_win(self):
        return

    def move(self, distance):
        self.distance = distance

    def draw(self, screen):
        screen.blit(self.placeholder, (self.x + self.distance / 1, self.y))
        self.progressbar.draw(screen)
        self.time_txt.draw(screen)
        self.speed_txt.draw(screen)
        self.name_txt.draw(screen)