import time


class RaceManager:
    def __init__(self, players=None, finish_distance=500):
        self.players = players
        self.finish_distance = finish_distance
        self.start_time = None
        self.race_active = False
        self.winner = None

    def add_player(self, player):
        if player.id in self.players:
            raise ValueError(f"Player with id {player.id} already exists.")
        self.players[player.id] = player

    def start_race(self):
        self.race_active = True
        for player in self.players.values():
            player.distance = 0
            player.racing = True
            player.won = False
            self.winner = player
        self.start_time = time.time()

    def handle_data(self, player_id, distance):
        player = self.players[player_id]
        if player.distance >= self.finish_distance:  # TODO change to dynamic distance parameter
            if player.racing:
                player.racing = False
                player.time = time.time() - self.start_time

        if player.racing:
            player.move(distance)

        if not self.racing():
            if all(not player.racing for player in self.players.values()):
                winner = min(self.players.values(), key=lambda player: player.time)
                winner.won = True
            self.race_active = False
        '''
        if (!data_handler.empty())
            process frame
            read {[id: 0, distance, 100], [id: 1, distance, 120]}
            for player in self.players
                player.move(timestamp, distance)
            if both players passed max_distance
        '''

    def racing(self):
        return any(player.racing for player in self.players.values())

    def get_players(self):
        return self.players.values


