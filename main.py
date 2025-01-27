import sys, time
from connection.data_handler import DataHandler
from connection.devices.serial_device import SerialDevice
from core.race_manager import RaceManager
from core.game_manager import GameManager
from core.controller import Controller
# data_handler=DataHandler(SerialDevice())
# data_handler.start()
#
# time.sleep(3)
# data_handler.send_configuration("start")
# time.sleep(3)
# print("--------STOP---------")
# data_handler.send_configuration("stop")
# time.sleep(3)
# print("--------CLEAR--------")
# data_handler.send_configuration("clear")
# data_handler.send_configuration("start")
# print("--------START--------")
# time.sleep(3)

device = SerialDevice()
race_manager = RaceManager()
controller = Controller(device, race_manager)
game = GameManager(controller)
game.setup()
game.run()

# After 5 seconds, disconnect and stop the thread
# data_handler.disconnect()
sys.exit()
