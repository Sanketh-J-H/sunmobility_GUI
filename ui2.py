import threading
import time
import socket
import tkinter as tk
from tkinter import ttk

import os
from typing import Self

B2T_BMS1 = {
    "B2T_BMS1_Message_sum":0,
    "B2T_TMax":0,
    "B2T_Tmin":0,
    "B2T_ScBatU_H":0,
    "B2T_ScBatU_L":0,
    "B2T_Mode":0,
    "B2T_TMSWorkMode":0,
    "B2T_BMUWorkMode":0,
    "B2T_HighVCtrl":0,
    "B2T_TargetT":0,
    "B2T_TAvg":0,
    "B2T_Life":0
}
keys = [
    "B2T_BMS1_Message_sum",
    "B2T_TMax",
    "B2T_Tmin",
    "B2T_ScBatU_H",
    "B2T_ScBatU_L",
    "B2T_Mode",
    "B2T_TMSWorkMode",
    "B2T_BMUWorkMode",
    "B2T_HighVCtrl",
    "B2T_TargetT",
    "B2T_TAvg",
    "B2T_Life"
]

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
       # self.attributes('-fullscreen', True)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # Specify the filename
        self.filename = "receiveData_for_GUI.py"

            
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3, Page4, Page5, Page6, Page7):
            frame = F(container, self)

            # initializing frame of that object from startpage, page1, page2 respectively with for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    
    # def start_background_thread(self):
    #     # Create and start the background thread
    #     background_thread = threading.Thread(target=self.run_file)
    #     background_thread.daemon = True  # Set the thread as a daemon so it exits when the main program exits
    #     # time.sleep(10000)
    #     background_thread.start()

    # Define the function to run the file
    def run_file(self):
        try:
            # Get the current directory
            current_directory = os.getcwd()
            # Construct the full path to the file
            file_path = os.path.join(current_directory, self.filename)
            
            # Open and execute the file
            with open(file_path, 'r') as file:
                exec(file.read())
        except Exception as e:
            print(f"Error running file: {e}")
  

# first window frame HOME


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of HOME page
        label = ttk.Label(self, text="HOME", font=LARGEFONT)
        label.grid(row=0, column=4, padx=100, pady=30)

        button0 = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(
            StartPage), style="Custom.TButton")
        button0.grid(row=0, column=1, padx=10, pady=(20, 10))

        button1 = ttk.Button(self, text="BMS RLY Command", command=lambda: controller.show_frame(
            Page1), style="Custom.TButton")
        button1.grid(row=1, column=1, padx=10, pady=(20, 10))

        button2 = ttk.Button(self, text="BMS Status", command=lambda: controller.show_frame(
            Page2), style="Custom.TButton")
        button2.grid(row=2, column=1, padx=10, pady=(20, 10))

        button3 = ttk.Button(self, text="VCU Command", command=lambda: controller.show_frame(
            Page3), style="Custom.TButton")
        button3.grid(row=3, column=1, padx=10, pady=(20, 10))

        button4 = ttk.Button(self, text="BMS Value", command=lambda: controller.show_frame(
            Page4), style="Custom.TButton")
        button4.grid(row=4, column=1, padx=10, pady=(20, 10))

        button5 = ttk.Button(self, text="BMS Temp and Voltage",
                             command=lambda: controller.show_frame(Page5), style="Custom.TButton")
        button5.grid(row=5, column=1, padx=10, pady=(20, 10))

        button6 = ttk.Button(self, text="BMS Alarms", command=lambda: controller.show_frame(
            Page6), style="Custom.TButton")
        button6.grid(row=6, column=1, padx=10, pady=(20, 10))

        button7 = ttk.Button(self, text="GB/T Cmd and Status",
                             command=lambda: controller.show_frame(Page7), style="Custom.TButton")
        button7.grid(row=7, column=1, padx=10, pady=(20, 10))

        # Create a new frame for self.tree and use pack
        tree_frame = tk.Frame(self)
        tree_frame.grid(row=3, column=2, rowspan=3,
                        padx=10, pady=10, sticky="nsew")

        data = [
            {"Version": "Version number 1", "Msg_Name": "B2V_SoftVers",
                "Signal_Name": "Major version number", "Signal": "<Major Value>"},
            {"Version": "", "Msg_Name": "",
                "Signal_Name": "Minor version number", "Signal": "<Minor Value>"},
            {"Version": "", "Msg_Name": "",
                "Signal_Name": "Year", "Signal": "<Year Value>"},
            {"Version": "", "Msg_Name": "",
                "Signal_Name": "Month", "Signal": "<Month Value>"},
            {"Version": "", "Msg_Name": "",
                "Signal_Name": "Month", "Signal": "<Month Value>"},
            {"Version": "", "Msg_Name": "",
                "Signal_Name": "Day", "Signal": "<Day Value>"},
            {"Version": "", "Msg_Name": "", "Signal_Name": "", "Signal": ""},
            {"Version": "Version number 2", "Msg_Name": "B2V_HardVers",
                "Signal_Name": "BMU hardware version number (V4.04)", "Signal": "<BMU Value>"},
            {"Version": "", "Msg_Name": "",
                "Signal_Name": "LECU hardware version number (V4.04)", "Signal": "<LECU Value>"}
        ]

        self.tree = ttk.Treeview(tree_frame, columns=(
            "Version", "Msg_Name", "Signal_Name", "Signal"), show="headings", selectmode="none")

        for col in ("Version", "Msg_Name", "Signal_Name", "Signal"):
            self.tree.heading(col, text=col)
            # self.tree.column(col, width=300)
            if col == "Signal_Name":
                self.tree.column(col, width=300)
            else:
                self.tree.column(col, width=150)

        for item in data:
            self.tree.insert("", "end", values=(
                item["Version"], item["Msg_Name"], item["Signal_Name"], item["Signal"]))

        # Configure the Treeview to expand and fill both directions
        self.tree.pack(expand=True, fill=tk.BOTH)

        style = ttk.Style()
        style.configure("Custom.TButton", width=20, padding=(40, 30))

