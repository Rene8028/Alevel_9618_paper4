class Character:
    # private Name as String
    # private XCoordinate as Integer
    # private YCoordinate as Integer
    def __init__(self, CN, CX, CY):
        self.__Name = CN
        self.__XCoordinate = CX
        self.__YCoordinate = CY

    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange
        


# main
Characters = []
try:
    File = open("Characters.txt", 'r')
    for i in range(0, 10):
        Thename = File.readline().strip()
        TheX = int(File.readline().strip())
        TheY = int(File.readline().strip())
        Characters.append(Character(Thename, TheX, TheY))
    File.close()
except:
    print("Can't open the file!")


Theindex = -1
Target = ""
while Theindex < 0:
    Target = str(input("Please enter a name:")).upper()
    for i in range(0, 10):
        if str(Characters[i].GetName().upper()) == Target:
            Theindex = i

Mvalid = False
while not Mvalid:
    Move = str(input("Please input the move:"))
    if Move.upper() == "W":
        Characters[Theindex].ChangePosition(0,1)
        Mvalid = True
    if Move.upper() == "A":
        Characters[Theindex].ChangePosition(-1,0)
        Mvalid = True
    if Move.upper() == "S":
        Characters[Theindex].ChangePosition(0,-1)
        Mvalid = True
    if Move.upper() == "D":
        Characters[Theindex].ChangePosition(1,0)
        Mvalid = True

print(Characters[Theindex].GetName(), " has changed coordinates to X = ", Characters[Theindex].GetX(), " and Y = ", Characters[Theindex].GetY())

