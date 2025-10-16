# CONSTANT
NullPointer = -1

class TreeNode:
    def __init__(self):
        self.Data = ""
        self.LeftPtr = -1
        self.RightPtr = -1

TreeList = []
RootPointer = NullPointer
FreePtr = 0
TreeSize = 0

def InitialiseTree(size):
    global TreeList, TreeSize
    TreeSize = size
    for i in range(TreeSize):
        TreeList.append(TreeNode())
        TreeList[i].LeftPtr = i + 1
    TreeList[TreeSize - 1].LeftPtr = -1

def PrintTree():
    print(f'----- Tree of {TreeSize} Nodes -----')
    print(f'RootPointer: {RootPointer}')
    print(f'FreePointer: {FreePtr}')
    print("----- TreeList -----")
    for i in range(TreeSize):
        print(f'Index: {i}')
        print(f'  Data: {TreeList[i].Data} Left: {TreeList[i].LeftPtr} Right: {TreeList[i].RightPtr}')
    print("----- EndTree -----")
    
def AddNode(ndata):
    global TreeList, FreePtr, RootPointer
    NewIndex = FreePtr
    if NewIndex != NullPointer:
        FreePtr = TreeList[NewIndex].LeftPtr
        TreeList[NewIndex].Data = ndata
        TreeList[NewIndex].LeftPtr = NullPointer
        TreeList[NewIndex].RightPtr = NullPointer
        
        if RootPointer == NullPointer:
            RootPointer = NewIndex
        else:
            ThisPtr = RootPointer
            while ThisPtr != NullPointer:
                PrePtr = ThisPtr
                if TreeList[ThisPtr].Data > ndata:
                    ThisPtr = TreeList[ThisPtr].LeftPtr
                else:
                    ThisPtr = TreeList[ThisPtr].RightPtr
            if TreeList[PrePtr].Data > ndata:
                TreeList[PrePtr].LeftPtr = NewIndex
            else:
                TreeList[PrePtr].RightPtr = NewIndex
        return True
    else:
        return False

def OrderPrint(TheOrder, TheRootPtr = -1):
    is_top = False
    if TheRootPtr == -1:
        TheRootPtr = RootPointer
        is_top = True
        print(f'The {TheOrder} order tree: ', end = "")

    if TheOrder == 1:
        print(TreeList[TheRootPtr].Data, end = " ")
    if TreeList[TheRootPtr].LeftPtr != -1:
        OrderPrint(TheOrder, TreeList[TheRootPtr].LeftPtr)
    if TheOrder == 2:
        print(TreeList[TheRootPtr].Data, end = " ")
    if TreeList[TheRootPtr].RightPtr != -1:
        OrderPrint(TheOrder, TreeList[TheRootPtr].RightPtr)
    if TheOrder == 3:
        print(TreeList[TheRootPtr].Data, end = " ")
    if is_top:
        print()
    
InitialiseTree(7)
addstr = "FCSBER"
for iword in addstr:
    if not AddNode(iword):
        print("ERROR: FULL!!!")
PrintTree()
OrderPrint(1)
OrderPrint(2)
OrderPrint(3)