# second window frame BMS RLY Command


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of BMS RLH Command page
        label = ttk.Label(self, text="BMS RLY Command", font=LARGEFONT)
        label.grid(row=0, column=4, padx=700, pady=30)

        button0 = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(
            StartPage), style="Custom.TButton")
        button0.grid(row=0, column=1, padx=10, pady=(20, 10))

        button1 = ttk.Button(self, text="BMS RLY Command", command=lambda: controller.show_frame(
            Page1), style="Custom.TButton")
        button1.grid(row=1, column=1, padx=10, pady=(20, 10))

        button2 = ttk.Button(self, text="BMS Status", command=lambda: controller.show_frame(
            Page2), style="Custom.TButton")
        button2.grid(row=2, column=1, padx=10, pady=(20, 10))

        button3 = ttk.Button(self, text="VCU Command", command=lambda: controller.show_frame(
            Page3), style="Custom.TButton")
        button3.grid(row=3, column=1, padx=10, pady=(20, 10))

        button4 = ttk.Button(self, text="BMS Value", command=lambda: controller.show_frame(
            Page4), style="Custom.TButton")
        button4.grid(row=4, column=1, padx=10, pady=(20, 10))

        button5 = ttk.Button(self, text="BMS Temp and Voltage",
                             command=lambda: controller.show_frame(Page5), style="Custom.TButton")
        button5.grid(row=5, column=1, padx=10, pady=(20, 10))

        button6 = ttk.Button(self, text="BMS Alarms", command=lambda: controller.show_frame(
            Page6), style="Custom.TButton")
        button6.grid(row=6, column=1, padx=10, pady=(20, 10))

        button7 = ttk.Button(self, text="GB/T Cmd and Status",
                             command=lambda: controller.show_frame(Page7), style="Custom.TButton")
        button7.grid(row=7, column=1, padx=10, pady=(20, 10))

        style = ttk.Style()
        style.configure("Custom.TButton", width=20, padding=(40, 30))

