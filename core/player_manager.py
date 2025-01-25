import pygame
from util.constant import Bike


class PlayerManager:
    def __init__(self, players, data_handler):
        self.players = players
        self.start_time = pygame.time.get_ticks()
        self.data_handler = data_handler

    def update(self):
        '''
        if (!data_handler.empty())
            process frame
            read {[id: 0, distance, 100], [id: 1, distance, 120]}
            for player in self.players
                player.move(timestamp, distance)
            if both players passed max_distance

        '''
        for player in self.players:
            if player.racing:
                player.move(2)
            player.update()

    def start_race(self, time=None):
        for player in self.players:
            player.racing = True

        if time is not None:
            self.start_time = time
        self.players[0].set_time(self.start_time)
        self.players[1].set_time(self.start_time)

    def racing(self):
        return any(player.racing for player in self.players)

    def log_data(self, player_id, timestamp, speed, distance):
        if player_id in self.players:
            self.players[player_id].log(timestamp, speed, distance)

    def get_players(self):
        return self.players
