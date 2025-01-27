from abc import ABC, abstractmethod
import socket
import json


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

import socket
import threading
from typing import Callable


class TCPDevice:
    def __init__(self, host: str = "192.168.4.1", port: int = 12345):
        """
        :param host: IP address of the ESP32 server.
        :param port: Port number of the ESP32 server.
        """
        self.host = host
        self.port = port
        self.client_socket = None
        self.running = False
        self.data_handler: Callable[[str], None] = None  # Callback for received data

    def connect(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")

            # Start a separate thread to receive data
            self.running = True
            threading.Thread(target=self._receive_data, daemon=True).start()
        except Exception as e:
            print(f"Failed to connect to server: {e}")
            self.disconnect()

    def disconnect(self):
        self.running = False
        if self.client_socket:
            self.client_socket.close()
            self.client_socket = None
        print("Disconnected from server")

    def send_command(self, command: str):
        """
        :param command: The command to send.
        """
        if not self.client_socket:
            print("Error: Not connected to the server")
            return

        try:
            self.client_socket.sendall(command.encode("utf-8"))
            print(f"Sent command: {command}")
        except Exception as e:
            print(f"Error sending command: {e}")

    def set_data_handler(self, handler: Callable[[str], None]):
        """
        :param handler: Function that takes a string as input.
        """
        self.data_handler = handler

    def _receive_data(self):
        try:
            while self.running:
                data = self.client_socket.recv(1024).decode("utf-8")
                if not data:
                    print("Server closed the connection")
                    break

                print(f"Received data: {data}")

                # Process the data using the callback
                if self.data_handler:
                    self.data_handler(data)
        except Exception as e:
            print(f"Error receiving data: {e}")
        finally:
            self.disconnect()


import serial
import threading


class SerialDevice:
    def __init__(self):
        self.serialPort = None
        self.is_connected = False

    def connect(self):
        self.serialPort = serial.Serial(
            port="COM3", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        self.is_connected = True

    def connected(self):
        return self.is_connected

    def read_data(self):
        serial_string = self.serialPort.readline()
        try:
            print(serial_string.decode("Ascii"))
        except Exception as e:
            pass
        return serial_string

    def disconnect(self):
        self.is_connected = False
        self.serialPort.close()

class SimulatedDevice(Device):
    pass
