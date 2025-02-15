from dataclasses import dataclass


@dataclass
class Player:
    player_id: int
    name: str


@dataclass
class PlayerRaceStatus:
    player: Player
    distance: float = 0.0
    speed: float = 0.0
    finish_time: float = 0.0
    is_racing: bool = True
    is_winner: bool = False