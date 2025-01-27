from connection.data_handler import DataHandler


class Controller:
    def __init__(self, device, race_manager):
        self.race_manager = race_manager
        self.data_handler = DataHandler(device)
        self.data_handler.data_callback = self.race_manager.update

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
        self.race_manager.end_race()
        print("Race stopped.")

    def race_in_progress(self):
        return self.race_manager.race_in_progress

    def log_race(self):
        pass