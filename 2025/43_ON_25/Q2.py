Queue = ["" for _ in range(100)] # 1D ARRAY OF STRING
QueueHead = -1
QueueTail = -1
NumberItems = 0

def Enqueue(NewS):
    global Queue, QueueHead, QueueTail, NumberItems
    if NumberItems == 100:
        return False
    else:
        if QueueHead == -1:
            QueueHead = 0
        Queue[QueueTail + 1] = NewS
        NumberItems = NumberItems + 1
        QueueTail = QueueTail + 1
        if QueueTail == 100:
            QueueTail = 0
        return True

def Dequeue():
    global Queue, QueueHead, QueueTail, NumberItems
    if NumberItems == 0:
        return "False"
    else:
        nextE = Queue[QueueHead]
        QueueHead = QueueHead + 1
        if QueueHead == 100:
            QueueHead = 0
        NumberItems = NumberItems - 1
        return nextE

def ReadData():
    TheFile = open("BinaryData.txt")
    for i in TheFile:
        Enqueue(i.strip())
    TheFile.close()

NewString = ""

def Compress():
    global Queue, QueueHead, QueueTail, NumberItems, NewString
    current = "-1"
    previous = "-1"
    times = 0
    for n in range(NumberItems):
        previous = current
        current = Dequeue()
        if current == previous or previous == "-1":
            times = times + 1
        else:
            NewString = NewString + previous + str(times)
            times = 1
    NewString = NewString + previous + str(times)
        


# MAIN
ReadData()
Compress()
print(NewString)
