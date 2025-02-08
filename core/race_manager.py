import time
from enum import Enum
from core.player import Player
from core.events import event_manager


class RaceState(Enum):
    IDLE = "idle"
    COUNTDOWN = "countdown"
    RACING = "racing"
    FINISHED = "finished"


class RaceManager:
    def __init__(self, players=None, finish_distance=50):
        if players is None:
            players = {0: Player(0, "Player_1"), 1: Player(1, "Player_2")}
        self.players = players
        self.finish_distance = finish_distance
        self.start_time = None
        self.race_state = RaceState.IDLE
        self.race_in_progress = False
        self.winners = None
        event_manager.subscribe("reset", self.reset())
        event_manager.subscribe("init_race", self.init)
        event_manager.subscribe("data_received", self.handle_data)

    def add_player(self, player):
        if player.id in self.players:
            raise ValueError(f"Player with id {player.id} already exists.")
        self.players[player.id] = player

    def init(self, player_name_1, player_name_2, finish_distance=None):
        if finish_distance is not None:
            self.finish_distance = finish_distance
        players = {0: Player(0, player_name_1), 1: Player(1, player_name_2)}
        self.players = players
        self.start_time = None
        self.race_in_progress = False
        self.winners = None
        self.countdown()

    def reset(self):
        self.race_state = RaceState.IDLE
        for player in self.players.values():
            player.reset()

    def countdown(self):
        event_manager.emit("countdown")
        self.race_state = RaceState.COUNTDOWN
        print("Get ready...")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("GO!")
        self.start_race()

    def start_race(self):
        self.race_in_progress = True
        self.race_state = RaceState.RACING
        for player in self.players.values():
            player.distance = 0
            player.racing = True
            player.won = False
        self.start_time = time.time()
        event_manager.emit("start_race", self.players)

    def handle_data(self, data):
        if self.race_state == RaceState.IDLE:
            pass
        elif self.race_state == RaceState.COUNTDOWN:
            self.falstart()
        elif self.race_state == RaceState.RACING:
            self.update(data)
        elif self.race_state == RaceState.FINISHED:
            pass

    def falstart(self):
        print("DUPADUPAFALSTARTDUPADUPA")

    def update(self, data):
        if not self.race_in_progress:
            print("falstart!!!")
            # emit falstart event
            pass

        players_data = data["players"]
        for player_data in players_data:
            player = self.players[player_data["id"]]
            if player.racing:
                player.move(player_data["distance"])
                if player.distance >= self.finish_distance:  # TODO change to dynamic distance parameter
                    player.racing = False
                    player.time = time.time() - self.start_time
                    if not any(winner.won for winner in self.players.values()):
                        player.won = True

        event_manager.emit("race_updated", self.players)
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
                self.race_state = RaceState.FINISHED
                event_manager.emit("race_finished", self.players)

    def racing(self):
        return any(player.racing for player in self.players.values())

    def get_players(self):
        return self.players.values

    def get_winners(self):
        return self.winners



