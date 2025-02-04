import tkinter as tk
import array as arr

import time
import sys

from networktables import NetworkTables

#network tables
ip = "10.6.95.2"
NetworkTables.initialize(server=ip)
time.sleep(1)

if NetworkTables.isConnected():
    print("Connected to NetworkTables server")
else:
    print("Failed to connect to NetworkTables server")


window = tk.Tk() #create window
window.geometry("400x400") #size
window.title("tracker") #title

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=1)
window.rowconfigure(8, weight=1)


# Create a 3x3 2D array initialized with 0s
matrix = [[False for _ in range(8)] for _ in range(4)]

# Initialize an empty 2D array
labels = []

# Use nested for loops to populate the array
for i in range(9):
    row = []  # Create a new row for each iteration
    for j in range(5):
        if i == 0 or j == 0:
            label = tk.Label(window, background="white")
        else:
            label = tk.Label(window, background="red")
        label.grid(row=i, column=j, sticky= 'nsew')
        row.append(label)  # Append a value (here, 0) to the row
    labels.append(row)  # Append the row to the 2D array

labels[1][0].config(text="A")
labels[2][0].config(text="B")
labels[3][0].config(text="C")
labels[4][0].config(text="D")
labels[5][0].config(text="E")
labels[6][0].config(text="F")
labels[7][0].config(text="G")
labels[8][0].config(text="H")

labels[0][1].config(text="L1")
labels[0][2].config(text="L2")
labels[0][3].config(text="L3")
labels[0][4].config(text="L4")


window.mainloop()