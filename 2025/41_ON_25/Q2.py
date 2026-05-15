class Train:
    def __init__(self, train, route):
        self.__TrainIDNumber = train # STRING
        self.__Route = route # INTEGER

    def GetTrainIDNumber(self):
        return self.__TrainIDNumber
    def GetRoute(self):
        return self.__Route

class Station:
    def __init__(self, station, number):
        self.__StationID = station # STRING
        self.__NumberPlatforms = number # INTEGER
        self.__Trains = [] # ARRAY [0:9] OF Train
        self.__NumberTrains = 0 # INTEGER
    def AddTrain(self, newtrain):
        if self.__NumberPlatforms > self.__NumberTrains:
            self.__Trains.append(newtrain)
            self.__NumberTrains += 1
            return True
        else:
            return False
    def GetTrains(self):
        if self.__NumberTrains == 0:
            return "There are no trains:"
        else:
            result = "The trains at station " + self.__StationID + " are: \n"
            for t in self.__Trains:
                result += t.GetTrainIDNumber() + " on route number " + str(t.GetRoute()) + "\n"
            return result
        

TrainA = Train("12ADV", 134)
TrainB = Train("33ART", 20)
TrainC = Train("9FKF", 3)
TrainD = Train("21VBC", 24)

StationA = Station("STH", 2)
StationB = Station("NTH", 1)

Result1 = StationA.AddTrain(TrainA)
if Result1 == False:
    print("Station is full")
Result2 = StationA.AddTrain(TrainB)
if Result2 == False:
    print("Station is full")
Result3 = StationA.AddTrain(TrainC)
if Result3 == False:
    print("Station is full")
Result4 = StationB.AddTrain(TrainD)
if Result4 == False:
    print("Station is full")

print(StationA.GetTrains())
print(StationB.GetTrains())
    
