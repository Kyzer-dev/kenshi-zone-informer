# Riley Poulin (STACK)
# 02/17/2025 -
'''
KENSHI ZONE INFORMER
'''

# Initialize Variables
zoneName = "NONE"
zoneGov = "NONE"
zoneRel = "NONE"
zoneDesc = "NONE"
zoneSqd = []
zoneNest = []
zoneFact = []
zoneShop = []
zoneFert = []
zoneOre = []
zoneGrnd = []

def filterFile(inputZone):
    dataFile = open("data.txt", "r")
    dataText = dataFile.read()
    startingIndex = dataText.find("NAME="+inputZone)
    endingIndex = dataText.find("END", startingIndex)
    filteredText = dataText[startingIndex:endingIndex]
    filteredText = filteredText.splitlines()
    # ALWAYS 11 INDICES
    return filteredText

def workingItem(filteredText, index):
    current = str(filteredText[index])
    new = current.split("=")
    print(new)
    
def giveMe(inputZone="Border Zone"):
    filteredText = filterFile(inputZone)
    for count in range(4):
        workingItem(filteredText, count)
    



giveMe()