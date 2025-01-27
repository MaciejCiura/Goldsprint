import json
import threading
import queue
from time import sleep


class DataHandler:
    def __init__(self, device, data_callback=None):
        self.device = device
        self.thread = None
        self.running = False
        self.data_callback = data_callback

    def start(self):
        self.device.connect()
        if not self.device.is_connected:
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

    def send_configuration(self, command):
        config = {"command": command}
        try:
            self.device.send((json.dumps(config) + '\n').encode())
        except Exception as e:
            print(f"Error sending configuration: {e}")

    def _read_loop(self):
        while self.running:
            try:
                if not self.device.is_connected:
                    print("Device disconnected. Stopping thread.")
                    break

                raw_data = self.device.read_data()
                if not raw_data:
                    continue
                data = json.loads(raw_data)

                if self.data_callback:
                    self.data_callback(data)
                else:
                    print(data)
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
            except Exception as e:
                print(f"Error in read loop: {e}")
            sleep(0.01)

    def is_running(self):
        return self.running and self.thread.is_alive()
