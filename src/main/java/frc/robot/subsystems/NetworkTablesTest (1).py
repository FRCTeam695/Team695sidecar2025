import array as arr

import tkinter
import tkinter.font

import time
import sys

from networktables import NetworkTables

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


# ****************************************
#
# main program starts here
#
# ****************************************

# set the roborio IP address
ip = "10.6.95.2"

NetworkTables.initialize(server=ip)
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

nt = NetworkTables.getTable("FMSInfo")
nt.addEntryListener(valueChanged)

# create user interface window
G_alliancecolor = "black"
window = tkinter.Tk()
window.title("FMS")
window.geometry('320x240')

# main loop
while True:
    window['background'] = G_alliancecolor
    window.update()
    time.sleep(0.1)
