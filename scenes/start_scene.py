import pygame

import scenes.scene

from util.constant import Colors


class StartScene(scenes.scene.Scene):

    def __init__(self, screen: pygame.Surface, winner):
        super().__init__(screen)
        self.winner = winner

    def display(self):
        self.screen.fill(Colors.WHITE)
        self.winner.display(self.screen)
        pygame.display.flip()
