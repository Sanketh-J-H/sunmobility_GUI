import tkinter as tk


def display_home():
    message_label.config(text="Welcome to the Home Page!")


def display_bms_rly_command():
    message_label.config(text="BMS RLY Command message here...")


def display_bms_status():
    message_label.config(text="BMS Status message here...")


def display_vcu_command():
    message_label.config(text="VCU Command message here...")


def display_bms_value():
    message_label.config(text="BMS Value message here...")


def display_bms_temp_voltage():
    message_label.config(text="BMS Temp and Voltage message here...")


def display_bms_alarms():
    message_label.config(text="BMS Alarms message here...")


def display_gbt_cmd_status():
    message_label.config(text="GB/T Cmd and Status message here...")


# Create main window
root = tk.Tk()
root.title("Sunmobility")

# Create buttons
home_button = tk.Button(root, text="HOME",width=10 , padx=100, pady=20, command=display_home)
bms_rly_command_button = tk.Button(
    root, text="BMS RLY Command",width=10 , padx=100, pady=20, command=display_bms_rly_command
)
bms_status_button = tk.Button(
    root, text="BMS Status", width=10 , padx=100, pady=20, command=display_bms_status
)
vcu_command_button = tk.Button(
    root, text="VCU Command", width=10 , padx=100, pady=20, command=display_vcu_command
)
bms_value_button = tk.Button(
    root, text="BMS Value", padx=100, width=10, pady=20, command=display_bms_value
)
bms_temp_voltage_button = tk.Button(
    root,
    text="BMS Temp and Voltage",
    width=10,
    padx=100,
    pady=20,
    command=display_bms_temp_voltage,
)
bms_alarms_button = tk.Button(
    root, text="BMS Alarms", width=10, padx=100, pady=20, command=display_bms_alarms
)
gbt_cmd_status_button = tk.Button(
    root, text="GB/T Cmd and Status", width=10, padx=100, pady=20, command=display_gbt_cmd_status
)

# Create an empty label to leave space to the left
empty_label = tk.Label(root, text="", width=10)
empty_label.grid(row=2, column=0, padx=10, pady=10)  # Add padx to leave space

# Create an empty label to leave space to the right
empty_label = tk.Label(root, text="", width=10)
empty_label.grid(row=2, column=2, padx=10, pady=10)  # Add padx to leave space

# Pack or grid the  buttons {Shoving it onto the screen}
home_button.grid(row=1, column=1 )
bms_rly_command_button.grid(row=2, column=1 )
bms_status_button.grid(row=3, column=1 )
vcu_command_button.grid(row=4, column=1 )
bms_value_button.grid(row=5, column=1 )
bms_temp_voltage_button.grid(row=6, column=1 )
bms_alarms_button.grid(row=7, column=1 )
gbt_cmd_status_button.grid(row=8, column=1 )

# Create label Widget to display messages
message_label_frame = tk.LabelFrame(root, padx=100, pady=300)
# Add this line to grid the LabelFrame
message_label_frame.grid(row=1, column=3, columnspan=8, rowspan=8)

message_label = tk.Label(
    message_label_frame, text="Click a button to display its message."  
)
# Use pack() instead of grid() for the Label inside the LabelFrame
message_label.pack(padx=10, pady=10)


# Run the main event loop
root.mainloop()