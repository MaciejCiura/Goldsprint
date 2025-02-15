import pygame
from ui.scenes.countdown_scene import CountdownScene
from ui.scenes.race_scene import RaceScene
from ui.scenes.start_scene import StartScene
from ui.scenes.winner_scene import WinnerScene
from util.constant import Screen
from core.events import event_manager


class PyGameManager:
    def __init__(self):
        self.screen = None
        self.active_scene = None
        self.clock = None
        self._setup()
        self._subscribe()

    def __del__(self):
        pygame.quit()

    def _setup(self):
        pygame.init()
        pygame.display.set_caption(Screen.WINDOW_CAPTION)
        self.screen = pygame.display.set_mode((Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.active_scene = StartScene(self.screen)

    def _subscribe(self):
        event_manager.subscribe("reset", self._on_reset)
        event_manager.subscribe("countdown", self._on_countdown)
        event_manager.subscribe("race_started", self._on_start_race)
        event_manager.subscribe("race_finished", self._on_race_finished)

    def _on_reset(self):
        self.active_scene = StartScene(self.screen)
        self.active_scene.setup()

    def _on_countdown(self, *args, **kwargs):
        self.active_scene = CountdownScene(self.screen)
        self.active_scene.setup()

    def _on_start_race(self, players):
        self.active_scene = RaceScene(self.screen, players)
        self.active_scene.setup()

    def _on_race_finished(self, players):
        self.active_scene = WinnerScene(self.screen, players)
        self.active_scene.setup()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        self.active_scene.update_state()
        self.active_scene.display()
        self.clock.tick(Screen.FRAMERATE)
        pygame.display.flip()
        return True
