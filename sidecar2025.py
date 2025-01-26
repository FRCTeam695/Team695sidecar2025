import tkinter
import tkinter.font
import math
import time
from networktables import NetworkTables

# cget = part of tkinter that retrieves information
def buttonPressed(button, place):
    print(button.cget("text") + " was chosen at " + place)
    sidecarTables.putString("scoringLocation", place)
    print(place + " chosen")
    print("The location is " + place)

# method for hexagon
def create_hexagon(canvas, x_center, y_center, size):
    points = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = x_center + size * math.cos(angle)
        y = y_center + size * math.sin(angle)
        points.extend([x, y])
    canvas.create_polygon(points, outline = 'blue', fill = 'white', width = 2)

# Set the RoboRIO IP address (from old nt code)
ip = "10.6.95.2"
NetworkTables.initialize(server=ip)
time.sleep(1)

if NetworkTables.isConnected():
    print("Connected to NetworkTables server")
else:
    print("Failed to connect to NetworkTables server")

# creates table and sets to none
sidecarTables = NetworkTables.getTable("sidecarTable")
sidecarTables.putString("scoringLocation", "")

# new interface window
window = tkinter.Tk()
window.title("sidecar695 FRC 2025")
window.geometry('500x500')

# making the canvas widget
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()

# making the hexagon
create_hexagon(canvas, 200, 250, 150)

# button names
buttonLabels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

# font type
button_font = tkinter.font.Font(size=11, weight="bold")

# create each button
# idx, label in enumerate(list): = way in python to make loops
# lambda is needed to pass arguements (when button pressed, do smth)
for idx, label in enumerate(buttonLabels):
    button = tkinter.Button(
        window,
        text=label,
        width=5,
        height=1,
        fg="black",
        bg="white",
        font=button_font,
        command=lambda b=label: buttonPressed(button, b)  # pass arguments
    )
    #btn.config(command=lambda b=btn, l=label: buttonPressed(b, l))
   
    if label=="A":
        button.place(x=185, y=390)
    if label=="B":
        button.place(x=255, y=390)
    if label=="C":
        button.place(x=350, y=350)
    if label=="D":
        button.place(x=380, y=290)
    if label=="E":
        button.place(x=380, y=180)
    if label=="F":
        button.place(x=350, y=120)
    if label=="G":
        button.place(x=255, y=80)
    if label=="H":
        button.place(x=185, y=80)
    if label=="I":
        button.place(x=90, y=120)
    if label=="J":
        button.place(x=60, y=180)
    if label=="K":
        button.place(x=60, y=290)
    if label=="L":
        button.place(x=90, y=350)

# GUI
window.mainloop()