import socket
import threading
from typing import Callable


class TcpDevice:
    def __init__(self, host: str = "192.168.4.1", port: int = 12345):
        """
        :param host: IP address of the ESP32 web_server.
        :param port: Port number of the ESP32 web_server.
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
            print(f"Connected to web_server at {self.host}:{self.port}")

            # Start a separate thread to receive data
            self.running = True
            threading.Thread(target=self._receive_data, daemon=True).start()
        except Exception as e:
            print(f"Failed to connect to web_server: {e}")
            self.disconnect()

    def disconnect(self):
        self.running = False
        if self.client_socket:
            self.client_socket.close()
            self.client_socket = None
        print("Disconnected from web_server")

    def send_command(self, command: str):
        """
        :param command: The command to send.
        """
        if not self.client_socket:
            print("Error: Not connected to the web_server")
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
