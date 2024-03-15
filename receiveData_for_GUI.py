import socket
import os
import threading
import time

# B2T_BMS1 = {}
# keys = [
#     "B2T_BMS1_Message_sum",
#     "B2T_TMax",
#     "B2T_Tmin",
#     "B2T_ScBatU_H",
#     "B2T_ScBatU_L",
#     "B2T_Mode",
#     "B2T_TMSWorkMode",
#     "B2T_BMUWorkMode",
#     "B2T_HighVCtrl",
#     "B2T_TargetT",
#     "B2T_TAvg",
#     "B2T_Life"
# ]

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
# B2T_BMS1 = {
#     "B2T_TMax": (56, 8),
#     "B2T_Tmin": (48, 8),
#     "B2T_ScBatU_H": (40, 8),
#     "B2T_ScBatU_L": (32, 8),
#     "B2T_Mode": (31, 1),
#     "B2T_TMSWorkMode": (28, 1),
#     "B2T_BMUWorkMode": (25, 3),
#     "B2T_HighVCtrl": (24, 1),
#     "B2T_TargetT": (16, 8),
#     "B2T_TAvg": (8, 8),
#     "B2T_Life": (0, 8)
# }


class B2TServer:
    def __init__(self):

        self.network_BSSID = 'F0:C8:14:77:98:9D'
        # self.network_BSSID = '60:FB:00:2E:A0:BF'
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
        command1 = f"nmcli device wifi connect {self.network_BSSID} password {self.password}"
        # command2 = f"sudo nmcli connection modify CANWiFi-II ipv4.address 192.168.1.12 ipv4.gateway 192.168.1.11 ipv4.dns 8.8.8.8"
        # command3 = f"sudo systemctl restart NetworkManager"
        exit_code1 = os.system(command1)
        # exit_code2 = os.system(command2)
        # exit_code3 = os.system(command3)
        # time.sleep(3)
        # exit_code1 = os.system(command1)
        if exit_code1 == 0:
            print(
                f"Successfully connected to WiFi network: {self.network_BSSID}")
        else:
            print(
                f"Error: Failed to connect to WiFi network {self.network_BSSID}")
            
        # if exit_code2 == 0:
        #     print(
        #         f"Successfully connected to IP : {self.SERVER_IP}")
        # else:
        #     print(
        #         f"Error: Failed to connect to WiFi network {self.SERVER_IP}")
            
        # if exit_code3 == 0:
        #     print(
        #         f"Successfully Restarted NetworkManager")
        # else:
        #     print(
        #         f"Error: Failed to Restarted NetworkManager")

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

    def get_B2T_BMS1(self):
        global B2T_BMS1
        # with self.lock
        return B2T_BMS1.copy()  # Return a copy to avoid directly exposing the internal dictionary

    def start_server(self):
        global B2T_BMS1
        global keys
        self.disconnect_from_wifi()
        self.connect_to_wifi()
        self.create_socket()
        print("UDP server is listening...")
        while True:
            received_data = self.receive_data_from_socket()
            print(received_data)

            # Check if the received data starts with the desired prefix
            if str(received_data[2:]).startswith('18ff45f3'):                
                trimmed_data = int(received_data, 16) & 0xffffffffffffffff
                # Convert hex data to binary string
                binary_data = bin(trimmed_data)[2:].zfill(64)
                # Decrypt hex data into separate variables
                decrypted_data = {}
                for var, (start_bit, length) in B2T_BMS1.items():
                    end_bit = start_bit + length
                    value = int(binary_data[start_bit:end_bit], 2)
                    if var == 
                    decrypted_data[var] = value
                print(decrypted_data)

    def stop_server(self):
        self.server_socket.close()


if __name__ == "__main__":
    server = B2TServer()
    server_thread = threading.Thread(target=server.start_server)
    # server_thread.daemon = True  # Run the thread as a daemon so it exits when the main program exits
    server_thread.start()
    # Other GUI-related code can go here