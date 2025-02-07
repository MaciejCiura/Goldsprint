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

    def reset(self):
        self.distance = 0
        self.speed = 0
        self.time = None
        self.racing = False
        self.won = False

    def move(self, distance):
        self.distance = distance

    def set_name(self, name):
        self.name = name

    def set_time(self, time):
        self.time = time

    def __repr__(self):
        return f"Player(id={self.id}, name='{self.name}', distance={self.distance}, speed={self.speed}, time={self.time})"

    def __str__(self):
        return f"Player {self.id}: {self.name} | Distance: {self.distance}m | Speed: {self.speed} m/s | Time: {self.time}s"