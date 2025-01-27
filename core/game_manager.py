import pygame
from core.player import Player
from core.race_manager import RaceManager
from ui.scene_manager import SceneManager
from util.constant import Screen


class GameManager:
    def __init__(self):
        self.screen = None
        self.scene_manager = None
        self.clock = None
        self.running = False
        self.race_manager = RaceManager()

    def setup(self):
        pygame.init()
        pygame.display.set_caption(Screen.WINDOW_CAPTION)
        self.screen = pygame.display.set_mode((Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT))
        # TODO: Init data handler

        self.scene_manager = SceneManager(self.screen, self.race_manager)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running is True:
            self.running = self.scene_manager.run()
            pygame.display.flip()
        pygame.quit()
