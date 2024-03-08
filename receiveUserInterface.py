import socket
import tkinter as tk
import threading
import time

def udp_server():
    server_ip = "192.168.1.13"
    server_port = 8002

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))

    while True:
        CanData, client_address = server_socket.recvfrom(1024)
        #data = server_socket.recvfrom(1024)
        hex_data = CanData.hex()
        
        data_payload = hex_data[-16:]
        decimal_data = int(data_payload, 16)
        time.sleep(0.5)
        label.config(text="{:}".format(decimal_data))
        root.update()

def start_udp_server():
    thread = threading.Thread(target=udp_server)
    thread.daemon = True
    thread.start()

# Create the tkinter window
root = tk.Tk()
root.title("SunMobility")

# Button to start generating numbers
start_button = tk.Button(root, text="Status Of Charge", command=start_udp_server)
start_button.pack()

# Create a label to display the numbers
label = tk.Label(root, font=("Helvetica", 24))
label.pack(pady=20)

# Button to open a link
history_button = tk.Button(root, text="History", command=lambda: open_link("https://random.com"))
history_button.pack()

# Function to open a link
def open_link(link):
    import webbrowser
    webbrowser.open(link)

# Run the tkinter event loop
root.mainloop()

