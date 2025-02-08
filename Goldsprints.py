import sys
import time

from connection.devices.serial_device import SerialDevice
from connection.devices.simulated_device import SimulatedDevice
from core.race_manager import RaceManager
from ui.game_manager import GameManager
from core.controller import Controller
from core.events import event_manager

# game = GameManager(controller)
# game.setup()
# game.run()

def main():
    print("Starting CLI-based Race Manager...")

    # Initialize game logic (without UI)
    device = SimulatedDevice()  # Replace with real device if needed
    race_manager = RaceManager()
    controller = Controller(device, race_manager)
    # game = GameManager(controller)
    # game.setup()
    # game.run()
    name1 = input("Enter name for Player 1: ")
    name2 = input("Enter name for Player 2: ")

    while True:
        print("\nCommands: start, stop, status, reset, exit")
        command = input("Enter command: ").strip().lower()

        if command == "init":
            event_manager.emit("init_race", name1, name2)

        elif command == "start":
            event_manager.emit("start_race")
            print(f"Race started between {name1} and {name2}.")

        elif command == "stop":
            controller.stop_race()
            print("Race stopped.")

        elif command == "status":
            if controller.race_in_progress():
                print("Race is currently in progress.")
            else:
                print("No race is active.")

        elif command == "reset":
            controller.reset()
            print("Race data reset.")

        elif command == "exit":
            print("Exiting CLI race manager.")
            break

        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
