import pygame

import ui.scenes.scene
from ui.entities.text import Text
from util.constant import Colors

from core.events import event_manager


class StartScene(ui.scenes.scene.Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.text = Text("Goldsprint", 0, 0)
        self.button_pressed = False

        event_manager.emit("reset")

    def key_down(self, keyname: int) -> None:
        self.button_pressed = True

    def display(self):
        self.screen.fill(Colors.WHITE)
        self.text.center()
        self.text.draw(self.screen)

    def update_state(self) -> bool:
        return self.button_pressed


