TreeArray = []
for n in range(50):
    TreeArray.append([-1, -1, -1])
RootPointer = -1
FreeNode = 0

def AddNode(NewNum):
    global TreeArray, RootPointer, FreeNode
    if RootPointer == -1:
        RootPointer = FreeNode
        TreeArray[FreeNode] = [-1, NewNum, -1]
        FreeNode = FreeNode + 1
    else:
        if FreeNode > 49:
            print("The tree is full")
        else:
            TreeArray[FreeNode] = [-1, NewNum, -1]
            prenode = RootPointer
            nextnode = RootPointer
            move = "none"
            while nextnode != -1:
                if NewNum <= TreeArray[nextnode][1]:
                    prenode = nextnode
                    nextnode = TreeArray[prenode][0]
                    move = "left"
                elif NewNum > TreeArray[nextnode][1]:
                    prenode = nextnode
                    nextnode = TreeArray[prenode][2]
                    move = "right"
            if move == "left":
                TreeArray[prenode][0] = FreeNode
            if move == "right":
                TreeArray[prenode][2] = FreeNode
            FreeNode = FreeNode + 1

thefile = open("TreeData.txt")
thedata = thefile.read().split()
for num in thedata:
    AddNode(int(num))

print(TreeArray)

thefile.close()
