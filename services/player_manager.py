import pygame


class PlayerManager:
    def __init__(self, players):
        self.players = players
        self.start_time = pygame.time.get_ticks()

    def update(self):
        for player in self.players:
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