# third window frame BMS Status


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of HOME page
        label = ttk.Label(self, text="BMS Status", font=LARGEFONT)
        label.grid(row=0, column=4, padx=700, pady=30)

        button0 = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(
            StartPage), style="Custom.TButton")
        button0.grid(row=0, column=1, padx=10, pady=(20, 10))

        button1 = ttk.Button(self, text="BMS RLY Command", command=lambda: controller.show_frame(
            Page1), style="Custom.TButton")
        button1.grid(row=1, column=1, padx=10, pady=(20, 10))

        button2 = ttk.Button(self, text="BMS Status", command=lambda: controller.show_frame(
            Page2), style="Custom.TButton")
        button2.grid(row=2, column=1, padx=10, pady=(20, 10))

        button3 = ttk.Button(self, text="VCU Command", command=lambda: controller.show_frame(
            Page3), style="Custom.TButton")
        button3.grid(row=3, column=1, padx=10, pady=(20, 10))

        button4 = ttk.Button(self, text="BMS Value", command=lambda: controller.show_frame(
            Page4), style="Custom.TButton")
        button4.grid(row=4, column=1, padx=10, pady=(20, 10))

        button5 = ttk.Button(self, text="BMS Temp and Voltage",
                             command=lambda: controller.show_frame(Page5), style="Custom.TButton")
        button5.grid(row=5, column=1, padx=10, pady=(20, 10))

        button6 = ttk.Button(self, text="BMS Alarms", command=lambda: controller.show_frame(
            Page6), style="Custom.TButton")
        button6.grid(row=6, column=1, padx=10, pady=(20, 10))

        button7 = ttk.Button(self, text="GB/T Cmd and Status",
                             command=lambda: controller.show_frame(Page7), style="Custom.TButton")
        button7.grid(row=7, column=1, padx=10, pady=(20, 10))

        style = ttk.Style()
        style.configure("Custom.TButton", width=20, padding=(40, 30))

