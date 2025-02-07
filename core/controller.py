import pprint
from connection.data_handler import DataHandler

class Controller:
    def __init__(self, device, race_manager):
        self.race_manager = race_manager
        self.data_handler = DataHandler(device)
        self.data_handler.data_callback = self.handle_data
        self.race_manager.on_race_end = self.stop_race

    def reset(self):
        self.race_manager.reset()
        self.data_handler.send_configuration("clear")

    def init_race(self, player_name_1, player_name_2, finish_distance=None):
        self.race_manager.setup(player_name_1, player_name_2, finish_distance)
        self.data_handler.start()

    def countdown(self):
        # check for fault start and so on
        pass

    def start_race(self):
        self.race_manager.start_race()
        self.data_handler.send_configuration("start")

    def stop_race(self):
        print(self.race_manager.players)
        self.data_handler.send_configuration("stop")

    def handle_data(self, data):
        self.race_manager.update(data)
        # plot data

    def race_in_progress(self):
        return self.race_manager.race_in_progress

    def log_race(self):
        pass