HighScores = [] # 2D ARRAY OF STRING
for i in range(7):
    HighScores.append(["", "", ""])


def ReadData():
    NewHighScores = []
    for i in range(7):
        NewHighScores.append(["", "", ""])
    try:
        Thefile = open("HighScoreTable.txt")
        for index in range(7):
            NewHighScores[index][0] = Thefile.readline().strip()
            NewHighScores[index][1] = Thefile.readline().strip()
            NewHighScores[index][2] = Thefile.readline().strip()
        return NewHighScores
    except:
        print("[ERROR] Can't open the file")


def OutputHighScores(TheArray):
    for player in TheArray:
        print(player[0], "reached level", player[1], "with a score of", player[2])


def SortScores(TheArray):
    SortedHighScores = TheArray
    move = True
    while move:
        move = False
        for i in range(6, 0, -1):
            cur = SortedHighScores[i]
            pre = SortedHighScores[i - 1]
            if cur[1] > pre[1]:
                SortedHighScores[i - 1] = cur
                SortedHighScores[i] = pre
                move = True
            else:
                if cur[1] == pre[1] and cur[2]> pre[2]:
                    SortedHighScores[i - 1] = cur
                    SortedHighScores[i] = pre
                    move = True
    return SortedHighScores

HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
HighScores = SortScores(HighScores)
print("After")
OutputHighScores(HighScores)

