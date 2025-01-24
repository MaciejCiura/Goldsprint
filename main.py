import sys
from services.game_manager import GameManager

game = GameManager()
game.setup()
game.run()

sys.exit()
