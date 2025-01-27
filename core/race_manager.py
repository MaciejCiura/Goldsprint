import time
from core.player import Player


class RaceManager:
    def __init__(self, players=None, finish_distance=500):
        if players is None:
            players = {0: Player(0, "Player_1"), 1: Player(1, "Player_2")}
        self.players = players
        self.finish_distance = finish_distance
        self.start_time = None
        self.race_in_progress = False
        self.winners = None

    def setup(self, player_name_1, player_name_2, finish_distance=None):
        if finish_distance is not None:
            self.finish_distance = finish_distance
        players = {0: Player(0, player_name_1), 1: Player(1, player_name_2)}
        self.players = players
        self.start_time = None
        self.race_in_progress = False
        self.winners = None

    def countdown(self):
        # countdown_time = time.time()
        #
        # while True:
        #     data = self.data_handler.get_data()
        #     if data and data["players"][0]["distance"] != 0 and data["players"][1]["distance"] !=0:
        #         print("FALSTART", data)
        #     else:
                pass

    def add_player(self, player):
        if player.id in self.players:
            raise ValueError(f"Player with id {player.id} already exists.")
        self.players[player.id] = player

    def start_race(self):
        self.race_in_progress = True
        for player in self.players.values():
            player.distance = 0
            player.racing = True
            player.won = False
        self.start_time = time.time()

    def update(self, data):
        players_data = data["players"]
        for player_data in players_data:
            player = self.players[player_data["id"]]
            if player.racing:
                player.move(player_data["distance"])
                if player.distance >= self.finish_distance:  # TODO change to dynamic distance parameter
                    player.move(self.finish_distance - player.distance)
                    player.racing = False
                    player.time = time.time() - self.start_time
                    if not any(winner.won for winner in self.players.values()):
                        player.won = True

        self._finish_race()

    def _finish_race(self):
        if self.race_in_progress:
            if all(not player.racing for player in self.players.values()):
                min_time = min(player.time for player in self.players.values() if player.time is not None)
                self.winners = [
                    player for player in self.players.values() if player.time == min_time
                ]
                for winner in self.winners:
                    winner.won = True
                self.race_in_progress = False

    def racing(self):
        return any(player.racing for player in self.players.values())

    def get_players(self):
        return self.players.values

    def get_winners(self):
        return self.winners



