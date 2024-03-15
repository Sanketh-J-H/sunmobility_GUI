import socket
import os
import threading
import datetime

# Define variables and their start bits and lengths
B2T_BMS1 = {
    "B2T_TMax": (0, 8),
    "B2T_Tmin": (8, 8),
    "B2T_ScBatU_H": (16, 8),
    "B2T_ScBatU_L": (24, 8),
    "B2T_Mode": (32, 1),
    "B2T_TMSWorkMode": (33, 3),
    "B2T_BMUWorkMode": (36, 1),
    "B2T_HighVCtrl": (39, 1),
    "B2T_TargetT": (40, 8),
    "B2T_TAvg": (48, 8),
    "B2T_Life": (56, 8)
}


class B2TServer:
    def __init__(self):

        # self.network_BSSID = 'F0:C8:14:77:98:9D'
        self.network_BSSID = '60:FB:00:2E:A0:BF'
        # self.network_BSSID = '60:FB:00:2E:A0:BA'
        self.password = '12345678'
        self.SERVER_IP = '192.168.1.12'
        self.SERVER_PORT = 8001
        self.index = 0

    def create_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.SERVER_IP, self.SERVER_PORT))
        self.lock = threading.Lock()  # Add a lock for thread safety

    def connect_to_wifi(self):
        command = f"nmcli device wifi connect {self.network_BSSID} password {self.password}"
        exit_code1 = os.system(command)
        if exit_code1 == 0:
            print(
                f"Successfully connected to WiFi network: {self.network_BSSID}")
        else:
            print(
                f"Error: Failed to connect to WiFi network {self.network_BSSID}")

    def disconnect_from_wifi(self):
        command = f"nmcli device disconnect wlo1"
        exit_code = os.system(command)
        if exit_code == 0:
            print(f"Device 'wlo1' successfully disconnected.")
        else:
            print(f"Error: Failed to disconnect from Device 'wlo1'.")

    def receive_data_from_socket(self):
        data, _ = self.server_socket.recvfrom(13)
        hex_data = data.hex()  # Convert received data to Hexadecimal
        return hex_data

    def start_server(self):
        self.disconnect_from_wifi()
        self.connect_to_wifi()
        self.create_socket()
        print("UDP server is listening...")
        while True:
            received_data = self.receive_data_from_socket()
            print("CAN ID <", received_data[2:10],
                  ">", " ", "HEX data", received_data[10:])
            
            # Get the current date and time
            timestamp = datetime.datetime.now()
            # Convert the timestamp to a string in a specific format
            timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            # Define the output string
            output_string = f'{timestamp_str} : CAN ID <{received_data[2:10]}> {received_data[10:]}\n'

            # Specify the file path
            file_path = "CANT_Test10Amps.log"

            # Write the output string to the file
            with open(file_path, "a") as file:
                file.write(output_string)

    def stop_server(self):
        self.server_socket.close()


if __name__ == "__main__":
    server = B2TServer()
    server_thread = threading.Thread(target=server.start_server)
    # server_thread.daemon = True  # Run the thread as a daemon so it exits when the main program exits
    server_thread.start()
