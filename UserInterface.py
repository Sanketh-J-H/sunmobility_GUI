import tkinter as tk
import time

def generate_numbers():
    number = 0.00

    while 1:
        label.config(text="{:.2f}".format(number))
        number += 0.01
        time.sleep(0.1)
        root.update()
        if(number<100.00):
            continue
        else:
            number = 0

# Create the tkinter window
root = tk.Tk()
root.title("SunMobility")

# Button to start generating numbers
start_button = tk.Button(root, text="Status Of Charge", command=generate_numbers)
start_button.pack()

# Create a label to display the numbers
label = tk.Label(root, font=("Helvetica", 24))
label.pack(pady=20)

# Button to display history
history = tk.Button(root, text="History", command="https://random.com")
history.pack()

# Run the tkinter event loop
root.mainloop()