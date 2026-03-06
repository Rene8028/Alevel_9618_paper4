class Balloon:
#Health as integer
#Colour as string
#DefenceItem as string
    def __init__(self, PDefenceItem, PColour):
        self.__Health = 100
        self.__Colour = PColour
        self.__DefenceItem = PDefenceItem
    def GetDefenceItem(self):
        return self.__DefenceItem
    def ChangeHealth(self, HVaule):
        self.__Health = self.__Health + HVaule
    def CheckHealth(self):
        if self.__Health > 0:
            return False
        else:
            return True

def Defend(TheBalloon):
    TheStrength = input("Enter the strength of opponent: ")
    TheBalloon.ChangeHealth(-int(TheStrength))
    print("Your defence items: ", TheBalloon.GetDefenceItem())
    if TheBalloon.CheckHealth() == True:  
        print("Defence failed")
    else:
        print("Defence succeeded")
    return TheBalloon

MyDefenceItem = input("Enter your defence items: ")
MyColour = input("Enter your colour: ")
Balloon1 = Balloon(MyDefenceItem, MyColour)
Balloon1 = Defend(Balloon1)
