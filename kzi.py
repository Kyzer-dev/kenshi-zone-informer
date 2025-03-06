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
CLOSING_TAG = "END_ZONE_INFO" # makes code cleaner to use a constant

genNotesOpen = bool(False)
genNotesActiveWindow = str()

# Our class for keeping data live
class DisplayedZone:
    # Initialize our vars
    def __init__(self, filteredText):
        # all of this is so we can call these easy for the window
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
        self.zoneLargeMap = filteredText[17]
        self.zoneNotes = filteredText[18]

    def __str__(self):
        print(self.zoneName)

    def updateData(self, filteredText):
        # same as above but update the data
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
        self.zoneLargeMap = filteredText[17]
        self.zoneNotes = filteredText[18]

class ZoneNotesWindow:
    # zone notes window
    def __init__(self):
        self.root = tk.Toplevel() # make the window
        self.rememberName = activeZone.zoneName # we need this to search the file later
        self.dynamicTitle = str(self.rememberName + " Notes (saves on close)") # we use the remembered name for the title bar too
        self.root.title(self.dynamicTitle)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry("600x900") # initial size

        self.zoneData = readZoneNotes(self.rememberName) # we get the notes section of the file

        self.font_tuple = ("Calibri", 12, "normal") # so the text doesn't look bad
        self.textblock = Text(self.root) # make the text element
        self.textblock.configure(font = self.font_tuple)
        self.textblock.insert(1.0, self.zoneData) # put the zone notes in the text element
        self.textblock.pack(fill="both", expand=True) # place it on screen

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) # the easiest way to deal with saving the file is on close
        self.root.mainloop()

    def on_closing(self):
        # runs when the window closes; saves the changes
        writeZoneNotes(self.rememberName, self) # call function to write to the file
        self.root.destroy()
        
class GeneralNotesWindow:
    # general notes window
    def __init__(self):
        self.root = tk.Toplevel() # make the window
        self.root.title("General Notes (saves on close)") # set the title
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry("600x900") # initial size

        self.font_tuple = ("Calibri", 12, "normal") # so the text doesn't look bad
        self.textblock = Text(self.root) # make the text element
        self.textblock.configure(font = self.font_tuple)
        self.readtext = readGenNotes() # get the gen notes file and read it to the var
        self.textblock.insert(1.0, self.readtext) # put the notes into the text element
        self.textblock.pack(fill="both", expand=True) # put the text element in the window

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) # easiest way to save the changes is when the window closes
        self.root.mainloop()

    def on_closing(self):
        writeGenNotes(self) # call the function to write to the file
        # global genNotesOpen       # this is leftover from an experiment
        # genNotesOpen = False      # this is leftover from an experiment
        self.root.destroy()    

class BigMapWindow:
    # big map window
    def __init__(self):
        self.root = tk.Toplevel() #make window
        self.rememberName = activeZone.zoneName # need this for the title bar
        self.dynamicTitle = str(self.rememberName + " Map Location") # make titlebar string
        self.root.title(self.dynamicTitle) # set title
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry("900x900") # size of window

        self.prepMapImg = Image.open(activeZone.zoneLargeMap) # load the image using PIL
        self.prepMapImg = self.prepMapImg.resize((900, 900), Image.BILINEAR) # resize it
        self.mapImage = ImageTk.PhotoImage(self.prepMapImg) # change it to a normal image
        self.mapImageLabel = ttk.Label(self.root, image=self.mapImage) # prep the label

        self.mapImageLabel.pack(fill="both", expand=True)

        self.root.mainloop()

