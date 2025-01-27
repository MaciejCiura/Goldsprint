import pygame

import ui.scenes.scene
from ui.entities.text import Text
from util.constant import Colors


class StartScene(ui.scenes.scene.Scene):
    def __init__(self, screen: pygame.Surface, controller):
        super().__init__(screen)
        self.controller = controller
        self.text = Text("Goldsprint", 0, 0)
        self.button_pressed = False

    def key_down(self, keyname: int) -> None:
        self.controller.init_race("Dupa", "Kupa")
        self.button_pressed = True

    def display(self):
        self.screen.fill(Colors.WHITE)
        self.text.center()
        self.text.draw(self.screen)

    def update_state(self) -> bool:
        # read names and other properites
        # if run button pressed
        return self.button_pressed


