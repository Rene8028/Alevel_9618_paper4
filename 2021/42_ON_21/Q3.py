ArrayNodes = []  # ARRAY
RootPointer = -1   # INTEGER
FreeNode = 0    # INTEGER

for i in range(20):
    ArrayNodes.append([-1, -1, -1])

def AddNode():
    global ArrayNodes, RootPointer, FreeNode
    NodeData = int(input("Enter the data "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")

def PrintAll():
    for OutI in range(20):
        for InI in range(3):
            print(ArrayNodes[OutI][InI], end = "    ")
        print()

def InOrder(RootNode):
    if ArrayNodes[RootNode][0] != -1:
        InOrder(ArrayNodes[RootNode][0])
    print(ArrayNodes[RootNode][1])
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes[RootNode][2])

# MAIN
for i in range(10):
    AddNode()
PrintAll()
InOrder(RootPointer)
                  
