# Riley Poulin (STACK)
# 02/17/2025 -
'''
KENSHI ZONE INFORMER
'''

from tkinter import *
import time
from tkinter import ttk
import tkinter as tk
import re
from PIL import ImageTk, Image, ImageOps, ImageTk

# Initialize Variables
dataFile = open("data.txt", "r")
dataText = dataFile.read()

genNotesOpen = bool(False)
genNotesActiveWindow = str()

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
        self.zoneWthr = filteredText[8]
        self.zoneBnty = filteredText[9]
        self.zoneOthr = filteredText[10]
        self.zoneFert = filteredText[11]
        self.zoneOre = filteredText[12]
        self.zoneGrnd = filteredText[13]
        self.zoneLargeImg = filteredText[14]
        self.zoneSmallImg = filteredText[15]
        self.zoneSmallMap = filteredText[16]
        self.zoneSmallMap = filteredText[17]
        self.zoneNotes = filteredText[18]

    def __str__(self):
        print(self.zoneName)

    def updateData(self, filteredText):
        self.zoneName = filteredText[0]
        self.zoneGov = filteredText[1]
        self.zoneRel = filteredText[2]
        self.zoneDesc = filteredText[3]
        self.zoneSqd = filteredText[4]
        self.zoneNest = filteredText[5]
        self.zoneFact = filteredText[6]
        self.zoneShop = filteredText[7]
        self.zoneWthr = filteredText[8]
        self.zoneBnty = filteredText[9]
        self.zoneOthr = filteredText[10]
        self.zoneFert = filteredText[11]
        self.zoneOre = filteredText[12]
        self.zoneGrnd = filteredText[13]
        self.zoneLargeImg = filteredText[14]
        self.zoneSmallImg = filteredText[15]
        self.zoneSmallMap = filteredText[16]
        self.zoneSmallMap = filteredText[17]
        self.zoneNotes = filteredText[18]

class ZoneNotesWindow:
    def __init__(self):
        self.root = Tk()
        self.rememberName = activeZone.zoneName
        self.dynamicTitle = str(self.rememberName + " Notes (saves on close)")
        self.root.title(self.dynamicTitle)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry("600x900")

        self.zoneData = readZoneNotes(self.rememberName)

        self.font_tuple = ("Calibri", 12, "normal")
        self.textblock = Text(self.root)
        self.textblock.configure(font = self.font_tuple)
        self.textblock.insert(1.0, self.zoneData)
        self.textblock.pack(fill="both", expand=True)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        writeZoneNotes(self.rememberName, self)
        self.root.destroy()
        

class GeneralNotesWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("General Notes (saves on close)")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry("600x900")

        self.font_tuple = ("Calibri", 12, "normal")
        self.textblock = Text(self.root)
        self.textblock.configure(font = self.font_tuple)
        self.readtext = readGenNotes()
        self.textblock.insert(1.0, self.readtext)
        self.textblock.pack(fill="both", expand=True)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        writeGenNotes(self)
        global genNotesOpen
        genNotesOpen = False
        self.root.destroy()    
        
