class BoardObject:
    def __init__(self, the_code, the_value):
        self.__Code = the_code # STRING
        self.__Value = the_value # INTEGER
    def GetCode(self):
        return self.__Code
    def GetValue(self):
        return self.__Value

class Board:
    def __init__(self):
        self.__TheBoard = [] # 2D ARRAY OF BoardObject
        for r in range(10):
            self.__TheBoard.append([])
            for c in range(10):
                self.__TheBoard[r].append(BoardObject('-', 0))
    def GetObject(self, rn, cn):
        return self.__TheBoard[rn][cn]
    def SetObject(self, NewB, rn, cn):
        self.__TheBoard[rn][cn] = NewB
        
    def DisplayBoard(self):
        for r in range(10):
            for c in range(10):
                print(self.GetObject(r,c).GetCode(), end="")
                if c == 9:
                    print("\n", end="")
                else:
                    print(" ", end="")
    

# Main
Object1 = BoardObject("A", 2)
Object2 = BoardObject("B", 3)
Object3 = BoardObject("C", 5)
Object4 = BoardObject("D", 2)
Object5 = BoardObject("E", 7)

TheBoard = Board()
TheBoard.SetObject(Object1, 0, 0)
TheBoard.SetObject(Object2, 9, 9)
TheBoard.SetObject(Object3, 4, 5)
TheBoard.SetObject(Object4, 2, 2)
TheBoard.SetObject(Object5, 8, 7)
TheBoard.DisplayBoard()

TheR = -1
TheC = -1
while(TheR < 0 or TheR > 9):
    TheR = int(input("Input Row: "))
while(TheC < 0 or TheC > 9):
    TheC = int(input("Input Col: "))
ans = TheBoard.GetObject(TheR, TheC)
if ans.GetValue():
    print(ans.GetCode(), ans.GetValue())
else:
    print("Miss")
    
    
