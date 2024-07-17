import pygame
from scenes.countdown_scene import CountdownScene
from scenes.race_scene import RaceScene
from scenes.start_scene import StartScene
from scenes.winner_scene import WinnerScene

from util.constant import Screen



class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.active_scene = StartScene(screen)
        self.clock = pygame.time.Clock()

    def key_down(self, keyname: int) -> None:
        # if isinstance(self.active_scene, StartScene):
        pass

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                self.active_scene.key_down(event.key)
        self.active_scene.display()
        if self.active_scene.update_state():
            self._next_scene()
        self.clock.tick(Screen.FRAMERATE)
        return True

    def _next_scene(self):
        if isinstance(self.active_scene, StartScene):
            self.active_scene = CountdownScene(self.screen)

        elif isinstance(self.active_scene, CountdownScene):
            self.active_scene = RaceScene(self.screen)

        elif isinstance(self.active_scene, RaceScene):
            self.active_scene = WinnerScene(self.screen, self.active_scene.winner)

        elif isinstance(self.active_scene, WinnerScene):
            self.active_scene = StartScene(self.screen)
