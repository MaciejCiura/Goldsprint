import pygame
import scenes.scene
from entities.player import Player
from services.player_manager import PlayerManager
from util.constant import Screen, Colors, Bike


class RaceScene(scenes.scene.Scene):
    def __init__(self, screen: pygame.Surface, data_handler):
        super().__init__(screen)
        self.players = [Player(0, "Dupa", color=Colors.RED, x=Screen.STARTING_POSITION, y=Screen.BIKE1_Y),
                        Player(1, "Kupa", color=Colors.BLUE, x=Screen.STARTING_POSITION, y=Screen.BIKE2_Y)]
        self.player_manager = PlayerManager(self.players)
        self.player_manager.start_race()
        self.data_handler = data_handler

    def key_down(self, keyname: int) -> None:
        if keyname == pygame.K_a:
            if self.player_manager.get_players()[0].racing:
                self.player_manager.get_players()[0].move(Bike.MOVE_INCREMENT)
        elif keyname == pygame.K_l:
            if self.player_manager.get_players()[1].racing:
                self.player_manager.get_players()[1].move(Bike.MOVE_INCREMENT)

    def display(self):
        self.screen.fill(Colors.WHITE)
        for player in self.player_manager.get_players():
            player.draw(self.screen)

    def update_state(self) -> bool:
        self.player_manager.update()
        if not self.player_manager.racing(): # TODO: move this logic to winner_scene
            winner = min(self.player_manager.get_players(), key=lambda player: player.time)
            winner.won = True
        return not self.player_manager.racing()
