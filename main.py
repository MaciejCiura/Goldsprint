import pygame
import sys
import services.game_manager
from util.constant import Screen


pygame.init()

screen = pygame.display.set_mode((Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT))
pygame.display.set_caption(Screen.WINDOW_CAPTION)

game = services.game_manager.GameManager(screen)
game.start()

pygame.quit()

sys.exit()
