# Riley Poulin (STACK)
# 02/17/2025 -
'''
KENSHI ZONE INFORMER
'''

import tkinter
from tkinter import *
from tkinter import ttk

# Initialize Variables
dataFile = open("data.txt", "r")
dataText = dataFile.read()

# Our class for keeping data live
class DisplayedZone:
    # Initialize our vars
    def __init__(self, filteredText):
        self.zoneName = filteredText[0]
        self.zoneGov = filteredText[1]
        self.zoneRel = filteredText[2]
        self.zoneDesc = filteredText[3]
        self.zoneSqd = filteredText[4]
        self.zoneNest = filteredText[5]
        self.zoneFact = filteredText[6]
        self.zoneShop = filteredText[7]
        self.zoneFert = filteredText[8]
        self.zoneOre = filteredText[9]
        self.zoneGrnd = filteredText[10]

    def __str__(self):
        print(self.zoneName)

class WindowService:
    def __init__(self):
        self.root = Tk()
        self.root.title("Kenshi Zone Informer")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry("1300x900")
        self.root_width = 1300
        self.root_height = 900
        self.root_halfwidth = int(self.root_width / 2)
        self.root_halfheight = int(self.root_height / 2)
        #self.root.resizable(False, False)
        # Set up the window
        self.firstTimeRunning()
        # self.root.bind('<Configure>', self.resizeWindow)
        self.root.mainloop()

    '''
    def resizeWindow(self, event):
        self.new_width = event.width
        self.new_height = event.height
        self.new_halfwidth = int(event.width / 2)
        self.new_halfheight = int(event.height / 2)
        self.lefthalf.configure(width=self.new_halfwidth, height=self.new_halfheight)
        self.righthalf.configure(width=self.new_halfwidth, height=self.new_halfheight)
        self.lefttopthird.configure(width=self.new_halfwidth, height=(self.new_height / 8))
        self.leftmidthird.configure(width=self.new_halfwidth, height=(self.new_height / 2))
        self.leftbottomthird.configure(width=self.new_halfwidth, height=(self.new_height / 2))
    '''


    def firstTimeRunning(self):
        # We're setting up the window frames
        self.mainframe = ttk.Frame(self.root, padding="5 5 5 5")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.pack(fill='both', expand=True)

        self.lefthalf = ttk.Frame(self.mainframe, padding="0 0 5 0")
        self.lefthalf.columnconfigure(0, weight=1)
        self.lefthalf.rowconfigure(0, weight=1)
        self.lefthalf.pack(side='left', fill='both', expand=True)

        self.righthalf = ttk.Frame(self.mainframe, padding="0 5 0 0")
        self.righthalf.columnconfigure(0, weight=1)
        self.righthalf.rowconfigure(0, weight=1)
        self.righthalf.pack(side='right', fill='both', expand=True)

        # containers in the frames
        # right side subframes
        self.righttophalf = ttk.Frame(self.righthalf, padding="0 0 0 0")
        self.righttophalf.pack(side="top")
        self.righttophalf.columnconfigure(0, weight=1)
        self.righttophalf.rowconfigure(0, weight=1)

        self.rightbottomhalf = ttk.Frame(self.righthalf, padding="0 0 0 0")
        self.rightbottomhalf.pack(side="bottom")
        self.rightbottomhalf.columnconfigure(0, weight=1)
        self.rightbottomhalf.rowconfigure(0, weight=1)

        # left side subframes
        self.lefttopthird = ttk.Frame(self.lefthalf, height=80, width=800, padding="0 0 0 0")
        self.lefttopthird.pack_propagate(False)
        self.lefttopthird.pack(side="top", fill="x")
        self.lefttopthird.columnconfigure(0, weight=1)
        self.lefttopthird.rowconfigure(0, weight=0)

        self.leftmidthird = ttk.Frame(self.lefthalf, height=570, padding="0 0 0 0")
        self.leftmidthird.pack(side="top", expand=True, fill="both")
        self.leftmidthird.columnconfigure(0, weight=1)
        self.leftmidthird.rowconfigure(0, weight=1)

        self.leftbottomthird = ttk.Frame(self.lefthalf, height=250, padding="0 0 0 0")
        self.leftbottomthird.pack_propagate(False)
        self.leftbottomthird.pack(side="bottom", fill="x")
        self.leftbottomthird.columnconfigure(0, weight=1)
        self.leftbottomthird.rowconfigure(0, weight=1)

        self.extra_infobox_button_frame = ttk.Frame(self.leftbottomthird, padding="0 0 0 0")
        self.extra_infobox_button_frame.pack(side="left", fill="both", expand=True)

        # initial loadup
        # left side top
        self.selectazone = StringVar(value="Select a zone")
        self.zoneGovernment = StringVar(value=activeZone.zoneGov)
        self.zoneRelations = StringVar(value=activeZone.zoneRel)
        self.drop_box = ttk.Combobox(self.lefttopthird, values=zoneNames, textvariable=self.selectazone, state="readonly", width=60).pack(side="left")
        self.general_notes = ttk.Button(self.lefttopthird, text="General Notes").pack(side="right")
        self.zone_notes = ttk.Button(self.lefttopthird, text="Zone Notes").pack(side="right")
        
        # middle left
        self.infobox = Text(self.leftmidthird)
        self.infobox.pack(fill="both", expand=True)
        self.infobox.insert('1.0', activeZone.zoneDesc)
        self.infobox.configure(state="disabled")

        # left side dynamic box
        self.factions = ttk.Button(self.extra_infobox_button_frame, text="Factions")
        self.factions.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.shops = ttk.Button(self.extra_infobox_button_frame, text="Shops")
        self.shops.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.weather = ttk.Button(self.extra_infobox_button_frame, text="Weather")
        self.weather.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.prospecting = ttk.Button(self.extra_infobox_button_frame, text="Prospecting")
        self.prospecting.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.bounties = ttk.Button(self.extra_infobox_button_frame, text="Bounties")
        self.bounties.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.other = ttk.Button(self.extra_infobox_button_frame, text="Other")
        self.other.pack(expand=True, ipadx=4, ipady=4, fill="both")

        self.extra_infobox = Text(self.leftbottomthird)
        self.extra_infobox.pack(side="left", fill="both", expand=True)
        self.extra_infobox.insert('1.0', activeZone.zoneFact)
        self.extra_infobox.configure(state="disabled")

        # right side
        self.largeImage = PhotoImage(file="img/bz.png")
        self.largeImageLabel = ttk.Label(self.rightbottomhalf, image=self.largeImage)
        self.largeImageLabel.pack(fill="both", expand=True)
        self.smallImage = PhotoImage(file="img/bz_sq.png")
        self.smallImageLabel = ttk.Label(self.righttophalf, image=self.smallImage)
        self.smallImageLabel.pack(side="left", fill="both", expand=True)
        self.mapPreview = PhotoImage(file="img/bz_map.png")
        self.mapPreviewLabel = ttk.Label(self.righttophalf, image=self.mapPreview)
        self.mapPreviewLabel.pack(side="right", fill="both", expand=True)

        
def filterFile(inputZone):
    # Data and vars
    textLength = len(dataText)
    zoneToFind = str("NAME="+inputZone)
    # Find our indices
    startingIndex = dataText.find(zoneToFind)
    endingIndex = dataText.find("END", startingIndex, textLength)
    # Use our indices to form a list version of the data
    filteredText = dataText[startingIndex:endingIndex]
    filteredText = filteredText.splitlines()
    # Remove the fat
    for line in range(len(filteredText)):
        startHere = filteredText[line].find("=") + 1
        endHere = (len(filteredText[line]))
        filteredText[line] = filteredText[line][startHere:endHere]
    return filteredText
    
def giveMeZone(inputZone="Skinners Roam"):
    filteredText = filterFile(inputZone)
    return filteredText

def startWithZone(inputZone="Border Zone"):
    filteredText = filterFile(inputZone)
    return filteredText

if __name__ == "__main__":
    # Initialize to something at all
    zoneNames = ["Border Zone", "Skinner's Roam"]
    filteredText = startWithZone()
    print(filteredText)
    activeZone = DisplayedZone(filteredText)
    mainWindow = WindowService()
