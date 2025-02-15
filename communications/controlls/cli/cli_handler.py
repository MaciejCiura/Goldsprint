import asyncio
import aioconsole
from core.player import Player
from core.events import event_manager


class CliHandler:
    def __init__(self, loop):
        self.cli_task = loop.create_task(cli_loop())


async def cli_loop():
    print("\nCommands: init, start, stop, reset, exit")
    while True:
        try:
            command = await aioconsole.ainput("Enter command: ")
        except asyncio.CancelledError:
            break

        command = command.strip().lower()

        if command == "init":
            # fetch players from DB
            players = [Player(0, "Player_1"), Player(1, "Player_2")]
            event_manager.emit("init_race", players)
            print(f"Race initialized for Player_2 and Player_2.")
        elif command == "start":
            event_manager.emit("start_race")
            print(f"Race started between Player_2 and Player_2.")
        elif command == "stop":
            event_manager.emit("stop_race")
            print("Race stopped.")
        elif command == "reset":
            event_manager.emit("reset")
            print("Race data reset.")

        if command == "exit":
            print("Exiting CLI race manager.")
            break

