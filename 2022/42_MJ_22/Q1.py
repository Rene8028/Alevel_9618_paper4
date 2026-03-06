StackPointer = 0
StackData = ["" for i in range(10)]

def PrintStack():
    print(StackPointer)
    for Item in StackData:
        print(Item)

def Push(NData):
    global StackData, StackPointer
    if StackPointer != 10:
        StackData[StackPointer] = NData
        StackPointer = StackPointer + 1
        return True
    else:
        return False

def Pop():
    global StackData, StackPointer
    if StackPointer != 0:
        PData = StackData[StackPointer - 1]
        StackData[StackPointer - 1] = ""
        StackPointer = StackPointer - 1
        return PData
    else:
        return -1

#main
    
for j in range(11):
    TheNum = input()
    if Push(TheNum):
        print("Success")
    else:
        print("ERROR: Stack is full")
PrintStack()

Pop()
Pop()
PrintStack()
