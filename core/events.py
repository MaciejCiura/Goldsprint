from typing import Callable, Dict, List
import threading


class EventManager:
    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = {}
        self.lock = threading.Lock()

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
            if event_name in self.listeners:
                for callback in self.listeners[event_name]:
                    threading.Thread(target=callback, args=args, kwargs=kwargs).start()


# Global instance
event_manager = EventManager()
