import tkinter as tk
import array as arr

import time
import sys

from networktables import NetworkTables

def buttonPressed(button, place):
    print(place + " was chosen")
    sidecarTables.putString("scoringLocation", place)

    for butt in buttons:
        butt['bg'] = 'white'
    button['bg'] = '#00C957'

def scoringLevel(button, place):
    print("Level " + str(place) + " was chosen")
    sidecarTables.putString("scoringLevel", place)

    for butt in buttons2:
        butt['bg'] = 'white'
    button['bg'] = '#9400D3'

#change color of hexagon depending on alliance color
def valueChanged(table, key, value, isNew): 
    global G_alliancecolor
    print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))
    if key == "IsRedAlliance":
        if value == True:
            G_alliancecolor = "#FF3030"
        else:
            G_alliancecolor = "#1E90FF"

def connectionListener(connected, info):
    print(info, "; Connected=%s" % connected)



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

canvas.create_polygon((175,120, 325,120, 400,250, 325,380, 175,380, 100,250), fill = 'gray', outline=G_alliancecolor, width='5') #hexagon

#buttons
buttons = []
buttonLabels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

# create each button
i = 0
while i <= 11:
    button = tk.Button(
        window,
        text=buttonLabels[i],
        bg="white",
        font=('Book Antiqua', 18),
        #command=lambda b=buttonLabels[i]: buttonPressed(buttons[i], b)
        #command=lambda: [buttonPressed(button), change_color]
    )
    buttons.append(button)
    i += 1

buttons[0].place(x=188, y=390, height=50, width=50)
buttons[0].config(command=lambda b="A": buttonPressed(buttons[0], b))

buttons[1].place(x=262, y=390, height=50, width=50)
buttons[1].config(command=lambda b="B": buttonPressed(buttons[1], b))

buttons[2].place(x=359, y=350, height=50, width=50)
buttons[2].config(command=lambda b="C": buttonPressed(buttons[2], b))

buttons[3].place(x=390, y=290, height=50, width=50)
buttons[3].config(command=lambda b="D": buttonPressed(buttons[3], b))

buttons[4].place(x=390, y=160, height=50, width=50)
buttons[4].config(command=lambda b="E": buttonPressed(buttons[4], b))

buttons[5].place(x=359, y=100, height=50, width=50)
buttons[5].config(command=lambda b="F": buttonPressed(buttons[5], b))

buttons[6].place(x=262, y=60, height=50, width=50)
buttons[6].config(command=lambda b="G": buttonPressed(buttons[6], b))

buttons[7].place(x=188, y=60, height=50, width=50)
buttons[7].config(command=lambda b="H": buttonPressed(buttons[7], b))

buttons[8].place(x=90, y=100, height=50, width=50)
buttons[8].config(command=lambda b="I": buttonPressed(buttons[8], b))

buttons[9].place(x=60, y=160, height=50, width=50)
buttons[9].config(command=lambda b="J": buttonPressed(buttons[9], b))

buttons[10].place(x=60, y=290, height=50, width=50)
buttons[10].config(command=lambda b="K": buttonPressed(buttons[10], b))

buttons[11].place(x=90, y=350, height=50, width=50)
buttons[11].config(command=lambda b="L": buttonPressed(buttons[11], b))


#buttons for selecting level
label = tk.Label(window, text = "Select Level", font=('Book Antiqua', 18))
label.place(x=500, y=0, height=75, width=300)
label.config(bg=G_alliancecolor)

buttons2 = []
j = 0
while j <= 3:
    button = tk.Button(
        window,
        text=('L' + str(j+1)),
        bg="white",
        font=('Book Antiqua', 18),
        #command=lambda b=j+1: scoringLevel(b)  # pass arguments
    )
    buttons2.append(button)
    j += 1

buttons2[3].place(x=550, y=100, height=75, width=200)
buttons2[3].config(command=lambda b="4": scoringLevel(buttons2[3], b))

buttons2[2].place(x=550, y=200, height=75, width=200)
buttons2[2].config(command=lambda b="3": scoringLevel(buttons2[2], b))

buttons2[1].place(x=550, y=300, height=75, width=200)
buttons2[1].config(command=lambda b="2": scoringLevel(buttons2[1], b))

buttons2[0].place(x=550, y=400, height=75, width=200)
buttons2[0].config(command=lambda b="1": scoringLevel(buttons2[0], b))

#run
window.mainloop()