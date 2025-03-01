import time
from logging import Logger
from core.player import PlayerRaceStatus
from core.race_data import RaceConfig, RacePhase, RaceState
from core.events import event_manager


class RaceManager:
    def __init__(self):
        self.race_config = None
        self.finish_distance = None
        self.state_data = RaceState()

        event_manager.subscribe("reset", self.reset)
        event_manager.subscribe("countdown", self.countdown)
        event_manager.subscribe("init_race", self.setup_race)
        event_manager.subscribe("data_received", self.update)
        event_manager.subscribe("status", self.status)

    def status(self):
        print(self.state_data.phase)

    def setup_race(self, players, finish_distance=None):
        if self.state_data.phase is not RacePhase.IDLE:
            return

        self.race_config = RaceConfig()
        if finish_distance is not None:
            self.race_config.finish_distance = finish_distance

        for player in players:
            self.state_data.player_statuses[player.player_id] = PlayerRaceStatus(player=player)
        self._transition(RacePhase.READY)

    def countdown(self):
        if self.state_data.phase is not RacePhase.READY:
            return

        self.state_data.countdown_start = time.time()
        self._transition(RacePhase.COUNTDOWN)
        print("Countdown")

    def update(self, data=None):
        if self.state_data.phase == RacePhase.IDLE:
            return
        elif self.state_data.phase == RacePhase.READY:
            return
        elif self.state_data.phase == RacePhase.COUNTDOWN:
            self._update_countdown(data)
        elif self.state_data.phase == RacePhase.RACING:
            self._update_race(data)
        elif self.state_data.phase == RacePhase.FINISHED:
            return

    def reset(self):
        self._transition(RacePhase.IDLE)

    def _update_countdown(self, data):
        if data is not None:
            players_data = data["players"]

            for player_data in players_data:
                player_status = self.state_data.player_statuses[player_data["id"]]

                if player_status.distance > 0:
                    # self.false_start()
                    # return
                    pass

        elapsed = time.time() - self.state_data.countdown_start
        remaining = self.race_config.countdown_seconds - elapsed
        self.state_data.countdown_remaining = max(0.0, remaining)
        print(self.state_data.countdown_remaining)
        if remaining <= 0:
            self._transition(RacePhase.RACING)
            self.state_data.start_time = time.time()
            event_manager.emit("race_started", self.state_data.player_statuses)

    def false_start(self):
        self._transition(RacePhase.FALSE_START)
        print("DUPADUPAFALSTARTDUPADUPA")

    def _update_race(self, data):
        if data is None:
            return

        players_data = data["players"]

        for player_data in players_data:
            player_status = self.state_data.player_statuses[player_data["id"]]
            if not player_status.is_racing:
                continue
            self._update_player(player_status, player_data)

        event_manager.emit("race_updated", self.state_data.player_statuses)
        self._finish_race()

    def _update_player(self, player_status, player_data):
        player_status.distance = min(self.race_config.finish_distance, player_data["distance"])
        if player_status.distance >= self.race_config.finish_distance:
            player_status.is_racing = False
            player_status.finish_time = time.time() - self.state_data.start_time
            if not any(player.is_winner for player in self.state_data.player_statuses.values()):
                player_status.is_winner = True

    def _finish_race(self):
        if self.state_data.phase == RacePhase.RACING:
            if all(not player.is_racing for player in self.state_data.player_statuses.values()):
                self._transition(RacePhase.FINISHED)
                self._check_result()

                event_manager.emit("race_finished", self.state_data.player_statuses)

    def _check_result(self):
        min_time = min(player.finish_time for player in self.state_data.player_statuses.values() if player.finish_time is not None)

        for player_status in self.state_data.player_statuses.values():
            player_status.is_winner = player_status.finish_time == min_time

    def _transition(self, phase):
        print(f"Phase {phase}")
        self.state_data.phase = phase
