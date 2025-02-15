import json
from communications.sensors.devices.device import Device


class SimulatedDevice(Device):
    def __init__(self):
        self.is_connected = False
        self.simulated_data = {"players": [
                {"id": 0, "distance": 0},
                {"id": 1, "distance": 0}]}
        self.running = False

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
        self.simulated_data["players"][0]["distance"] += 1
        self.simulated_data["players"][1]["distance"] += 2
        return json_data
