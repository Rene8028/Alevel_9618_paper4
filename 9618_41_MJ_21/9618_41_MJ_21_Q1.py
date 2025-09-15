class node:
    def __init__(self, thedata, thenextNode):
        self.data = thedata
        self.nextNode = thenextNode

linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),
              node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer = 0
emptyList = 5

def outputNodes(theList, startPointer):
    thePointer = startPointer
    while thePointer != -1:
        print(theList[thePointer].data)
#        print(theList[thePointer].nextNode)
        thePointer = theList[thePointer].nextNode

outputNodes(linkedList, startPointer)

def addNode(theList, startPointer):
    global emptyList
    nData = input()
    if emptyList == -1:
        return False
    else:
        thePointer = startPointer
        prePointer = -1
        while thePointer != -1:
            prePointer = thePointer
            thePointer = theList[thePointer].nextNode
        nPointer = emptyList
        theList[nPointer].data = nData
        theList[nPointer].nextNode = -1
        theList[prePointer].nextNode = nPointer
        emptyList = theList[emptyList].nextNode
        return True

if addNode(linkedList, startPointer):
    print("Add node success")
else:
    print("Error: No empty space")

outputNodes(linkedList, startPointer)
