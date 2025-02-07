import time

import pytest
from unittest.mock import Mock
from core.controller import Controller
from core.race_manager import RaceManager
from connection.devices.simulated_device import SimulatedDevice


@pytest.fixture
def controller():
    device = SimulatedDevice()
    race_manager = RaceManager()
    return Controller(device, race_manager)


def test_controller_initialization(controller):
    assert controller.race_manager is not None
    assert controller.data_handler is not None


def test_controller_start_race(controller):
    controller.init_race("Alice", "Bob", 100)
    controller.start_race()

    assert controller.race_manager.race_in_progress is True
    assert controller.race_manager.players[0].name == "Alice"
    assert controller.race_manager.players[1].name == "Bob"


def test_controller_stop_race(controller):
    controller.init_race("Alice", "Bob", 5)
    controller.start_race()
    time.sleep(1)
    assert controller.race_manager.race_in_progress is False


def test_controller_handle_data(controller):
    controller.init_race("Alice", "Bob", 100)
    controller.start_race()

    # Simulate a data update
    sample_data = {
        "players": [
            {"id": 0, "distance": 40},
            {"id": 1, "distance": 60}
        ]
    }
    controller.handle_data(sample_data)

    assert controller.race_manager.players[0].distance == 40
    assert controller.race_manager.players[1].distance == 60


def test_controller_race_completion(controller):
    controller.init_race("Alice", "Bob", 40)
    controller.race_manager.on_race_end = Mock()
    controller.start_race()
    sample_data = {
        "players": [
            {"id": 0, "distance": 40},
            {"id": 1, "distance": 60}
        ]
    }
    controller.handle_data(sample_data)

    assert controller.race_manager.race_in_progress is False
    controller.race_manager.on_race_end.assert_called_once()


def test_controller_reset(controller):
    controller.init_race("Alice", "Bob", 50)
    controller.start_race()
    sample_data = {
        "players": [
            {"id": 0, "distance": 50},
            {"id": 1, "distance": 50}
        ]
    }
    controller.handle_data(sample_data)
    assert controller.race_manager.race_in_progress is False
    assert controller.race_manager.players[0].distance == 50
    assert controller.race_manager.players[1].distance == 50

    controller.reset()

    assert controller.race_manager.race_in_progress is False
    assert controller.race_manager.players[0].distance == 0
    assert controller.race_manager.players[1].distance == 0
