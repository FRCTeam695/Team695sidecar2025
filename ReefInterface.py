import tkinter as tk
import array as arr
import csv

import time
import sys

from networktables import NetworkTables


def buttonPressed(i):
    global location
    location = buttonLabels[i]

    for butt in buttons:
        if butt['bg'] == '#00C957':
            butt['bg'] = 'white'
    buttons[i].config(bg='#00C957')

    print(location + " was chosen")
    sidecarTables.putString("scoringLocation", location)
    combinationater(location, level)

def scoringLevel(button, place):
    global level

    for butt in buttons2:
        if butt['bg'] == G_alliancecolor:
            butt['bg'] = 'white'
    button['bg'] = G_alliancecolor

    print(place + " was chosen")
    sidecarTables.putString("scoringLevel", place)
    level = place
    combinationater(location, place)


def gamePieceSelect():
    global currentIntakeMode
    global gamePiece

    if currentIntakeMode == 1:
        currentIntakeMode = 2
        gamePiece.config(bg="#00CED1", text="Algae")
        canvas['bg'] = "#00CED1"

        for i in range(1, len(buttons), 2):
            buttons[i].config(bg='gray', command=obsolete)
        buttons2[0].config(bg='gray', command=obsolete)
        buttons2[3].config(bg='gray', command=obsolete)
    else:
        currentIntakeMode = 1
        gamePiece.config(bg="#9400D3", text="Coral")
        canvas['bg'] = "#9400D3"

        for i in range(1, len(buttons), 2):
            buttons[i].config(bg='white', command=lambda b=i: buttonPressed(b))
        buttons2[0].config(bg='white', command=lambda: scoringLevel(buttons2[0], "Level 1"))
        buttons2[3].config(bg='white', command=lambda: scoringLevel(buttons2[3], "Level 4"))

    print("Intake mode " + str(currentIntakeMode) + " was chosen")
    sidecarTables.putNumber("currentIntakeMode", currentIntakeMode)


#change color of hexagon depending on alliance color
def valueChanged(table, key, value, isNew): 
    global G_alliancecolor
    global EventName
    global MatchNumber

    print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))
    if key == "IsRedAlliance":
        if value == True:
            G_alliancecolor = "#DC143C"
        else:
            G_alliancecolor = "#1E90FF"

#log all used combinations
def combinationater(place, level):
    global used_combinations
    new_combination = (place, level)

    if new_combination not in used_combinations:
        used_combinations.add(new_combination)
        print("New combination added: " + str(new_combination))
    else:
        print("Combination " + str(new_combination) + " already used")

def obsolete():
    print("Button obsolete for selected intake mode")

def connectionListener(connected, info):
    print(info, "; Connected=%s" % connected)


# Set the RoboRIO IP address (from old nt code)
ip = "10.6.95.2"

NetworkTables.initialize(server=ip)
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

nt = NetworkTables.getTable("FMSInfo")
nt.addEntryListener(valueChanged)
EventName = nt.getString("EventName", "")
MatchNumber = nt.getNumber("MatchNumber", 0)

time.sleep(1)

if NetworkTables.isConnected():
    print("Connected to NetworkTables server")
else:
    print("Failed to connect to NetworkTables server")


#creates table and sets to none
sidecarTables = NetworkTables.getTable("sidecarTable")
sidecarTables.putString("scoringLocation", "")
sidecarTables.putString("scoringLevel", "")

#set default intake mode to coral
currentIntakeMode = 1
sidecarTables.putNumber("currentIntakeMode", currentIntakeMode)

#set default location and level to nothing
location = ""
level = ""
used_combinations = set()

#window
window = tk.Tk() #create window
window.geometry("800x500") #size
window.title("Reef GUI") #title

#canvas
canvas = tk.Canvas(window, width = 800, height = 500, bg = '#9400D3')
canvas.place(x=0, y=0)
canvas.create_polygon((175,120, 325,120, 400,250, 325,380, 175,380, 100,250), fill = '#D1D1D1', outline=G_alliancecolor, width='5') #hexagon

#reef buttons
buttons = []
buttonLabels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

i = 0
while i <= 11:
    button = tk.Button(
        window,
        text=buttonLabels[i],
        bg="white",
        font=('Book Antiqua', 18),
        command=lambda b=i: buttonPressed(b)
        #command=lambda: [buttonPressed(button), change_color]
    )
    buttons.append(button)
    i += 1

buttons[0].place(x=188, y=390, height=50, width=50)
buttons[1].place(x=262, y=390, height=50, width=50)
buttons[2].place(x=359, y=350, height=50, width=50)
buttons[3].place(x=390, y=290, height=50, width=50)
buttons[4].place(x=390, y=160, height=50, width=50)
buttons[5].place(x=359, y=100, height=50, width=50)
buttons[6].place(x=262, y=60, height=50, width=50)
buttons[7].place(x=188, y=60, height=50, width=50)
buttons[8].place(x=90, y=100, height=50, width=50)
buttons[9].place(x=60, y=160, height=50, width=50)
buttons[10].place(x=60, y=290, height=50, width=50)
buttons[11].place(x=90, y=350, height=50, width=50)


#buttons for selecting level
gamePiece = tk.Button(window, text="Coral", bg="#9400D3", font=("Book Antiqua", 18))
gamePiece.config(command=gamePieceSelect)
gamePiece.place(x=550, y=12, height=75, width=200)

buttons2 = []
j = 0
while j <= 3:
    button = tk.Button(
        window,
        text=('L' + str(j+1)),
        bg="white",
        font=('Book Antiqua', 18),
    )
    buttons2.append(button)
    j += 1

buttons2[3].place(x=550, y=112, height=75, width=200)
buttons2[3].config(command=lambda: scoringLevel(buttons2[3], "Level 4"))

buttons2[2].place(x=550, y=212, height=75, width=200)
buttons2[2].config(command=lambda: scoringLevel(buttons2[2], "Level 3"))

buttons2[1].place(x=550, y=312, height=75, width=200)
buttons2[1].config(command=lambda: scoringLevel(buttons2[1], "Level 2"))

buttons2[0].place(x=550, y=412, height=75, width=200)
buttons2[0].config(command=lambda: scoringLevel(buttons2[0], "Level 1"))

#run
window.mainloop()

#Write to a CSV file after program is finished running
with open("output.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow((EventName, MatchNumber))
    writer.writerows(used_combinations)

print("Data written to output.csv")