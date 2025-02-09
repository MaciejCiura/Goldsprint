from typing import Callable, Dict, List
import threading
import queue


class EventManager:
    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = {}
        self.lock = threading.Lock()
        self._callback_queue = queue.Queue()

    def subscribe(self, event_name: str, callback: Callable):
        with self.lock:
            if event_name not in self.listeners:
                self.listeners[event_name] = []
            self.listeners[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: Callable):
        with self.lock:
            if event_name in self.listeners:
                self.listeners[event_name].remove(callback)

    def emit(self, event_name: str, *args, **kwargs):
        with self.lock:
            callbacks = self.listeners.get(event_name, []).copy()
        for callback in callbacks:
            self._callback_queue.put((callback, args, kwargs))

    def process_callbacks(self):
        while True:
            try:
                callback, args, kwargs = self._callback_queue.get_nowait()
            except queue.Empty:
                break
            try:
                callback(*args, **kwargs)
            except Exception as e:
                print(f"Error executing callback: {e}")


event_manager = EventManager()
