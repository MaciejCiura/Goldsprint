import sys, time
from connection.data_handler import DataHandler
from connection.device import TCPDevice, SerialDevice
from core.game_manager import GameManager

game = GameManager()
data_handler=DataHandler(SerialDevice(), game.race_manager)
data_handler.start()
game.setup()
game.run()

# After 5 seconds, disconnect and stop the thread
# data_handler.disconnect()
sys.exit()
