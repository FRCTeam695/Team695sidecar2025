import tkinter
import tkinter.font
import time
from networktables import NetworkTables

# cget = part of tkinter that retrieves information
def buttonPressed(button, place):
    print(button.cget("text") + " was chosen at " + place)
    button.configure(fg="white", bg="green")
    sidecarTables.putString("scoringLocation", place)
    print(place + " chosen")
    button.configure(fg="black", bg="white")
    print("The location is " + place)

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
window.geometry('574x574')

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
    button.place(x=250, y=50 + idx * 40)
    if label=="A":
        button.place(x=75, y=225)
    if label=="B":
        button.place(x=75, y=325)
    if label=="C":
        button.place(x=110, y=400)
    if label=="D":
        button.place(x=180, y=450)
    if label=="E":
        button.place(x= 360, y=450)
    if label=="F":
        button.place(x=410, y=400)
    if label=="G":
        button.place(x=450, y=325)
    if label=="H":
        button.place(x=450, y=225)
    if label=="K":
        button.place(x=180, y=100)
    if label=="L":
        button.place(x=110, y=150)

# GUI
window.mainloop()