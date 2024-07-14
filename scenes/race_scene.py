import pygame

import scenes.scene

from entities.player import Player

from util.constant import Screen, Colors, Bike
from util.position import Position


class RaceScene(scenes.scene.Scene):

    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.players = [Player(Colors.RED, Position(Screen.STARTING_POSITION, Screen.BIKE1_Y)),
                        Player(Colors.BLUE, Position(Screen.STARTING_POSITION, Screen.BIKE2_Y),
                               progressbar_position=Position(Screen.STARTING_POSITION, Screen.PROGRESSBAR2_Y))]
        self.start_time = pygame.time.get_ticks()
        self.winner = None

    def _count_elapsed_time(self):
        return pygame.time.get_ticks() - self.start_time

    def update_entities(self):
        for player in self.players:
            if player.check_win():
                self.winner = player
                print(self._count_elapsed_time())
                break

    def key_down(self, keyname: int) -> None:
        if keyname == pygame.K_a:
            self.players[0].move(Bike.MOVE_INCREMENT, 0)
        elif keyname == pygame.K_l:
            self.players[1].move(Bike.MOVE_INCREMENT, 0)

    def display(self):
        self.screen.fill(Colors.WHITE)
        for player in self.players:
            player.display(self.screen)
        pygame.display.flip()

    def update_state(self) -> bool:
        return self.winner is not None
