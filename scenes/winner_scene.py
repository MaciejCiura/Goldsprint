import pygame

import scenes.scene

from util.constant import Colors


class WinnerScene(scenes.scene.Scene):

    def __init__(self, screen: pygame.Surface, winner):
        super().__init__(screen)
        self.winner = winner
        self.button_pressed = False

    def key_down(self, keyname: int) -> None:
        self.button_pressed = True

    def display(self):
        self.screen.fill(Colors.WHITE)
        self.winner.display(self.screen)
        pygame.display.flip()

    def update_state(self) -> bool:
        return self.button_pressed
