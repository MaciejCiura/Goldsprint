import pygame
from ui.scenes.countdown_scene import CountdownScene
from ui.scenes.race_scene import RaceScene
from ui.scenes.start_scene import StartScene
from ui.scenes.winner_scene import WinnerScene
from util.constant import Screen


class SceneManager:
    def __init__(self, screen, race_manager):
        self.screen = screen
        self.active_scene = StartScene(screen, race_manager)
        self.clock = pygame.time.Clock()
        self.race_manager = race_manager

    def key_down(self, keyname: int) -> None:
        # if isinstance(self.active_scene, StartScene):
        pass

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                self.active_scene.key_down(event.key)
        self.active_scene.display()

        if self.active_scene.update_state():
            self._next_scene()
            self.active_scene.setup()

        self.clock.tick(Screen.FRAMERATE)
        return True

    def _next_scene(self):
        if isinstance(self.active_scene, StartScene):
            self.active_scene = CountdownScene(self.screen)

        elif isinstance(self.active_scene, CountdownScene):
            self.active_scene = RaceScene(self.screen, self.race_manager)

        elif isinstance(self.active_scene, RaceScene):
            self.active_scene = WinnerScene(self.screen, self.active_scene.player_views)

        elif isinstance(self.active_scene, WinnerScene):
            self.active_scene = StartScene(self.screen, self.race_manager)
