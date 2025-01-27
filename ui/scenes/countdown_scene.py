import pygame

import ui.scenes.scene
from ui.entities.text import Text
from util.constant import Colors


class CountdownScene(ui.scenes.scene.Scene):
    def __init__(self, screen: pygame.Surface, race_manager):
        super().__init__(screen)
        self.text = Text("Ready...", 0, 0)
        self.button_pressed = False
        self.race_manager = race_manager

    def setup(self) -> None:
        self.button_pressed = False
        # self.race_manager.countdown()

    def key_down(self, keyname: int) -> None:
        self.button_pressed = True

    def display(self):
        self.screen.fill(Colors.WHITE)
        self.text.center()
        self.text.draw(self.screen)

    def update_state(self) -> bool:
        # read names and other properites
        # if run button pressed
        return self.button_pressed