class MainWindowService:
    def __init__(self):
        self.root = Tk() # make the main window
        self.root.title("Kenshi Zone Informer") # set the title
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry("1600x790") # initial size
        self.ratio = 0.5625
        self.root_width = 1600 # keep that
        self.root_height = 790 # keep that
        self.root_halfwidth = int(self.root_width / 2) # for setting frame widths
        self.root_halfheight = int(self.root_height / 2) # for setting frame heights
        self.root_lefttopheight = int(self.root_height * 0.088 )
        self.root_leftmidheight = int(self.root_height * 0.633)
        self.root_leftbottomheight = int(self.root_height * 0.277)
        self.root_ratio_height = int(self.root_halfwidth * self.ratio)

        self.mainframe = ttk.Frame(self.root, padding="5 5 5 5") # make the overall frame in the window
        self.lefthalf = ttk.Frame(self.mainframe, width=self.root_halfwidth, height=self.root_height, padding="0 0 5 0") # left half of the window
        self.righthalf = ttk.Frame(self.mainframe, width=self.root_halfwidth, height=self.root_height, padding="0 5 0 0") # right half of the window
        
        self.righttophalf = ttk.Frame(self.righthalf, width=self.root_halfwidth, height=self.root_halfheight, padding="0 0 0 0") # we split the right side into two halves for images
        self.rightbottomhalf = ttk.Frame(self.righthalf, width=self.root_halfwidth, height=self.root_halfheight, padding="0 0 0 0")

        self.lefttopthird = ttk.Frame(self.lefthalf, width=self.root_halfwidth, height=self.root_lefttopheight, padding="0 0 0 0") # we split the left side into thirds
        self.leftmidthird = ttk.Frame(self.lefthalf, width=self.root_halfwidth, height=self.root_leftmidheight, padding="0 0 0 0")
        self.leftbottomthird = ttk.Frame(self.lefthalf, width=self.root_halfwidth, height=self.root_leftbottomheight, padding="0 0 0 0")

        self.extra_infobox_button_frame = ttk.Frame(self.leftbottomthird, width=self.root_halfwidth, height=self.root_leftbottomheight, padding="0 0 0 0") # we need a frame for the buttons on the extra info box

        self.selectazone = StringVar(value=activeZone.zoneName) # default
        self.builtGovStr = str("Local Government: " + activeZone.zoneGov) # make a string for gov label
        self.govString = StringVar(value=self.builtGovStr) 
        self.builtRelStr = str("Default Relations: " + activeZone.zoneRel) # make a string for rel label
        self.relString = StringVar(value=self.builtRelStr)

        self.drop_box = ttk.Combobox(self.lefttopthird, values=zoneNames, textvariable=self.selectazone, state="readonly", width=60) # set up the combo box
        self.general_notes = ttk.Button(self.lefttopthird, text="General Notes", command=openGenNotes) # the button for general notes
        self.zone_notes = ttk.Button(self.lefttopthird, text="Zone Notes", command=openZoneNotes) # zone notes button
        self.factions = ttk.Button(self.extra_infobox_button_frame, text="Factions", command=self.factionButton) # run func on click to change info box
        self.shops = ttk.Button(self.extra_infobox_button_frame, text="Shops", command=self.shopButton) # run func on click to change info box
        self.weather = ttk.Button(self.extra_infobox_button_frame, text="Weather", command=self.weatherButton) # run func on click to change info box
        self.prospecting = ttk.Button(self.extra_infobox_button_frame, text="Prospecting", command=self.prospectingButton) # run func on click to change info box
        self.bounties = ttk.Button(self.extra_infobox_button_frame, text="Bounties", command=self.bountiesButton) # run func on click to change info box
        self.other = ttk.Button(self.extra_infobox_button_frame, text="Other", command=self.otherButton) # run func on click to change info box

        self.gov = ttk.Label(self.lefttopthird, textvariable=self.govString) # label for gov
        
        self.rel = ttk.Label(self.lefttopthird, textvariable=self.relString) # label for relations


        self.infobox = tk.Text(self.leftmidthird, width=98, height=26) # make the main info box element

        self.extra_infobox = tk.Text(self.leftbottomthird) # make the extra info box element

        self.font_tuple = ("Calibri", 12, "normal") # need this to make the text not look bad

        self.infobox.configure(font = self.font_tuple) # set the info boxes to use the better font
        self.extra_infobox.configure(font = self.font_tuple)

        self.prepLrgImg = Image.open(activeZone.zoneLargeImg) # load the image using PIL
        self.prepLrgImg = self.prepLrgImg.resize((self.root_halfwidth, self.root_ratio_height), Image.BILINEAR) # resize it
        self.largeImage = ImageTk.PhotoImage(self.prepLrgImg) # change it to a normal image
        self.largeImageLabel = ttk.Label(self.rightbottomhalf, image=self.largeImage) # prep the label

        self.prepSmImg = Image.open(activeZone.zoneSmallImg) # load the image using PIL
        self.prepSmImg = self.prepSmImg.resize((self.root_halfheight, self.root_halfheight), Image.BILINEAR) # resize it
        self.smallImage = ImageTk.PhotoImage(self.prepSmImg) # change it to a normal image
        self.smallImageLabel = ttk.Label(self.righttophalf, image=self.smallImage) # prep the label

        self.prepSmMap = Image.open(activeZone.zoneSmallMap) # load the image using PIL
        self.prepSmMap = self.prepSmMap.resize((self.root_halfheight, self.root_halfheight), Image.BILINEAR) # resize it
        self.smallMap = ImageTk.PhotoImage(self.prepSmMap) # change it to a normal image
        self.smallMapButton = ttk.Button(self.righttophalf, image=self.smallMap, command=openMapWindow) # prep the label

        '''
        self.largeImage = PhotoImage(file=activeZone.zoneLargeImg) # load the image
        self.largeImageLabel = ttk.Label(self.rightbottomhalf, image=self.largeImage) # make a label
        self.smallImage = PhotoImage(file=activeZone.zoneSmallImg) # load the image
        self.smallImageLabel = ttk.Label(self.rightbottomhalf, image=self.smallImage) # make a label
        self.smallMap = PhotoImage(file=activeZone.zoneSmallMap) # load the image
        self.smallMapLabel = ttk.Label(self.rightbottomhalf, image=self.smallMap) # make a label
        self.largeMap = PhotoImage(file=activeZone.zoneLargeMap) # load the image
        '''

        #self.root.bind('<Configure>', self.resizeWindow)
        self.root.resizable(False, False) # resizing the program is a lot of effort and likes to cause problems
        self.drop_box.bind("<<ComboboxSelected>>", lambda x: giveMeZone(self)) # run a function when the combobox changes (zone is changed)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) # we save the open zone to the file to open to it first on subsequent runs
        self.packItUp() # func; put all the elements in the main window
        self.update()
        self.root.mainloop() 

    def update(self):
        self.root.update()
        self.mainframe.update()
        self.lefthalf.update()
        self.lefttopthird.update()
        self.leftmidthird.update()
        self.leftbottomthird.update()
        self.extra_infobox_button_frame.update()
        self.righthalf.update()
        self.righttophalf.update()
        self.rightbottomhalf.update()
        self.leftmidthird.configure(height=self.root_leftmidheight)
        '''
        # keeping this in case
        self.lefthalf.config(width=self.root_halfwidth, height=self.root_height)
        self.righthalf.config(width=self.root_halfwidth, height=self.root_height)
        self.lefttopthird.config(width=self.root_halfwidth, height=self.root_lefttopheight)
        self.leftmidthird.config(width=self.root_halfwidth, height=self.root_leftmidheight)
        self.leftbottomthird.config(width=self.root_halfwidth, height=self.root_leftbottomheight)
        self.rightbottomhalf.config(width=self.root_halfwidth, height=self.root_halfheight)
        self.righttophalf.config(width=self.root_halfwidth, height=self.root_halfheight)
        '''
        return None

    '''  
    the following is leftover from trying to make resizing work properly
    I tried for a pretty long time to get this stuff to work like I wanted
    while it's kind of there it just doesn't work right

    self.rbh_width = self.rightbottomhalf.winfo_width()
    self.rbh_height = self.rightbottomhalf.winfo_height()
    self.largeImage = Image.open(activeZone.zoneLargeImg)
    self.resized = self.largeImage.resize((self.rbh_width, self.rbh_height))
    self.tk_image = ImageTk.PhotoImage(self.resized)
    self.resize_active = None

    def resizeWindow(self, event):
        if event.width != self.root_width or event.height != self.root_height:
            self.root_width = event.width
            self.root_height = event.height
            self.root_halfwidth = int(self.root_width / 2) # for setting frame widths
            self.root_halfheight = int(self.root_height / 2) # for setting frame heights
            self.root_lefttopheight = int(self.root_height * 0.088 )
            self.root_leftmidheight = int(self.root_height * 0.633)
            self.root_leftbottomheight = int(self.root_height * 0.277)
            self.root_ratio_height = int(self.root_halfwidth * self.ratio)
            self.update()
        return None
    '''

    def factionButton(self):
        # we change the information in the extra box when this is called
        self.extra_infobox.configure(state="normal")
        self.extra_infobox.delete(1.0, tk.END)
        self.extra_infobox.insert(1.0, activeZone.zoneFact)
        self.extra_infobox.configure(state="disabled")

    def shopButton(self):
        # we change the information in the extra box when this is called
        self.extra_infobox.configure(state="normal")
        self.extra_infobox.delete(1.0, tk.END)
        self.extra_infobox.insert(1.0, activeZone.zoneShop)
        self.extra_infobox.configure(state="disabled")

    def weatherButton(self):
        # we change the information in the extra box when this is called
        self.extra_infobox.configure(state="normal")
        self.extra_infobox.delete(1.0, tk.END)
        self.extra_infobox.insert(1.0, activeZone.zoneWthr)
        self.extra_infobox.configure(state="disabled")

    def prospectingButton(self):
        # we change the information in the extra box when this is called
        # we put multiple different datas in here as a combined string
        temp = str(activeZone.zoneFert + "\n" + activeZone.zoneOre + "\n" + activeZone.zoneGrnd)
        self.extra_infobox.configure(state="normal")
        self.extra_infobox.delete(1.0, tk.END)
        self.extra_infobox.insert(1.0, temp)
        self.extra_infobox.configure(state="disabled")

    def bountiesButton(self):
        # we change the information in the extra box when this is called
        self.extra_infobox.configure(state="normal")
        self.extra_infobox.delete(1.0, tk.END)
        self.extra_infobox.insert(1.0, activeZone.zoneBnty)
        self.extra_infobox.configure(state="disabled")

    def otherButton(self):
        # we change the information in the extra box when this is called
        self.extra_infobox.configure(state="normal")
        self.extra_infobox.delete(1.0, tk.END)
        self.extra_infobox.insert(1.0, activeZone.zoneSqd)
        self.extra_infobox.configure(state="disabled")

    def packItUp(self):
        # We're putting all the elements in the window
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.pack(fill='both', expand=True)

        self.lefthalf.columnconfigure(0, weight=1)
        self.lefthalf.rowconfigure(0, weight=1)
        #self.lefthalf.pack(side='left', fill='both', expand=True) # commented out for testing reasons
        self.lefthalf.grid(row=0, column=0, sticky=(W))

        self.righthalf.columnconfigure(0, weight=1)
        self.righthalf.rowconfigure(0, weight=1)
        #self.righthalf.pack(side='right', fill='both', expand=True) # commented out for testing reasons
        self.righthalf.grid(row=0, column=1, sticky=(E))

        # containers in the frames
        # right side subframes
        #self.righttophalf.pack(side="top")
        self.righttophalf.grid(column=0, row=0, sticky=N)
        self.righttophalf.columnconfigure(0, weight=1)
        self.righttophalf.rowconfigure(0, weight=1)

        #self.rightbottomhalf.pack(side="bottom")
        self.rightbottomhalf.grid(column=0, row=1, sticky=S)
        self.rightbottomhalf.columnconfigure(0, weight=1)
        self.rightbottomhalf.rowconfigure(0, weight=1)

        #self.label = ttk.Label(self.rightbottomhalf, image=self.tk_image)
        #self.label.pack(fill="both", expand=True)

        # left side subframes
        self.lefttopthird.pack_propagate(False)
        self.lefttopthird.pack(side="top", fill="x")
        self.lefttopthird.columnconfigure(0, weight=1)
        self.lefttopthird.rowconfigure(0, weight=0)

        self.leftmidthird.pack_propagate(True)
        self.leftmidthird.pack(side="top", expand=True, fill="x")
        self.leftmidthird.columnconfigure(0, weight=1)
        self.leftmidthird.rowconfigure(0, weight=1)

        self.leftbottomthird.pack_propagate(False)
        self.leftbottomthird.pack(side="bottom", fill="x")
        self.leftbottomthird.columnconfigure(0, weight=1)
        self.leftbottomthird.rowconfigure(0, weight=1)

        self.extra_infobox_button_frame.pack(side="left", fill="both", expand=True)

        # pack the elements so they go on screen
        self.drop_box.grid(column=0, row=0, ipady=4, ipadx=83, columnspan=3, sticky=(NW))
        self.general_notes.grid(column=4, row=0, rowspan=3, ipady=24, ipadx=16, sticky=(N))
        self.zone_notes.grid(column=3, row=0, ipady=24, ipadx=18, rowspan=3, sticky=(N))
        self.gov.grid(column=0, row=1, sticky=W, ipadx=4)
        self.rel.grid(column=1, row=1, sticky=W, ipadx=2)
        
        self.infobox.pack(fill="y", expand=True,)
        self.infobox.insert('1.0', activeZone.zoneDesc)
        self.infobox.configure(state="disabled")

        self.factions.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.shops.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.weather.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.prospecting.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.bounties.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.other.pack(expand=True, ipadx=4, ipady=4, fill="both")
        self.extra_infobox.pack(side="left", fill="both", expand=True)
        self.extra_infobox.insert('1.0', activeZone.zoneFact) # put the info in there
        self.extra_infobox.configure(state="disabled") # stops you from writing in it

        self.smallImageLabel.pack(side="left", fill="both", expand=True)
        self.smallMapButton.pack(side="right", fill="both", expand=True)
        self.largeImageLabel.pack(side="top", fill="both", expand=True)
        return None

    def updateData(self):
        # we use this to change whats on screen when the zone changes
        self.infobox.configure(state="normal")
        self.infobox.delete(1.0, tk.END)
        self.infobox.insert(1.0, activeZone.zoneDesc)
        self.infobox.configure(state="disabled")
        self.factionButton() # we could change this later to find the button last clicked but for now this is fine
        self.imageWork()
        return None

    def imageWork(self):
        self.largeImageLabel.destroy()
        self.smallImageLabel.destroy()
        self.smallMapButton.destroy()
        self.prepLrgImg = Image.open(activeZone.zoneLargeImg) # load the image using PIL
        self.prepLrgImg = self.prepLrgImg.resize((self.root_halfwidth, self.root_ratio_height), Image.BILINEAR) # resize it
        self.largeImage = ImageTk.PhotoImage(self.prepLrgImg) # change it to a normal image
        self.largeImageLabel = ttk.Label(self.rightbottomhalf, image=self.largeImage) # prep the label

        self.prepSmImg = Image.open(activeZone.zoneSmallImg) # load the image using PIL
        self.prepSmImg = self.prepSmImg.resize((self.root_halfheight, self.root_halfheight), Image.BILINEAR) # resize it
        self.smallImage = ImageTk.PhotoImage(self.prepSmImg) # change it to a normal image
        self.smallImageLabel = ttk.Label(self.righttophalf, image=self.smallImage) # prep the label

        self.prepSmMap = Image.open(activeZone.zoneSmallMap) # load the image using PIL
        self.prepSmMap = self.prepSmMap.resize((self.root_halfheight, self.root_halfheight), Image.BILINEAR) # resize it
        self.smallMap = ImageTk.PhotoImage(self.prepSmMap) # change it to a normal image
        self.smallMapButton = ttk.Button(self.righttophalf, image=self.smallMap, command=openMapWindow) # prep the label

        self.smallImageLabel.pack(side="left", fill="both", expand=True)
        self.smallMapButton.pack(side="right", fill="both", expand=True)
        self.largeImageLabel.pack(side="top", fill="both", expand=True)
        return None

    def on_closing(self):
        writeLastActiveZone() # call the function to write to the file
        self.root.destroy()

