import json
import threading
import queue
from time import sleep


class DataHandler:
    def __init__(self, device, race_manager):
        self.device = device
        self.thread = None
        self.running = False
        self.race_manager = race_manager

    def start(self):
        self.device.connect()
        if not self.device.connected():
            raise ConnectionError("Device is not connected. Cannot start DataHandler.")
        self.running = True
        print("Starting thread...")  # Debugging statement
        self.thread = threading.Thread(target=self._read_loop, daemon=True)
        self.thread.start()

    def disconnect(self):
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join()  # Wait for the thread to finish
        self.device.disconnect()

    def send_configuration(self):
        pass

    def _read_loop(self):
        while self.running:
            try:
                if not self.device.connected():
                    print("Device disconnected. Stopping thread.")
                    break

                data = json.loads(self.device.read_data())
                self.race_manager.update(data)
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
            except Exception as e:
                print(f"Error in read loop: {e}")
            sleep(0.001)

    def is_running(self):
        return self.running and self.thread.is_alive()
