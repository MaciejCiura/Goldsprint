from dataclasses import dataclass, field
from enum import Enum
from typing import Dict

from core.player import PlayerRaceStatus


class RacePhase(Enum):
    IDLE = 0
    READY = 1
    COUNTDOWN = 2
    RACING = 3
    FINISHED = 4
    FALSE_START = 5


@dataclass
class RaceConfig:
    finish_distance: float = 100.0
    countdown_seconds: int = 4


@dataclass
class RaceState:
    phase: RacePhase = RacePhase.IDLE
    player_statuses: Dict[int, PlayerRaceStatus] = field(default_factory=dict)
    start_time: float = 0.0
    countdown_start: float = 0.0
    countdown_remaining: float = 0.0