# fourth window frame VCU Command


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of HOME page
        label = ttk.Label(self, text="VCU Command", font=LARGEFONT)
        label.grid(row=0, column=4, padx=100, pady=30)

        button0 = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(
            StartPage), style="Custom.TButton")
        button0.grid(row=0, column=1, padx=10, pady=(20, 10))

        button1 = ttk.Button(self, text="BMS RLY Command", command=lambda: controller.show_frame(
            Page1), style="Custom.TButton")
        button1.grid(row=1, column=1, padx=10, pady=(20, 10))

        button2 = ttk.Button(self, text="BMS Status", command=lambda: controller.show_frame(
            Page2), style="Custom.TButton")
        button2.grid(row=2, column=1, padx=10, pady=(20, 10))

        button3 = ttk.Button(self, text="VCU Command", command=lambda: controller.show_frame(
            Page3), style="Custom.TButton")
        button3.grid(row=3, column=1, padx=10, pady=(20, 10))

        button4 = ttk.Button(self, text="BMS Value", command=lambda: controller.show_frame(
            Page4), style="Custom.TButton")
        button4.grid(row=4, column=1, padx=10, pady=(20, 10))

        button5 = ttk.Button(self, text="BMS Temp and Voltage",
                             command=lambda: controller.show_frame(Page5), style="Custom.TButton")
        button5.grid(row=5, column=1, padx=10, pady=(20, 10))

        button6 = ttk.Button(self, text="BMS Alarms", command=lambda: controller.show_frame(
            Page6), style="Custom.TButton")
        button6.grid(row=6, column=1, padx=10, pady=(20, 10))

        button7 = ttk.Button(self, text="GB/T Cmd and Status",
                             command=lambda: controller.show_frame(Page7), style="Custom.TButton")
        button7.grid(row=7, column=1, padx=10, pady=(20, 10))

        # Create a new frame for self.tree and use pack
        tree_frame = tk.Frame(self)
        tree_frame.grid(row=3, column=2, rowspan=3,
                        padx=10, pady=10, sticky="nsew")

        data = [
            {"Function": "VCU Command", "Msg_Name": "V2B_VCUCmd",
                "Signal_Name": "High pressure command", "Signal": "<Major Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Charging Command", "Signal": "<Minor Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Insulation shutdown request", "Signal": "<Year Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Thermal management operating mode", "Signal": "<Month Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "TMS relay command", "Signal": "<Month Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Battery main negative contactor status", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Battery main negative contactor falure", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Motor precharge contactor status (TM/ISG)", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Vehicle end accessory relay status", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Motor total positive contactor status (TM/ISG)", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Motor total positive contactor failure (TM/ISG)", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Auxiliary relay status", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Auxiliary relay failure", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Fast charging positive contactor status", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Fast charging positive contactor failure", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Battery heating contactor status", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Battery heating contactor failure", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "PLC contactor status", "Signal": "<Day Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "VCU life frame", "Signal": "<Day Value>"},
        ]

        self.tree = ttk.Treeview(tree_frame, columns=(
            "Function", "Msg_Name", "Signal_Name", "Signal"), show="headings", selectmode="none")

        for col in ("Function", "Msg_Name", "Signal_Name", "Signal"):
            self.tree.heading(col, text=col)
            # self.tree.column(col, width=300)
            if col == "Signal_Name":
                self.tree.column(col, width=320)
            else:
                self.tree.column(col, width=150)

        for item in data:
            self.tree.insert("", "end", values=(
                item["Function"], item["Msg_Name"], item["Signal_Name"], item["Signal"]))

        # Configure the Treeview to expand and fill both directions
        self.tree.pack(fill=tk.BOTH)

        style = ttk.Style()
        style.configure("Custom.TButton", width=20, padding=(40, 30))

# fifth window frame BMS Value


class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of BMS Value page
        label = ttk.Label(self, text="BMS Value", font=LARGEFONT)
        label.grid(row=0, column=4, padx=100, pady=30)

        button0 = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(
            StartPage), style="Custom.TButton")
        button0.grid(row=0, column=1, padx=10, pady=(20, 10))

        button1 = ttk.Button(self, text="BMS RLY Command", command=lambda: controller.show_frame(
            Page1), style="Custom.TButton")
        button1.grid(row=1, column=1, padx=10, pady=(20, 10))

        button2 = ttk.Button(self, text="BMS Status", command=lambda: controller.show_frame(
            Page2), style="Custom.TButton")
        button2.grid(row=2, column=1, padx=10, pady=(20, 10))

        button3 = ttk.Button(self, text="VCU Command", command=lambda: controller.show_frame(
            Page3), style="Custom.TButton")
        button3.grid(row=3, column=1, padx=10, pady=(20, 10))

        button4 = ttk.Button(self, text="BMS Value", command=lambda: controller.show_frame(
            Page4), style="Custom.TButton")
        button4.grid(row=4, column=1, padx=10, pady=(20, 10))

        button5 = ttk.Button(self, text="BMS Temp and Voltage",
                             command=lambda: controller.show_frame(Page5), style="Custom.TButton")
        button5.grid(row=5, column=1, padx=10, pady=(20, 10))

        button6 = ttk.Button(self, text="BMS Alarms", command=lambda: controller.show_frame(
            Page6), style="Custom.TButton")
        button6.grid(row=6, column=1, padx=10, pady=(20, 10))

        button7 = ttk.Button(self, text="GB/T Cmd and Status",
                             command=lambda: controller.show_frame(Page7), style="Custom.TButton")
        button7.grid(row=7, column=1, padx=10, pady=(20, 10))

        # Create a new frame for self.tree and use pack
        tree_frame = tk.Frame(self)
        tree_frame.grid(row=3, column=2, rowspan=3,
                        padx=10, pady=10, sticky="nsew")
        
        global B2T_BMS1 
        global keys
        data = [
            {"Function": "Thermal Management 1", "Msg_Name": "B2T_BMS1",
                "Signal_Name": "Maximum termperature of single battery", "Signal": B2T_BMS1[keys[0]]},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Minimum temperature of single battery", "Signal": B2T_BMS1[keys[1]]},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "BMS current voltage high byte", "Signal": B2T_BMS1[keys[2]]},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "model", "Signal": B2T_BMS1[keys[3]]},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Control TMS working mode", "Signal": B2T_BMS1[keys[4]]},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "BMS working mode", "Signal": B2T_BMS1[keys[5]]},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "High voltage control command", "Signal": B2T_BMS1[keys[6]]},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Set target temperature", "Signal": B2T_BMS1[keys[7]]},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Average battery temperature", "Signal": B2T_BMS1[keys[8]]},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Target", "Signal": B2T_BMS1[keys[9]]},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "TAverage", "Signal": B2T_BMS1[keys[10]]},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "BMSLife value", "Signal": B2T_BMS1[keys[11]]},
        ]

        self.tree = ttk.Treeview(tree_frame, columns=(
            "Function", "Msg_Name", "Signal_Name", "Signal"), show="headings", selectmode="none")

        for col in ("Function", "Msg_Name", "Signal_Name", "Signal"):
            self.tree.heading(col, text=col)
            # self.tree.column(col, width=300)
            if col == "Signal_Name":
                self.tree.column(col, width=320)
            else:
                self.tree.column(col, width=180)

        for item in data:
            self.tree.insert("", "end", values=(
                item["Function"], item["Msg_Name"], item["Signal_Name"], item["Signal"]))

        # Configure the Treeview to expand and fill both directions
        self.tree.pack(fill=tk.BOTH)

        style = ttk.Style()
        style.configure("Custom.TButton", width=20, padding=(40, 30))

