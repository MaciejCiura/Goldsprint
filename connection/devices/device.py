from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def send_configuration(self, sampling_rate):
        pass

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def is_connected(self):
        pass
