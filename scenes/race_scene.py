import pygame
import scenes.scene
from entities.player import Player
from util.constant import Screen, Colors, Bike


class RaceScene(scenes.scene.Scene):

    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.players = [Player("Dupa", color=Colors.RED, x=Screen.STARTING_POSITION, y=Screen.BIKE1_Y),
                        Player("Kupa", color=Colors.BLUE, x=Screen.STARTING_POSITION, y=Screen.BIKE2_Y)]
        for player in self.players:
            player.racing = True
        self.racing = True
        self.start_time = pygame.time.get_ticks()
        self.players[0].set_time(self.start_time)
        self.players[1].set_time(self.start_time)

    def _count_elapsed_time(self, time):
        return time - self.start_time

    def _update_entities(self):
        for player in self.players:
            player.update()

    def _finish(self):
        if not self.racing:
            for player in self.players:
                player.racing = False

    def key_down(self, keyname: int) -> None:
        if keyname == pygame.K_a:
            if self.players[0].racing:
                self.players[0].move(Bike.MOVE_INCREMENT)
        elif keyname == pygame.K_l:
            if self.players[1].racing:
                self.players[1].move(Bike.MOVE_INCREMENT)

    def display(self):
        self.screen.fill(Colors.WHITE)
        for player in self.players:
            player.draw(self.screen)

    def update_state(self) -> bool:
        self._update_entities()
        if all(not player.racing for player in self.players):
            self.racing = False
            winner = min(self.players, key=lambda player: player.time)
            winner.won = True
        return not self.racing
