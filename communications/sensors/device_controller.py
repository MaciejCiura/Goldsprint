import json
import threading
import queue
from time import sleep
from core.events import event_manager


class DeviceController:
    def __init__(self, device):
        self.device = device
        self.thread = None
        self.running = False
        self._subscribe()

    def _subscribe(self):
        event_manager.subscribe("reset", self._on_reset)
        event_manager.subscribe("init_race", self.init)
        event_manager.subscribe("countdown", self._on_countdown)
        event_manager.subscribe("race_finished", self._on_race_finished)

    def init(self, *args, **kwargs):
        if self.running:
            return
        self.device.connect()
        if not self.device.is_connected:
            raise ConnectionError("Device is not connected. Cannot start DataHandler.")
        self.running = True
        print("Starting thread...")
        self.thread = threading.Thread(target=self._read_loop, daemon=True)
        self.thread.start()

    def disconnect(self):
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join()
        self.device.disconnect()

    def _on_reset(self):
        self._send_configuration("clear")

    def _on_countdown(self, *args, **kwargs):
        self._send_configuration("start")

    def _on_race_finished(self, *args, **kwargs):
        self._send_configuration("stop")

    def _send_configuration(self, command):
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

                raw_data = self.device.receive()
                if not raw_data:
                    continue
                data = json.loads(raw_data)
                # print(data)
                event_manager.emit("data_received", data)
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
            except Exception as e:
                print(f"Error in read loop: {e}")
            sleep(0.1)

    def is_running(self):
        return self.running and self.thread.is_alive()
