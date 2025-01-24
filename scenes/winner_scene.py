import pygame

import scenes.scene

from util.constant import Colors


class WinnerScene(scenes.scene.Scene):

    def __init__(self, screen: pygame.Surface, players):
        super().__init__(screen)
        self.players = players
        self.button_pressed = False

    def _update_entities(self):
        for player in self.players:
            player.update()

    def key_down(self, keyname: int) -> None:
        self.button_pressed = True

    def display(self):
        self.screen.fill(Colors.WHITE)
        for player in self.players:
            player.draw(self.screen)
        pygame.display.flip()

    def update_state(self) -> bool:
        self._update_entities()
        return self.button_pressed