class MainWindowService:
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

        self.mainframe = ttk.Frame(self.root, padding="5 5 5 5")
        self.lefthalf = ttk.Frame(self.mainframe, padding="0 0 5 0")
        self.righthalf = ttk.Frame(self.mainframe, padding="0 5 0 0")
        self.righttophalf = ttk.Frame(self.righthalf, padding="0 0 0 0")
        self.rightbottomhalf = ttk.Frame(self.righthalf, padding="0 0 0 0")

        self.lefttopthird = ttk.Frame(self.lefthalf, height=80, width=800, padding="0 0 0 0")
        self.leftmidthird = ttk.Frame(self.lefthalf, height=570, padding="0 0 0 0")
        self.leftbottomthird = ttk.Frame(self.lefthalf, height=250, padding="0 0 0 0")
        self.extra_infobox_button_frame = ttk.Frame(self.leftbottomthird, padding="0 0 0 0")

        self.selectazone = StringVar(value="Border Zone")

        self.drop_box = ttk.Combobox(self.lefttopthird, values=zoneNames, textvariable=self.selectazone, state="readonly", width=60)
        self.general_notes = ttk.Button(self.lefttopthird, text="General Notes", command=openGenNotes)
        self.zone_notes = ttk.Button(self.lefttopthird, text="Zone Notes", command=openZoneNotes)
        self.factions = ttk.Button(self.extra_infobox_button_frame, text="Factions", command=self.factionButton)
        self.shops = ttk.Button(self.extra_infobox_button_frame, text="Shops", command=self.shopButton)
        self.weather = ttk.Button(self.extra_infobox_button_frame, text="Weather", command=self.weatherButton)
        self.prospecting = ttk.Button(self.extra_infobox_button_frame, text="Prospecting", command=self.prospectingButton)
        self.bounties = ttk.Button(self.extra_infobox_button_frame, text="Bounties", command=self.bountiesButton)
        self.other = ttk.Button(self.extra_infobox_button_frame, text="Other", command=self.otherButton)

        self.infobox = tk.Text(self.leftmidthird)
        self.extra_infobox = tk.Text(self.leftbottomthird)

        self.font_tuple = ("Calibri", 12, "normal")
        self.infobox.configure(font = self.font_tuple)
        self.extra_infobox.configure(font = self.font_tuple)

        #self.root.resizable(False, False)
        self.packItUp()
        self.drop_box.bind("<<ComboboxSelected>>", lambda x: giveMeZone(self))
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

    def factionButton(self):
        self.extra_infobox.configure(state="normal")
        self.extra_infobox.delete(1.0, tk.END)
        self.extra_infobox.insert(1.0, activeZone.zoneFact)
        self.extra_infobox.configure(state="disabled")

    def shopButton(self):
        self.extra_infobox.configure(state="normal")
        self.extra_infobox.delete(1.0, tk.END)
        self.extra_infobox.insert(1.0, activeZone.zoneShop)
        self.extra_infobox.configure(state="disabled")

    def weatherButton(self):
        self.extra_infobox.configure(state="normal")
        self.extra_infobox.delete(1.0, tk.END)
        self.extra_infobox.insert(1.0, activeZone.zoneWthr)
        self.extra_infobox.configure(state="disabled")

    def prospectingButton(self):
        temp = str(activeZone.zoneFert + "\n" + activeZone.zoneOre + "\n" + activeZone.zoneGrnd)
        self.extra_infobox.configure(state="normal")
        self.extra_infobox.delete(1.0, tk.END)
        self.extra_infobox.insert(1.0, temp)
        self.extra_infobox.configure(state="disabled")

    def bountiesButton(self):
        self.extra_infobox.configure(state="normal")
        self.extra_infobox.delete(1.0, tk.END)
        self.extra_infobox.insert(1.0, activeZone.zoneBnty)
        self.extra_infobox.configure(state="disabled")

    def otherButton(self):
        self.extra_infobox.configure(state="normal")
        self.extra_infobox.delete(1.0, tk.END)
        self.extra_infobox.insert(1.0, activeZone.zoneSqd)
        self.extra_infobox.configure(state="disabled")

    def packItUp(self):
        # We're setting up the window frames
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.pack(fill='both', expand=True)

        self.lefthalf.columnconfigure(0, weight=1)
        self.lefthalf.rowconfigure(0, weight=1)
        self.lefthalf.pack(side='left', fill='both', expand=True)

        self.righthalf.columnconfigure(0, weight=1)
        self.righthalf.rowconfigure(0, weight=1)
        self.righthalf.pack(side='right', fill='both', expand=True)

        # containers in the frames
        # right side subframes
        self.righttophalf.pack(side="top")
        self.righttophalf.columnconfigure(0, weight=1)
        self.righttophalf.rowconfigure(0, weight=1)

        self.rightbottomhalf.pack(side="bottom")
        self.rightbottomhalf.columnconfigure(0, weight=1)
        self.rightbottomhalf.rowconfigure(0, weight=1)

        # left side subframes
        self.lefttopthird.pack_propagate(False)
        self.lefttopthird.pack(side="top", fill="x")
        self.lefttopthird.columnconfigure(0, weight=1)
        self.lefttopthird.rowconfigure(0, weight=0)

        self.leftmidthird.pack(side="top", expand=True, fill="both")
        self.leftmidthird.columnconfigure(0, weight=1)
        self.leftmidthird.rowconfigure(0, weight=1)

        self.leftbottomthird.pack_propagate(False)
        self.leftbottomthird.pack(side="bottom", fill="x")
        self.leftbottomthird.columnconfigure(0, weight=1)
        self.leftbottomthird.rowconfigure(0, weight=1)

        self.extra_infobox_button_frame.pack(side="left", fill="both", expand=True)

        self.drop_box.pack(side="left")
        self.general_notes.pack(side="right")
        self.zone_notes.pack(side="right")
        
        self.infobox.pack(fill="both", expand=True)
        self.infobox.insert('1.0', activeZone.zoneDesc)
        self.infobox.configure(state="disabled")

        self.factions.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.shops.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.weather.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.prospecting.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.bounties.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.other.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.extra_infobox.pack(side="left", fill="both", expand=True)
        self.extra_infobox.insert('1.0', activeZone.zoneFact)
        self.extra_infobox.configure(state="disabled")

    def updateData(self):
        self.infobox.configure(state="normal")
        self.infobox.delete(1.0, tk.END)
        self.infobox.insert(1.0, activeZone.zoneDesc)
        self.infobox.configure(state="disabled")
        self.factionButton()

