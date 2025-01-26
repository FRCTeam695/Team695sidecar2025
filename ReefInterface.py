import tkinter as tk
import array as arr

import time
import sys

from networktables import NetworkTables

def buttonPressed(button, place):
    print(button.cget("text") + " was chosen at " + place)
    sidecarTables.putString("scoringLocation", place)
    print(place + " chosen")
    print("The location is " + place)

def scoringLevel(button, place):
    print(button.cget("text") + " was chosen at " + place)
    sidecarTables.putString("scoringLevel", place)
    print(place + " chosen")
    print("The level is " + place)

def valueChanged(table, key, value, isNew):
    global G_alliancecolor
    print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))
    if key == "IsRedAlliance":
        if value == True:
            G_alliancecolor = "red"
        else:
            G_alliancecolor = "blue"

def connectionListener(connected, info):
    print(info, "; Connected=%s" % connected)

global is_on
is_on = True
def switch(button):
    # Determine is on or off
    if is_on:
        button.config(bg='green')
        is_on = True
    else:
        button.config(bg='gray')
        is_on = False
    is_on = not(is_on)
    


# Set the RoboRIO IP address (from old nt code)
ip = "10.6.95.2"

NetworkTables.initialize(server=ip)
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

nt = NetworkTables.getTable("FMSInfo")
nt.addEntryListener(valueChanged)

time.sleep(1)

if NetworkTables.isConnected():
    print("Connected to NetworkTables server")
else:
    print("Failed to connect to NetworkTables server")

# creates table and sets to none
sidecarTables = NetworkTables.getTable("sidecarTable")
sidecarTables.putString("scoringLocation", "")
sidecarTables.putString("scoringLevel", "")

#window
window = tk.Tk() #create window
window.geometry("800x500") #size
window.title("Reef GUI") #title

#canvas
canvas = tk.Canvas(window, width = 800, height = 500, bg = 'white')
canvas.place(x=0, y=0)

canvas.create_polygon((175,120, 325,120, 400,250, 325,370, 175,370, 100,250), fill = 'gray', outline=G_alliancecolor, width='5') #hexagon


#buttons
buttons = []
buttonLabels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

# create each button
# idx, label in enumerate(list): = way in python to make loops
# lambda is needed to pass arguements (when button pressed, do smth)
i = 0
while i <= 11:
    button = tk.Button(
        window,
        text=buttonLabels[i],
        bg="white",
        font = ('Arial', 18),
        command=lambda b=buttonLabels[i]: buttonPressed(button, b)  # pass arguments
    )
    buttons.append(button)
    i += 1

buttons[0].place(x=185, y=390, height=50, width=50)
buttons[1].place(x=255, y=390, height=50, width=50)
buttons[2].place(x=350, y=350, height=50, width=50)
buttons[3].place(x=380, y=290, height=50, width=50)
buttons[4].place(x=380, y=160, height=50, width=50)
buttons[5].place(x=350, y=100, height=50, width=50)
buttons[6].place(x=255, y=60, height=50, width=50)
buttons[7].place(x=185, y=60, height=50, width=50)
buttons[8].place(x=90, y=100, height=50, width=50)
buttons[9].place(x=60, y=160, height=50, width=50)
buttons[10].place(x=60, y=290, height=50, width=50)
buttons[11].place(x=90, y=350, height=50, width=50)


#buttons for selecting level
label = tk.Label(window, text = "Select Level", font = ('Arial, 18'))
label.place(x=500, y=0, height=75, width=300)
label.config(bg=G_alliancecolor)

button = tk.Button(window, text = "L4", font = ('Arial', 18))
button.place(x=550, y=100, height=75, width=200)
button.config(command=lambda b=button.cget('text'): scoringLevel(button, b))

button = tk.Button(window, text = "L3", font = ('Arial', 18))
button.place(x=550, y=200, height=75, width=200)
button.config(command=lambda b=button.cget('text'): scoringLevel(button, b))

button = tk.Button(window, text = "L2", font = ('Arial', 18))
button.place(x=550, y=300, height=75, width=200)
button.config(command=lambda b=button.cget('text'): scoringLevel(button, b))

button = tk.Button(window, text = "L1", font = ('Arial', 18))
button.place(x=550, y=400, height=75, width=200)
button.config(command=lambda b=button.cget('text'): scoringLevel(button, b))

#run
window.mainloop()