def filterFile(inputZone):
    # Data and vars
    textLength = len(dataText) # length of the text in the file
    zoneToFind = str("NAME="+inputZone) # build a string to find the zone in the file
    # Find our indices
    startingIndex = dataText.find(zoneToFind) # find the first instance of the zone
    endingIndex = dataText.find(CLOSING_TAG, startingIndex, textLength) # find the closing tag
    # Use our indices to form a list version of the data
    filteredText = dataText[startingIndex:endingIndex] # get the section for the zone
    filteredText = filteredText.splitlines() # split into lines for data building
    # Remove the fat; we just need the actual info
    for line in range(len(filteredText)): # for every line
        startHere = filteredText[line].find("=") + 1 # split at the tag delimiter
        endHere = (len(filteredText[line])) # get the length of the line
        filteredText[line] = filteredText[line][startHere:endHere] # get just the actual data the tag is pointing to
    return filteredText # return the list of data

def refreshInfo():
    # we reget the data file every time we change it
    global dataFile # call globals to be sure
    global dataText
    dataFile = open("data.txt", "r") # re-open the file
    dataText = dataFile.read() # re-read it for the variable
    return None # no return necessary

def openMapWindow():
    BigMapWindow()
    return None

def openZoneNotes():
    # open up a zone notes window
    ZoneNotesWindow()
    return None # no return necessary

