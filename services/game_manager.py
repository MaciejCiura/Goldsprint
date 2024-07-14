import pygame
from services.scene_manager import SceneManager
from scenes.race_scene import RaceScene
from util.constant import Screen


class GameManager:
    def __init__(self, screen: pygame.Surface):
        self.scene_manager = SceneManager(screen)
        self.clock = pygame.time.Clock()
        self.running = False

