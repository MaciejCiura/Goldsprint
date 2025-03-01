import asyncio
import threading
import time
from communications.controlls.cli.cli_handler import CliHandler
from communications.sensors.devices.simulated_device import SimulatedDevice
from communications.sensors.device_controller import DeviceController
from core.race_manager import RaceManager
from core.events import event_manager

from ui.pygame_controller import PyGameManager


def start_async_loop(loop):
    asyncio.set_event_loop(loop)
    try:
        loop.run_forever()
    finally:
        tasks = asyncio.all_tasks(loop)
        for task in tasks:
            task.cancel()
        loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
        loop.close()
        print("Asyncio loop closed.")


def run_pygame():
    loop = asyncio.new_event_loop()
    loop_thread = threading.Thread(target=start_async_loop, args=(loop,), daemon=True)

    input_controller = CliHandler(loop)
    loop_thread.start()

    device_controller = DeviceController(SimulatedDevice())
    race_manager = RaceManager()
    game = PyGameManager()

    running = True
    while running:
        event_manager.process_callbacks()
        running = game.run()

    loop.call_soon_threadsafe(loop.stop)
    loop_thread.join()


def main():
    run_pygame()


if __name__ == "__main__":
    main()
