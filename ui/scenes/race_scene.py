import pygame
import ui.scenes.scene
from ui.entities.player_view import PlayerView
from util.constant import Screen, Colors


class RaceScene(ui.scenes.scene.Scene):
    def __init__(self, screen: pygame.Surface, race_manager):
        super().__init__(screen)
        self.race_manager = race_manager
        self.player_views = [PlayerView(self.race_manager.players[0],
                                        x=Screen.STARTING_POSITION, y=Screen.BIKE1_Y,
                                        color=Colors.RED),
                             PlayerView(self.race_manager.players[1],
                                        x=Screen.STARTING_POSITION, y=Screen.BIKE2_Y,
                                        color=Colors.BLUE)]
        self.race_manager.start_race()

    # Workaround for development
    def key_down(self, keyname: int) -> None:
        inc1 = 0
        inc2 = 0
        if keyname == pygame.K_a:
            inc1 = 20
        elif keyname == pygame.K_l:
            inc2 = 20
        data = {
            "players": [
                {"id": 0, "distance": self.race_manager.players[0].distance + inc1},
                {"id": 1, "distance": self.race_manager.players[1].distance + inc2}
            ]
        }
        self.race_manager.update(data)

    def display(self):
        self.screen.fill(Colors.WHITE)
        for player_view in self.player_views:
            player_view.draw(self.screen)

    def update_state(self) -> bool:
        for player_view in self.player_views:
            player_view.update()
        return not self.race_manager.race_active
