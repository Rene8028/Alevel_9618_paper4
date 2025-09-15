nullPtr = -1 #CONSTANT
allList = []
startPtr = nullPtr
freeListPtr = 0

class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

def initList(size):
    global startPtr, freeListPtr, allList
    allList.clear()
    startPtr = nullPtr
    freeListPtr = 0
    for i in range(size - 1):
        allList.append(Node("", i + 1))
    allList.append(Node("", nullPtr))
    
def printList():
    print(f'=====List of {len(allList)} elements =====')
    print(f'startPointer: {startPtr}')
    print(f'freeListPointer: {freeListPtr}')
    for i, j in enumerate(allList):
        print(f'Node {i}:')
        print(f'    data: {j.data}')
        print(f'    pointer: {j.pointer}')

def insertNode(newData):
    global startPtr, freeListPtr, allList
    if freeListPtr != nullPtr:
        newPtr = freeListPtr
        allList[newPtr].data = newData
        freeListPtr = allList[freeListPtr].pointer
        thisPtr = startPtr
        prePtr = nullPtr
        while thisPtr != nullPtr and allList[thisPtr].data < newData:
            prePtr = thisPtr
            thisPtr = allList[thisPtr].pointer
        if prePtr == nullPtr:
            allList[newPtr].pointer = startPtr
            startPtr = newPtr
        else:
            allList[newPtr].pointer = allList[prePtr].pointer
            allList[prePtr].pointer = newPtr
        
        
        

initList(7)

insertNode("B")
insertNode("D")
insertNode("A")
insertNode("C")
insertNode("Y")

printList()
