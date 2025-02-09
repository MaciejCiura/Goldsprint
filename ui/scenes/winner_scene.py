import pygame

import ui.scenes.scene
from ui.entities.player_view import PlayerView
from util.constant import Colors, Screen


class WinnerScene(ui.scenes.scene.Scene):
    def __init__(self, screen: pygame.Surface, players):
        super().__init__(screen)
        self.player_views = [PlayerView(players[0],
                                        x=Screen.STARTING_POSITION, y=Screen.BIKE1_Y,
                                        color=Colors.RED),
                             PlayerView(players[1],
                                        x=Screen.STARTING_POSITION, y=Screen.BIKE2_Y,
                                        color=Colors.BLUE)]

    def setup(self):
        for player in self.player_views:
            player.progressbar.visible = False
            player.time_txt.visible = True

    def _update_entities(self):
        for player in self.player_views:
            player.update()

    def display(self):
        self.screen.fill(Colors.WHITE)
        for player in self.player_views:
            player.draw(self.screen)
        pygame.display.flip()

    def update_state(self):
        pass