def writeZoneNotes(inputZone, window):
    # this is similar to the filterFile function but has to be different for writing zone notes
    global dataText # not sure if we need to but we do this anyway

    dataFileWriteMode = open("data.txt", "w") # open the data file as a write-able
    textLength = len(dataText) # length of the file
    zoneToFind = str("NAME="+inputZone) # put together a string to search the file
    startingIndex = dataText.find(zoneToFind) # we need to find the index of the zone name in the file
    endingIndex = dataText.find(CLOSING_TAG, startingIndex, textLength) # we need to find where zone data ends
    notesIndex = (dataText.find("NOTES=", startingIndex, endingIndex) + 6) # get the zone notes index and add 6 (the length of the 'notes=' tag)
    notesToWrite = window.textblock.get('1.0', tk.END) # get the new notes from the window
    newNotes = dataText[:notesIndex] + notesToWrite + dataText[endingIndex:textLength] # make a new block of data to write and replace
    dataFileWriteMode.write(newNotes) # write
    del dataFileWriteMode # delete the variable this function makes or it causes major issues
    refreshInfo() # reload the file
    return None # we don't need to return anything
    
def readZoneNotes(inputZone):
    # while similar to other functions, has a unique purpose
    textLength = len(dataText) # length of the data file
    zoneToFind = str("NAME="+inputZone) # build a string to search for the zone
    startingIndex = dataText.find(zoneToFind) # find where it starts
    endingIndex = dataText.find(CLOSING_TAG, startingIndex, textLength) # find where it ends
    notesIndex = (dataText.find("NOTES=", startingIndex, endingIndex) + 6) # get the zone notes index and add 6 (the length of the 'notes=' tag)
    notesToRead = dataText[notesIndex:endingIndex] # get just the notes part of the notes
    return notesToRead # return to the zone notes window

