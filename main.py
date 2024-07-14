import pygame
import sys
import services.scene_manager
from util.constant import Screen


pygame.init()

screen = pygame.display.set_mode((Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT))
pygame.display.set_caption(Screen.WINDOW_CAPTION)

game = services.scene_manager.SceneManager(screen)

status = True
while status is True:
    status = game.run()
    pygame.display.flip()

pygame.quit()

sys.exit()
