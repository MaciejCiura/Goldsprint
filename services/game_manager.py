import pygame
from services.scene_manager import SceneManager
from scenes.race_scene import RaceScene
from util.constant import Screen


class GameManager:
    def __init__(self, screen: pygame.Surface):
        self.scene_manager = SceneManager(screen)
        self.clock = pygame.time.Clock()
        self.running = False

    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.scene_manager.active_scene.key_down(event.key)

            if isinstance(self.scene_manager.active_scene, RaceScene):
                self.scene_manager.active_scene.update_entities()
            self.scene_manager.active_scene.display()
            self.scene_manager.update()

            self.clock.tick(Screen.FRAMERATE)