def openGenNotes():
    # open the gen notes window
    GeneralNotesWindow()
    return None # no return necessary

def readGenNotes():
    # read the gen notes file
    genNotes = open("general_notes.txt", "r")
    genNotesText = genNotes.read()
    return genNotesText # send the text back to the caller

def writeGenNotes(window):
    # write the gen notes file
    genNotes = open("general_notes.txt", "w")
    notesFromWindow = window.textblock.get('1.0', tk.END)
    genNotes.write(notesFromWindow)
    return None # no return necessary

def getZoneNames():
    # we search a specific line index and split it up to get the zone names to populate the combobox
    linedFile = dataText.splitlines() # split the data file into lines
    newList = re.split('=|,', linedFile[2]) # we dont need to specify more because it's just this line
    newList.pop(0) # remove the prefix tag
    return newList # return the list of zones
    
def giveMeZone(window):
    # we run this when we need to change the zone
    inputZone = window.drop_box.get() # get the value of the combobox (the selected zone)
    filteredText = filterFile(inputZone) # run the filterfile for data
    activeZone.updateData(filteredText) # run a func in the displayedzone class to change data
    window.updateData() # run a func that updates the main window's data
    return None # this func doesn't return anything because everyone else gets their info elsewhere

def startWithZone():
    # we use a tag line in the data file to open to the last opened zone
    linedFile = dataText.splitlines() # split the data file into lines
    newString = linedFile[0] # we need the first line
    newList = newString.split("=") # split at the tag delimiter
    newList.pop(0) # remove the tag
    lastZone = newList[0] # we make a string equal to the list's only value
    filteredText = filterFile(lastZone) # filterfile func for the last opened zone
    return filteredText # return filterfile's filteredtext

def writeLastActiveZone():
    # we write to the data file the last zone that was opened on close. It will open to that zone
    dataFileWriteMode = open("data.txt", "w") # open the data file as a write-able
    textLength = len(dataText) # we need the length
    zoneToWrite = str("LAST_ACTIVE_ZONE="+activeZone.zoneName) # build a string to write the first line
    endingIndex = dataText.find("END_LAST_ACTIVE_ZONE") # we need to know where the end is
    endingIndex -= 1 # we subtract 1 because it counts the E as the start
    finalData = zoneToWrite + dataText[endingIndex:textLength] # make the final string
    dataFileWriteMode.write(finalData) # write the final string to the file
    del dataFileWriteMode # delete the variable this function makes or it causes major issues
    return None # we dont need to return anything

if __name__ == "__main__":
    # Initialize to something at all
    zoneNames = getZoneNames()
    filteredText = startWithZone()
    activeZone = DisplayedZone(filteredText)
    mainWindow = MainWindowService()

    
