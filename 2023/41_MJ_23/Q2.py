class Vehicle:
    def __init__(self, TheID, TheMaxSpeed, TheIncreaseAmount):
        self.__ID = TheID  # STRING
        self.__MaxSpeed = TheMaxSpeed  # INTEGER
        self.__IncreaseAmount = TheIncreaseAmount  # INTEGER
        self.__CurrentSpeed = 0  # INTEGER
        self.__HorizontalPosition = 0  # INTEGER

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, TheSpeed):
        self.__CurrentSpeed = TheSpeed
    def SetHorizontalPosition(self, ThePosition):
        self.__HorizontalPosition = ThePosition

    def IncreaseSpeed(self):
        ResultSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if ResultSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        else:
            self.__CurrentSpeed = ResultSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed

    def OutputCurrentPosition(self):
        print("Current position is", self.__HorizontalPosition)
        print("Current speed is", self.__CurrentSpeed) 
        
class Helicopter(Vehicle):
    def __init__(self, TheID, TheMaxSpeed, TheIncreaseAmount, TheVerticalChange, TheMaxHeight):
        Vehicle.__init__(self, TheID, TheMaxSpeed, TheIncreaseAmount)
        self.__VerticalPosition = 0  # INTEGER
        self.__VerticalChange = TheVerticalChange  # INTEGER
        self.__MaxHeight = TheMaxHeight  # INTEGER

    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if(self.__VerticalPosition > self.__MaxHeight):
            self.__VerticalPosition = MaxHeight
        Vehicle.IncreaseSpeed(self)

    def OutputCurrentPosition(self):
        Vehicle.OutputCurrentPosition(self)
        print("Current verticalposition = ", self.__VerticalPosition)

TheCar = Vehicle("Tiger", 100, 20)
TheHeli = Helicopter("Lion", 350, 40, 3, 100)
TheCar.IncreaseSpeed()
TheCar.IncreaseSpeed()
TheCar.OutputCurrentPosition()
print("")
TheHeli.IncreaseSpeed()
TheHeli.IncreaseSpeed()
TheHeli.OutputCurrentPosition()

        
