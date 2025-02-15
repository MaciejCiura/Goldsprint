import json

from communications.sensors.devices.device import Device

from core.events import event_manager

class SimulatedDevice(Device):
    def __init__(self):
        self.is_connected = False
        self.simulated_data = {"players": [
                {"id": 0, "distance": 0},
                {"id": 1, "distance": 0}]}
        self.running = False
        self.addition = 0
        self.start_time = None
        event_manager.subscribe("race_started", self._on_race_started)

    def _on_race_started(self, *args, **kwargs):
        self.addition = 1

    def connect(self):
        self.is_connected = True

    def disconnect(self):
        self.is_connected = False

    def send(self, command):
        if not self.is_connected:
            print("Device not connected. Cannot send configuration.")
            return
        if command == b'{"command": "start"}\n':
            self.running = True
        elif command == b'{"command": "stop"}\n':
            self.running = False
        elif command == b'{"command": "clear"}\n':
            self.simulated_data["players"][0]["distance"] = 0
            self.simulated_data["players"][1]["distance"] = 0

    def receive(self):
        if not self.running or not self.is_connected:
            return None
        json_data = (json.dumps(self.simulated_data) + '\n').encode()
        self.simulated_data["players"][0]["distance"] += self.addition
        self.simulated_data["players"][1]["distance"] += 2*self.addition
        return json_data
