import tkinter as tk
import array as arr
import csv
import math
import time
import sys

from networktables import NetworkTables


def buttonPressed(i):
    global location
    location = buttonLabels[i]

    for butt in buttons:
        if butt['bg'] == '#FF1493':
            butt['bg'] = 'white'
    buttons[i].config(bg='#FF1493')

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
    global scoringMode
    global gamePiece

    if scoringMode == "Coral":
        scoringMode = "Algae"
        gamePiece.config(bg="#00CED1", text="Algae")
        canvas['bg'] = "#48D1CC"

        for butt in buttons2:
            butt.config(bg='gray')
    else:
        scoringMode = "Coral"
        gamePiece.config(bg="#9400D3", text="Coral")
        canvas['bg'] = "#ab3fd9"

        for butt in buttons2:
            butt.config(bg='white')

        #when changing back to coral mode, retain color selected
        index = int(level[-1]) - 1
        print(index)
        buttons2[index].config(bg=G_alliancecolor)

    print("Intake mode " + scoringMode + " was chosen")
    sidecarTables.putString("currentIntakeMode", scoringMode)


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


def reset():
    if(scoringMode == "Coral"):
        for butt in buttons:
            butt['bg'] = "white"
        for butt in buttons2:
            butt['bg'] = "white"
    elif(scoringMode == "Algae"):
        for butt in buttons:
            butt['bg'] = "white"
        for butt in buttons2:
            butt['bg'] = "gray"

    sidecarTables.putString("scoringLocation", "")
    sidecarTables.putString("scoringLevel", "")


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
scoringMode = "Coral"
sidecarTables.putString("currentIntakeMode", scoringMode)

#set default location and level to nothing
location = ""
level = ""
used_combinations = set()

#window
window = tk.Tk() #create window
window.geometry("1280x800") #size
window.title("sidecar") #title

#canvas
canvas = tk.Canvas(window, width = 1280, height = 800, bg = '#ab3fd9')
canvas.place(x=0, y=0)
canvas.create_polygon((440,192, 680,192, 800,400, 680,608, 440,608, 320,400), fill = '#D1D1D1', outline=G_alliancecolor, width='5') #hexagon

#reef buttons
buttons = []
buttonLabels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

i = 0
while i <= 11:
    button = tk.Button(
        window,
        text=buttonLabels[i],
        bg="white",
        font=('Book Antiqua', 21),
        command=lambda b=i: buttonPressed(b)
        #command=lambda: [buttonPressed(button), change_color]
    )
    buttons.append(button)
    i += 1

buttons[0].place(x=460, y=628, height=80, width=80) #A
buttons[1].place(x=580, y=628, height=80, width=80) #B
buttons[2].place(x=740, y=550, height=80, width=80) #C
buttons[3].place(x=800, y=445, height=80, width=80) #D
buttons[4].place(x=800, y=270, height=80, width=80) #E
buttons[5].place(x=740, y=160, height=80, width=80) #F
buttons[6].place(x=580, y=92, height=80, width=80) #G
buttons[7].place(x=460, y=92, height=80, width=80) #H
buttons[8].place(x=300, y=160, height=80, width=80) #I
buttons[9].place(x=240, y=270, height=80, width=80) #J
buttons[10].place(x=240, y=445, height=80, width=80) #K
buttons[11].place(x=300, y=550, height=80, width=80) #L


#buttons for selecting level
gamePiece = tk.Button(window, text="Coral", bg="#9400D3", font=("Book Antiqua", 24))
gamePiece.config(command=gamePieceSelect)
gamePiece.place(x=50, y=187, height=160, width=160)

resetButton = tk.Button(window, text="Reset", bg="white", font=("Book Antiqua", 24))
resetButton.config(command=reset)
resetButton.place(x=50, y=453, height=160, width=160)

buttons2 = []
j = 0
while j <= 3:
    button = tk.Button(
        window,
        text=('L' + str(j+1)),
        bg="white",
        font=('Book Antiqua', 30),
    )
    buttons2.append(button)
    j += 1

buttons2[3].place(x=910, y=92, height=130, width=320)
buttons2[3].config(command=lambda: scoringLevel(buttons2[3], "Level 4"))

buttons2[2].place(x=910, y=254, height=130, width=320)
buttons2[2].config(command=lambda: scoringLevel(buttons2[2], "Level 3"))

buttons2[1].place(x=910, y=416, height=130, width=320)
buttons2[1].config(command=lambda: scoringLevel(buttons2[1], "Level 2"))

buttons2[0].place(x=910, y=578, height=130, width=320)
buttons2[0].config(command=lambda: scoringLevel(buttons2[0], "Level 1"))

#run
window.mainloop()

#Write to a CSV file after program is finished running
with open("output.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow((EventName, MatchNumber))
    writer.writerows(used_combinations)

print("Data written to output.csv")