# sixth window frame BMS Temp and Voltage


class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of BMS Temp and Voltage page
        label = ttk.Label(self, text="BMS Temp and Voltage", font=LARGEFONT)
        label.grid(row=0, column=4, padx=100, pady=30)

        button0 = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(
            StartPage), style="Custom.TButton")
        button0.grid(row=0, column=1, padx=10, pady=(20, 10))

        button1 = ttk.Button(self, text="BMS RLY Command", command=lambda: controller.show_frame(
            Page1), style="Custom.TButton")
        button1.grid(row=1, column=1, padx=10, pady=(20, 10))

        button2 = ttk.Button(self, text="BMS Status", command=lambda: controller.show_frame(
            Page2), style="Custom.TButton")
        button2.grid(row=2, column=1, padx=10, pady=(20, 10))

        button3 = ttk.Button(self, text="VCU Command", command=lambda: controller.show_frame(
            Page3), style="Custom.TButton")
        button3.grid(row=3, column=1, padx=10, pady=(20, 10))

        button4 = ttk.Button(self, text="BMS Value", command=lambda: controller.show_frame(
            Page4), style="Custom.TButton")
        button4.grid(row=4, column=1, padx=10, pady=(20, 10))

        button5 = ttk.Button(self, text="BMS Temp and Voltage",
                             command=lambda: controller.show_frame(Page5), style="Custom.TButton")
        button5.grid(row=5, column=1, padx=10, pady=(20, 10))

        button6 = ttk.Button(self, text="BMS Alarms", command=lambda: controller.show_frame(
            Page6), style="Custom.TButton")
        button6.grid(row=6, column=1, padx=10, pady=(20, 10))

        button7 = ttk.Button(self, text="GB/T Cmd and Status",
                             command=lambda: controller.show_frame(Page7), style="Custom.TButton")
        button7.grid(row=7, column=1, padx=10, pady=(20, 10))

        # Create a new frame for self.tree and use pack
        tree_frame = tk.Frame(self)
        tree_frame.grid(row=3, column=2, rowspan=3,
                        padx=10, pady=10, sticky="nsew")

        data = [
            {"Function": "Thermal Management 2", "Msg_Name": "T2B_TMS1",
                "Signal_Name": "Water inlet temperature", "Signal": "<Major Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Outlet temperature", "Signal": "<Major Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "model", "Signal": "<Major Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Control TMS working mode", "Signal": "<Major Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "BMS working mode", "Signal": "<Major Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "TMS relay command", "Signal": "<Major Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "Compressor load ratio", "Signal": "<Major Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "TMS reports fault code", "Signal": "<Major Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "TMS reports vault level", "Signal": "<Major Value>"},
            {"Function": "", "Msg_Name": "",
                "Signal_Name": "TMS life frame", "Signal": "<Major Value>"},
        ]

        self.tree = ttk.Treeview(tree_frame, columns=(
            "Function", "Msg_Name", "Signal_Name", "Signal"), show="headings", selectmode="none")

        for col in ("Function", "Msg_Name", "Signal_Name", "Signal"):
            self.tree.heading(col, text=col)
            # self.tree.column(col, width=300)
            if col == "Signal_Name":
                self.tree.column(col, width=320)
            else:
                self.tree.column(col, width=180)

        for item in data:
            self.tree.insert("", "end", values=(
                item["Function"], item["Msg_Name"], item["Signal_Name"], item["Signal"]))

        # Configure the Treeview to expand and fill both directions
        self.tree.pack(fill=tk.BOTH)

        style = ttk.Style()
        style.configure("Custom.TButton", width=20, padding=(40, 30))

