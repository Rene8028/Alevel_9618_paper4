def ReadData():
    TheArray = []
    filename = input("PLease enter a filename")
    try:
        TheFile = open(filename)
        for line in TheFile:
            TheArray.append(line.strip())
        TheFile.close()
    except:
        print("Can't open file")
    return TheArray

def StoreData(DataToStore, FileName):
    try:
        wfile = open(FileName, 'a')
        for item in DataToStore:
            wfile.write(item)
            wfile.write("\n")
        wfile.close()
    except:
        print("Can't write to file")

def SplitData(DataArray):
    red = []
    green = []
    blue = []
    orange = []
    yellow = []
    pink = []
    for line in DataArray:
        Items = line.split(",")
        if Items[1] == "red":
            red.append(Items[0])
        elif Items[1] == "green":
            green.append(Items[0])
        elif Items[1] == "blue":
            blue.append(Items[0])
        elif Items[1] == "orange":
            orange.append(Items[0])
        elif Items[1] == "yellow":
            yellow.append(Items[0])
        elif Items[1] == "pink":
            pink.append(Items[0])
    StoreData(red, "Red.txt")
    StoreData(green, "Green.txt")
    StoreData(blue, "Blue.txt")
    StoreData(orange, "Orange.txt")
    StoreData(yellow, "Yellow.txt")
    StoreData(pink, "Pink.txt")

SplitData(ReadData())