def filterFile(inputZone):
    # Data and vars
    textLength = len(dataText)
    zoneToFind = str("NAME="+inputZone)
    # Find our indices
    startingIndex = dataText.find(zoneToFind)
    endingIndex = dataText.find("END_ZONE_INFO", startingIndex, textLength)
    # Use our indices to form a list version of the data
    filteredText = dataText[startingIndex:endingIndex]
    filteredText = filteredText.splitlines()
    # Remove the fat
    for line in range(len(filteredText)):
        startHere = filteredText[line].find("=") + 1
        endHere = (len(filteredText[line]))
        filteredText[line] = filteredText[line][startHere:endHere]
    return filteredText

def refreshInfo():
    global dataFile
    global dataText
    dataFile = open("data.txt", "r")
    dataText = dataFile.read()
    return None

def openZoneNotes():
    ZoneNotesWindow()
    return None

def writeZoneNotes(inputZone, window):
    CLOSING_TAG = "END_ZONE_INFO"
    global dataText

    dataFileWriteMode = open("data.txt", "w")
    textLength = len(dataText)
    zoneToFind = str("NAME="+inputZone)
    startingIndex = dataText.find(zoneToFind)
    endingIndex = dataText.find(CLOSING_TAG, startingIndex, textLength)
    notesIndex = (dataText.find("NOTES=", startingIndex, endingIndex) + 6) # get the zone notes index and add 6 (the length of the 'notes=' tag)
    notesToWrite = window.textblock.get('1.0', tk.END)
    newNotes = dataText[:notesIndex] + notesToWrite + dataText[endingIndex:textLength]
    dataFileWriteMode.write(newNotes)
    del dataFileWriteMode
    refreshInfo()
    return None
    
def readZoneNotes(inputZone):
    textLength = len(dataText)
    zoneToFind = str("NAME="+inputZone)
    startingIndex = dataText.find(zoneToFind)
    endingIndex = dataText.find("END_ZONE_INFO", startingIndex, textLength)
    notesIndex = (dataText.find("NOTES=", startingIndex, endingIndex) + 6) # get the zone notes index and add 6 (the length of the 'notes=' tag)
    notesToRead = dataText[notesIndex:endingIndex]
    return notesToRead

def openGenNotes():
    GeneralNotesWindow()
    return None

def readGenNotes():
    genNotes = open("general_notes.txt", "r")
    genNotesText = genNotes.read()
    return genNotesText

def writeGenNotes(window):
    genNotes = open("general_notes.txt", "w")
    notesFromWindow = window.textblock.get('1.0', tk.END)
    genNotes.write(notesFromWindow)
    return None

def getZoneNames():
    linedFile = dataText.splitlines()
    newList = re.split('=|,', linedFile[2]) # we dont need to specify more because it's just this line
    newList.pop(0)
    return newList
    
def giveMeZone(window):
    inputZone = window.drop_box.get()
    filteredText = filterFile(inputZone)
    activeZone.updateData(filteredText)
    window.updateData()
    return None

def startWithZone(inputZone="Border Zone"):
    filteredText = filterFile(inputZone)
    return filteredText

if __name__ == "__main__":
    # Initialize to something at all
    zoneNames = getZoneNames()
    filteredText = startWithZone()
    activeZone = DisplayedZone(filteredText)
    mainWindow = MainWindowService()

    
