from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def send(self, sampling_rate):
        pass

    @abstractmethod
    def receive(self):
        pass
