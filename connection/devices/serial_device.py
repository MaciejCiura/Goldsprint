import json
import serial
from connection.devices.device import Device


class SerialDevice:
    def __init__(self, port="COM3", baudrate=115200, timeout=2):
        self.serialPort = None
        self.is_connected = False
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout

    def connect(self):
        try:
            self.serialPort = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=8,
                timeout=self.timeout,
                stopbits=serial.STOPBITS_ONE
            )
            self.is_connected = True
            print(f"Connected to {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            print(f"Failed to connect: {e}")
            self.is_connected = False

    def send(self, command):
        if not self.is_connected:
            print("Device not connected. Cannot send configuration.")
            return
        if command:
            try:
                self.serialPort.write(command)
            except Exception as e:
                print(f"Send failed: {e}")

    def read_data(self):
        if not self.is_connected:
            print("Device not connected. Cannot read data.")
            return None

        try:
            serial_string = self.serialPort.readline()
            if not serial_string:
                return None
            print(serial_string)
            decoded_data = serial_string.decode("utf-8").strip()
            # print("Received data:", decoded_data)
            return decoded_data
        except Exception as e:
            print(f"Error reading data: {e}")
            return None

    def disconnect(self):
        if self.serialPort and self.serialPort.is_open:
            self.serialPort.close()
            print("Disconnected from serial port.")
        self.is_connected = False
