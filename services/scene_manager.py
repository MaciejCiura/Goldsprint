from scenes.race_scene import RaceScene
from scenes.winner_scene import WinnerScene


class SceneManager:
    def __init__(self, screen):
        self.active_scene = RaceScene(screen)

    def tick(self):
        pass

    def update(self):
        if self.active_scene.update_state():
            if isinstance(self.active_scene, RaceScene):
                self.active_scene = WinnerScene(self.active_scene.screen, self.active_scene.winner)
