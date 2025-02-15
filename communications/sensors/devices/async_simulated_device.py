import json
import asyncio
from communications.sensors.devices.device import Device


class SimulatedDevice(Device):
    def __init__(self):
        self.is_connected = False
        self.simulated_data = {
            "players": [
                {"id": 0, "distance": 0},
                {"id": 1, "distance": 0}
            ]
        }
        self.running = False

    async def connect(self):
        # Simulate asynchronous connection setup
        await asyncio.sleep(0)
        self.is_connected = True

    async def disconnect(self):
        # Simulate asynchronous disconnection
        await asyncio.sleep(0)
        self.is_connected = False

    async def send(self, command):
        if not self.is_connected:
            print("Device not connected. Cannot send configuration.")
            return
        # Simulate non-blocking send operation
        await asyncio.sleep(0)
        if command == b'{"command": "start"}\n':
            self.running = True
        elif command == b'{"command": "stop"}\n':
            self.running = False
        elif command == b'{"command": "clear"}\n':
            self.simulated_data["players"][0]["distance"] = 0
            self.simulated_data["players"][1]["distance"] = 0

    async def receive(self):
        if not self.running or not self.is_connected:
            return None
        # Simulate delay for asynchronous reading (e.g., waiting for data)
        await asyncio.sleep(0.1)
        json_data = (json.dumps(self.simulated_data) + '\n').encode()
        # Update simulated data for the next read
        self.simulated_data["players"][0]["distance"] += 1
        self.simulated_data["players"][1]["distance"] += 2
        return json_data
