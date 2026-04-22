class EventItem:
    def __init__(self, EN, TY, DI):
        self.__EventName = EN # STRING
        self.__Type = TY # STRING
        self.__Difficulty = DI # INTEGER

    def GetName(self):
        return self.__EventName
        
    def GetEventType(self):
        return self.__Type

    def GetDifficulty(self):
        return self.__Difficulty


class Character:
    def __init__(self, CN, JP, SM, RN, DR):
        self.__CharacterName = CN # INTEGER
        self.__Jump = JP # INTEGER
        self.__Swim = SM # INTEGER
        self.__Run = RN # INTEGER
        self.__Drive = DR # INTEGER

    def GetName(self):
        return self.__CharacterName

    def CalculateScore(self, TheTY, TheDI):
        mylevel = -1
        if TheTY == "jump":
            mylevel = self.__Jump
        if TheTY == "swim":
            mylevel = self.__Swim
        if TheTY == "run":
            mylevel = self.__Run
        if TheTY == "drive":
            mylevel = self.__Drive

        if mylevel >= TheDI:
            return 100
        else:
            return 100 - (TheDI - mylevel) * 20
        
        



# MAIN
Group = [] # ARRAY OF EventItem

Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mile run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on wall", "jump", 4))


ChT = Character("Tarz", 5, 3, 5, 1)
ChG = Character("Geni", 2, 2, 3, 4)

PointT = 0
PointG = 0

for env in Group:
    ScoreT = ChT.CalculateScore(env.GetEventType(), env.GetDifficulty())
    ScoreG = ChG.CalculateScore(env.GetEventType(), env.GetDifficulty())
    if ScoreT == ScoreG:
        print("The event is a draw.")
    if ScoreT > ScoreG:
        PointT = PointT + 1
        print(ChT.GetName(), "have won the event.")
    if ScoreT < ScoreG:
        PointG = PointG + 1
        print(ChG.GetName(), "have won the event.")

if PointT == PointG:
    print("The Group is a draw.")
if PointT > PointG:
    print(ChT.GetName(), "have won with", PointT, "points.")
if PointT < PointG:
    print(ChG.GetName(), "have won with", PointG, "points.")



