import pygame
from ui.scenes.countdown_scene import CountdownScene
from ui.scenes.race_scene import RaceScene
from ui.scenes.start_scene import StartScene
from ui.scenes.winner_scene import WinnerScene
from util.constant import Screen
from core.events import event_manager

class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.active_scene = StartScene(screen)
        self.clock = pygame.time.Clock()

        event_manager.subscribe("reset", self._on_reset)
        event_manager.subscribe("init_race", self._on_init_race)
        event_manager.subscribe("start_race", self._on_start_race)
        event_manager.subscribe("race_finished", self._on_race_finished)

    def _on_reset(self):
        self.active_scene = StartScene(self.screen)
        self.active_scene.setup()

    def _on_init_race(self, *args, **kwargs):
        self.active_scene = CountdownScene(self.screen)
        self.active_scene.setup()

    def _on_start_race(self, players):
        self.active_scene = RaceScene(self.screen, players)
        self.active_scene.setup()

    def _on_race_finished(self, players):
        self.active_scene = WinnerScene(self.screen, players)
        self.active_scene.setup()

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
        self.active_scene.display()

        self.active_scene.update_state()

        self.clock.tick(Screen.FRAMERATE)
        return True
