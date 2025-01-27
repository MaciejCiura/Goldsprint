import pytest
import time
from core.player import Player
from core.race_manager import RaceManager


@pytest.fixture
def race_manager():
    players = {
        0: Player(0, "Alice"),
        1: Player(1, "Bob")
    }

    return RaceManager(players, finish_distance=100)


def get_data(race_manager, inc1, inc2):
    players_data = {
        "players": [
            {"id": 1, "distance": race_manager.players[0].distance + inc1},
            {"id": 2, "distance": race_manager.players[1].distance + inc2}
        ]
    }
    return players_data


def test_start_race(race_manager):
    race_manager.start_race()
    assert race_manager.race_active is True
    for player in race_manager.players.values():
        assert player.racing is True
        assert player.distance == 0
        assert player.won is False


def test_handle_data(race_manager):
    race_manager.start_race()
    race_manager.update(get_data(race_manager, 50, 75))

    assert race_manager.players[0].distance == 50
    assert race_manager.players[1].distance == 75
    assert race_manager.race_active is True


def test_finish_race(race_manager):
    race_manager.start_race()
    race_manager.update(get_data(race_manager, 100, 0))  # Alice finishes the race
    assert race_manager.players[0].racing is False
    assert race_manager.players[0].won is True

    # Bob hasn't finished yet
    assert race_manager.players[1].racing is True
    assert race_manager.players[1].won is False
    assert race_manager.race_active is True
    time.sleep(1)
    race_manager.update(get_data(race_manager, 0, 100))  # Bob finishes
    assert race_manager.players[1].racing is False
    assert race_manager.players[1].won is False
    assert race_manager.race_active is False


def test_get_winners(race_manager):
    race_manager.start_race()
    race_manager.update(get_data(race_manager, 100, 80))

    winner = race_manager.get_winners()
    assert winner is None  # Race is still active

    race_manager.update(get_data(race_manager, 0, 20))  # Bob finishes
    winner = race_manager.get_winners()
    assert winner is not None


def test_race_not_active_if_no_players(race_manager):
    race_manager.start_race()
    race_manager.update(get_data(race_manager, 100, 100))

    assert race_manager.race_active is False
    winners = race_manager.get_winners()
    assert len(winners) == 2  # Tie