# seventh window frame BMS Alarms


class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of HOME page
        label = ttk.Label(self, text="BMS Alarms", font=LARGEFONT)
        label.grid(row=0, column=4, padx=700, pady=30)

        button0 = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(
            StartPage), style="Custom.TButton")
        button0.grid(row=0, column=1, padx=10, pady=(20, 10))

        button1 = ttk.Button(self, text="BMS RLY Command", command=lambda: controller.show_frame(
            Page1), style="Custom.TButton")
        button1.grid(row=1, column=1, padx=10, pady=(20, 10))

        button2 = ttk.Button(self, text="BMS Status", command=lambda: controller.show_frame(
            Page2), style="Custom.TButton")
        button2.grid(row=2, column=1, padx=10, pady=(20, 10))

        button3 = ttk.Button(self, text="VCU Command", command=lambda: controller.show_frame(
            Page3), style="Custom.TButton")
        button3.grid(row=3, column=1, padx=10, pady=(20, 10))

        button4 = ttk.Button(self, text="BMS Value", command=lambda: controller.show_frame(
            Page4), style="Custom.TButton")
        button4.grid(row=4, column=1, padx=10, pady=(20, 10))

        button5 = ttk.Button(self, text="BMS Temp and Voltage",
                             command=lambda: controller.show_frame(Page5), style="Custom.TButton")
        button5.grid(row=5, column=1, padx=10, pady=(20, 10))

        button6 = ttk.Button(self, text="BMS Alarms", command=lambda: controller.show_frame(
            Page6), style="Custom.TButton")
        button6.grid(row=6, column=1, padx=10, pady=(20, 10))

        button7 = ttk.Button(self, text="GB/T Cmd and Status",
                             command=lambda: controller.show_frame(Page7), style="Custom.TButton")
        button7.grid(row=7, column=1, padx=10, pady=(20, 10))

        style = ttk.Style()
        style.configure("Custom.TButton", width=20, padding=(40, 30))

# eigth window frame GB/T Cmd and Status


class Page7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of HOME page
        label = ttk.Label(self, text="GB/T Cmd and Status", font=LARGEFONT)
        label.grid(row=0, column=4, padx=700, pady=30)

        button0 = ttk.Button(self, text="HOME", command=lambda: controller.show_frame(
            StartPage), style="Custom.TButton")
        button0.grid(row=0, column=1, padx=10, pady=(20, 10))

        button1 = ttk.Button(self, text="BMS RLY Command", command=lambda: controller.show_frame(
            Page1), style="Custom.TButton")
        button1.grid(row=1, column=1, padx=10, pady=(20, 10))

        button2 = ttk.Button(self, text="BMS Status", command=lambda: controller.show_frame(
            Page2), style="Custom.TButton")
        button2.grid(row=2, column=1, padx=10, pady=(20, 10))

        button3 = ttk.Button(self, text="VCU Command", command=lambda: controller.show_frame(
            Page3), style="Custom.TButton")
        button3.grid(row=3, column=1, padx=10, pady=(20, 10))

        button4 = ttk.Button(self, text="BMS Value", command=lambda: controller.show_frame(
            Page4), style="Custom.TButton")
        button4.grid(row=4, column=1, padx=10, pady=(20, 10))

        button5 = ttk.Button(self, text="BMS Temp and Voltage",
                             command=lambda: controller.show_frame(Page5), style="Custom.TButton")
        button5.grid(row=5, column=1, padx=10, pady=(20, 10))

        button6 = ttk.Button(self, text="BMS Alarms", command=lambda: controller.show_frame(
            Page6), style="Custom.TButton")
        button6.grid(row=6, column=1, padx=10, pady=(20, 10))

        button7 = ttk.Button(self, text="GB/T Cmd and Status",
                             command=lambda: controller.show_frame(Page7), style="Custom.TButton")
        button7.grid(row=7, column=1, padx=10, pady=(20, 10))

        style = ttk.Style()
        style.configure("Custom.TButton", width=20, padding=(40, 30))


if __name__ == "__main__":
    
    # Create and run the GUI application
    app = tkinterApp()
    app.run_file()
    app.mainloop()