import asyncio
import threading
import pygame
import aioconsole  # asynchronous console input
from connection.devices.simulated_device import SimulatedDevice
from core.controller import Controller
from core.events import event_manager
from core.race_manager import RaceManager
from util.constant import Screen
from ui.scene_manager import SceneManager


async def cli_loop(command_queue):
    print("\nCommands: init, start, stop, reset, exit")
    while True:
        try:
            command = await aioconsole.ainput("Enter command: ")
        except asyncio.CancelledError:
            break

        command = command.strip().lower()
        await command_queue.put(command)

        if command == "exit":
            print("Exiting CLI race manager.")
            break


async def process_commands(command_queue, name1, name2):
    while not command_queue.empty():
        command = await command_queue.get()

        if command == "init":
            await event_manager.emit("init_race", name1, name2)
            print(f"Race initialized for {name1} and {name2}.")
        elif command == "start":
            await event_manager.emit("start_race")
            print(f"Race started between {name1} and {name2}.")
        elif command == "stop":
            await event_manager.emit("stop_race")
            print("Race stopped.")
        elif command == "reset":
            await event_manager.emit("reset")
            print("Race data reset.")


def start_async_loop(loop, command_queue, name1, name2):
    asyncio.set_event_loop(loop)
    cli_task = loop.create_task(cli_loop(command_queue))
    try:
        loop.run_forever()
    finally:
        # Cancel all pending tasks when the loop is stopping.
        tasks = asyncio.all_tasks(loop)
        for task in tasks:
            task.cancel()
        loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
        loop.close()
        print("Asyncio loop closed.")


def run_pygame(command_queue):
    pygame.init()
    pygame.display.set_caption(Screen.WINDOW_CAPTION)
    screen = pygame.display.set_mode((Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT))

    device = SimulatedDevice()
    race_manager = RaceManager()
    controller = Controller(device, race_manager)
    scene_manager = SceneManager(screen)

    name1 = "Dupa"
    name2 = "Kupa"

    # Create and start a new asyncio event loop in a separate thread.
    loop = asyncio.new_event_loop()
    async_thread = threading.Thread(
        target=start_async_loop,
        args=(loop, command_queue, name1, name2),
        daemon=True
    )
    async_thread.start()

    running = True
    while running:
        # Process any pending CLI commands.
        while not command_queue.empty():
            asyncio.run_coroutine_threadsafe(
                process_commands(command_queue, name1, name2),
                loop
            )
        # Run your Pygame scene; assume scene_manager.run() returns False when done.
        running = scene_manager.run()
        pygame.display.flip()

    # Pygame loop has ended; signal the asyncio loop to stop.
    print("Shutting down...")
    loop.call_soon_threadsafe(loop.stop)
    async_thread.join()
    pygame.quit()


def main():
    command_queue = asyncio.Queue()  # Async-safe queue for CLI commands
    run_pygame(command_queue)


if __name__ == "__main__":
    main()
