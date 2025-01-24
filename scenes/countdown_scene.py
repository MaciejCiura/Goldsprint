import pygame

import scenes.scene

from entities.text import Text

from util.constant import Colors
from util.position import Position


class CountdownScene(scenes.scene.Scene):
    def setup(self) -> None:
        self.text = Text("Ready...", 0, 0)
        self.button_pressed = False

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


