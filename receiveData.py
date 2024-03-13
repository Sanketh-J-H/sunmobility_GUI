import socket

# Define server IP address and port
SERVER_IP = '192.168.1.12'
SERVER_PORT = 8001

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server_socket.bind((SERVER_IP, SERVER_PORT))

print("UDP server is listening...")

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)
    hex_data = data.hex()

    # Print received data and client address
    print(f"Received data from {client_address}:0x{hex_data}")