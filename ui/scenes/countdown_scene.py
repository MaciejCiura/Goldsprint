import time

import pygame

import ui.scenes.scene
from ui.entities.text import Text
from util.constant import Colors


class CountdownScene(ui.scenes.scene.Scene):
    def __init__(self, screen: pygame.Surface, controller):
        super().__init__(screen)
        self.text = Text("Get ready...", 0, 0, font_size=84)
        self.button_pressed = False
        self.controller = controller
        self.countdown_values = None
        self.last_update_time = time.time()
        self.finished = False

    def setup(self) -> None:
        self.button_pressed = False
        self.countdown_values = ["3", "2", "1", "GO!"]

    def countdown(self):
        self.controller.countdown()
        time.sleep(1)

    def key_down(self, keyname: int) -> None:
        self.button_pressed = True

    def display(self):
        self.screen.fill(Colors.WHITE)
        self.text.center()
        self.text.draw(self.screen)

    def update_state(self) -> bool:
        current_time = time.time()
        if self.countdown_values and current_time - self.last_update_time >= 1:
            self.last_update_time = current_time
            self.text.set(self.countdown_values.pop(0))
            self.text.update()
            if not self.countdown_values:
                self.button_pressed = True
        return self.button_pressed


