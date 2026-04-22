class Queue:
    def __init__(self, QA, HP, TP):
        self.QueueArray = QA # 1D ARRAY TO 100 OF INTEGER
        self.Headpointer = HP # INTEGER
        self.Tailpointer = TP # INTEGER

def Enqueue(AQueue, TheData):
    if AQueue.Headpointer == -1:
        AQueue.QueueArray[AQueue.Tailpointer] = TheData
        AQueue.Headpointer = 0
        AQueue.Tailpointer = AQueue.Tailpointer + 1
        return 1
    else:
        if AQueue.Tailpointer > 100:
            return -1
        else:
            AQueue.QueueArray[AQueue.Tailpointer] = TheData
            AQueue.Tailpointer = AQueue.Tailpointer + 1
            return 1

        
# MAIN
Tmp = []
for _ in range(100):
    Tmp.append(-1)
TheQueue = Queue(Tmp, -1, 0)


def ReturnAllData():
    global TheQueue
    result = ""
    current = TheQueue.Headpointer
    while current < TheQueue.Tailpointer:
        result = result + str(TheQueue.QueueArray[current]) + " "
        current = current + 1
    return result

def Dequeue():
    global TheQueue
    if TheQueue.Headpointer == TheQueue.Tailpointer or TheQueue.Headpointer == -1:
        return -1
    else:
        nextItem = TheQueue.QueueArray[TheQueue.Headpointer]
        TheQueue.Headpointer = TheQueue.Headpointer + 1
        return nextItem

for _ in range(10):
    TheInput = -1
    while int(TheInput) < 0:
        TheInput = input("Please input a integer: ")
    if Enqueue(TheQueue, TheInput):
        print("The item has been added")

print(ReturnAllData())

DQ = Dequeue()
if DQ == -1:
    print("Queue empty")
else:
    print(DQ)
DQ = Dequeue()
if DQ == -1:
    print("Queue empty")
else:
    print(DQ)

print(ReturnAllData())
