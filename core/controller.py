import pprint
from connection.data_handler import DataHandler
from core.events import event_manager


class Controller:
    def __init__(self, device, race_manager):
        self.race_manager = race_manager
        self.data_handler = DataHandler(device)

    def reset(self):
        self.race_manager.reset()
        # self.data_handler.send_configuration("clear")

    def countdown(self):
        # check for fault start and so on
        pass

    def start_race(self):
        self.race_manager.start_race()
        # self.data_handler.send_configuration("start")

    def stop_race(self):
        print(self.race_manager.players)
        # self.data_handler.send_configuration("stop")

    def handle_data(self, data):
        self.race_manager.update(data)
        # plot data

    def race_in_progress(self):
        return self.race_manager.race_in_progress

    def log_race(self):
        pass
