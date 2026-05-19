Queue = []
HeadPointer = -1
TailPointer = -1
NumberItems = 0

for i in range(20):
    Queue.append(-1)

def Enqueue(NewN):
    global Queue, NumberItems, HeadPointer, TailPointer
    if NumberItems >= 20:
        return False
    else:
        if HeadPointer == -1:
            HeadPointer = 0
        TailPointer += 1
        if TailPointer == 20:
            TailPointer = 0
        Queue[TailPointer] = NewN
        NumberItems += 1
        return True

def Dequeue():
    global Queue, NumberItems, HeadPointer, TailPointer
    if NumberItems == 0:
        return -1
    else:
        result = Queue[HeadPointer]
        HeadPointer += 1
        if HeadPointer == 20:
            HeadPointer = 0
        NumberItems -= 1
        if NumberItems == 0:
            HeadPointer = -1
            TailPointer = -1
        return result

for n in range(1,26):
    ans = str(n)
    if Enqueue(n) == True:
        ans += " Successful"
    else:
        ans += " Unsuccessful"
    print(ans)
print(Dequeue())
print(Dequeue())
