import array as arr

import tkinter
import tkinter.font

import networktables
import time
import sys

# ****************************************
#
# LevelSelect sends the user clicked level
# and updates the button colors
#
# ****************************************

from tkinter import *
root = Tk()
w = Label(root, text='GeeksForGeeks.org!')
w.pack()
root.mainloop()

"""
def LevelSelect(level):
    global btnLevel
    global nt
    global requestLevel

    for blp in range(3):
        if blp == level-1:
            btnLevel[blp]['bg'] = "orange"
        else:
            btnLevel[blp]['bg'] = "gray"
    # fixup because station is below level 3:
    if level == 3:
        level = 4
    elif level == 4:
        level = 3
    nt.putNumber("requestLevel", level)
    requestLevel = level
    print("requestLevel: " + str(level))
    print("robotLevel:   " + str(nt.getNumber("currentLevel", 1)))
    print("")

# ****************************************
#
# IntakeModeSelect sends the user clicked
# game piece mode (1=cone or 2=cube) and
# updates the button color (yellow or purple)
#
# ****************************************
def IntakeModeSelect():
    global currentIntakeMode
    global btnIntakeMode
    global nt

    if currentIntakeMode == 1:
        currentIntakeMode = 2
        btnIntakeMode.configure(fg="white", bg="purple", text="CUBE")
    else:
        currentIntakeMode = 1
        btnIntakeMode.configure(fg="black", bg="yellow", text="CONE")
    nt.putNumber("currentIntakeMode", currentIntakeMode)

# ****************************************
#
# main program starts here
#
# ****************************************
n = len(sys.argv)
# if any command line arguments specified, set tether mode
if n > 1:
    ip = "172.22.11.2"
    mainbackground = "red"
else:
    ip = "10.6.95.2"
    mainbackground = "white"

networktables.NetworkTables.initialize(server=ip)
nt = networktables.NetworkTables.getDefault().getTable("sidecar695")

# set default intake mode to cone
currentIntakeMode = 1
nt.putNumber("currentIntakeMode", currentIntakeMode)

# set default request level to 1
requestLevel = 1
nt.putNumber("requestLevel", requestLevel)

# set default grid to 0
currentGrid = 0
nt.putNumber("currentGrid", currentGrid)

# create user interface window
window = tkinter.Tk()
window['background'] = mainbackground
window.title("Sidecar695")
window.geometry('840x575')

btnIntakeMode = tkinter.Button(window)
btnIntakeMode['width'] = 10
btnIntakeMode['height'] = 3
btnIntakeMode['fg'] = "black"
btnIntakeMode['bg'] = "yellow"
btnIntakeMode['text'] = "CONE"
btnIntakeMode['font'] = tkinter.font.Font(size=50, weight="bold")
btnIntakeMode['command'] = IntakeModeSelect
btnIntakeMode.place(x=25, y=10)

btnLevel = []
btntxt = [ "Bottom", "Middle", "Top", "Station" ]
ycur = 375
for blp in range(3):
    btnLevel.append(tkinter.Button(window, text=btntxt[blp],
        font=tkinter.font.Font(size=25, weight="bold"),
        width="4", height="1", fg="black", bg="gray",
        command=lambda b=blp+1 : LevelSelect(b)))
    btnLevel[blp]['width'] = 15
    btnLevel[blp]['height'] = 3
    btnLevel[blp].place(x=500, y=ycur)
    ycur = ycur - 175

# station button
#blp = 3
#btnLevel.append(tkinter.Button(window, text=btntxt[blp],
#    font=tkinter.font.Font(size=33, weight="bold"),
#    width="4", height="1", fg="black", bg="gray",
#    command=lambda b=blp+1 : LevelSelect(b)))
#btnLevel[blp]['width'] = 15
#btnLevel[blp]['height'] = 3
#btnLevel[blp].place(x=25, y=350)

# create station override status label
lblStatus = tkinter.Label(window, text="*** STATION OVERRIDE ***")
lblStatus['font'] = tkinter.font.Font(size=25, weight="bold")

# set default requestLevel color
btnLevel[0]['bg'] = "orange"

# main loop
#window.mainloop()
while True:
    window.update()
    if currentIntakeMode != nt.getNumber("currentIntakeMode", 1):
        IntakeModeSelect()
    if requestLevel != nt.getNumber("currentLevel", 1):
        lblStatus.place(x=25, y=350)
    else:
        lblStatus.place_forget()
    time.sleep(0.1)
"""