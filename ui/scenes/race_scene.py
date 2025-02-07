import pygame
import ui.scenes.scene
from ui.entities.player_view import PlayerView
from util.constant import Screen, Colors


class RaceScene(ui.scenes.scene.Scene):
    def __init__(self, screen: pygame.Surface, controller):
        super().__init__(screen)
        self.controller = controller
        self.player_views = [PlayerView(self.controller.race_manager.players[0],
                                        x=Screen.STARTING_POSITION, y=Screen.BIKE1_Y,
                                        color=Colors.RED),
                             PlayerView(self.controller.race_manager.players[1],
                                        x=Screen.STARTING_POSITION, y=Screen.BIKE2_Y,
                                        color=Colors.BLUE)]
        self.controller.start_race()

    def key_down(self, keyname: int) -> None:
        pass

    def display(self):
        self.screen.fill(Colors.WHITE)
        for player_view in self.player_views:
            player_view.draw(self.screen)

    def update_state(self) -> bool:
        for player_view in self.player_views:
            player_view.update()
        return not self.controller.race_in_progress()
