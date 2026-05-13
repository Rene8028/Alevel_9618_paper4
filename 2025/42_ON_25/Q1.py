class Bird:
    def __init__(self, distnceph, species):
        self.__DistncePH = distnceph  # REAL
        self.__Species = species  # STRING
        self.__XPosition = 0  # REAL
        self.__YPosition = 0  # REAL
    def GetSpecies(self):
        return self.__Species
    def GetPosition(self):
        return "X = " + str(self.__XPosition) + " Y = " + str(self.__YPosition)
    def Move(self, flydir, flytime):
        travelled = (self.__DistncePH / 60) * flytime
        if flydir == "N":
            self.__YPosition = self.__YPosition + travelled
        if flydir == "S":
            self.__YPosition = self.__YPosition - travelled
        if flydir == "E":
            self.__XPosition = self.__XPosition + travelled
        if flydir == "W":
            self.__XPosition = self.__XPosition - travelled

BirdA = Bird(71, 'Cockatiel')
BirdB = Bird(56, 'Macaw')
print(BirdA.GetSpecies())
print(BirdA.GetPosition())
print(BirdB.GetSpecies())
print(BirdB.GetPosition())

bird_move = input("Please enter the species of the bird to move: ")
dir_move = input("Please input the direction to move: ")
time_move = input("Please input minutes the bird moved: ")

if bird_move == "Cockatiel":
    BirdA.Move(dir_move, int(time_move))
    print(BirdA.GetPosition())
if bird_move == "Macaw":
    BirdB.Move(dir_move, int(time_move))
    print(BirdB.GetPosition())


