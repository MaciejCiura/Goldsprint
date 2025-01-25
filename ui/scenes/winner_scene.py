import pygame

import ui.scenes.scene

from util.constant import Colors


class WinnerScene(ui.scenes.scene.Scene):

    def __init__(self, screen: pygame.Surface, player_views):
        super().__init__(screen)
        self.player_views = player_views
        self.button_pressed = False

    def _update_entities(self):
        for player in self.player_views:
            player.update()

    def key_down(self, keyname: int) -> None:
        self.button_pressed = True

    def display(self):
        self.screen.fill(Colors.WHITE)
        for player in self.player_views:
            player.draw(self.screen)
        pygame.display.flip()

    def update_state(self) -> bool:
        self._update_entities()
        return self.button_pressed
