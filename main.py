import sys

from core.game_manager import GameManager

init_data_handler = None


game = GameManager()
game.setup()
game.run()

sys.exit()
