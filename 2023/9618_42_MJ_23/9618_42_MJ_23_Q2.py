class SaleData:
    def __init__(self, TheSaleID, TheQuantity):
        self.SaleID = TheSaleID # string
        self.Quantity = TheQuantity # integer

CircularQueue = []
NumberOfItems = 0
Head = 0
Tail = 0

def Enqueue(NewRecord):
    global CircularQueue, NumberOfItems, Head, Tail
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = NewRecord
        if Tail == 4:
            Tail = 0
        else:
            Tail = Tail + 1
        NumberOfItems = NumberOfItems + 1
        return 1
    
def Dequeue():
    global CircularQueue, NumberOfItems, Head, Tail
    if NumberOfItems == 0:
        return SaleData("", -1)
    else:
        DelRecord = CircularQueue[Head]
        if Head == 4:
            Head = 0
        else:
            Head = Head + 1
        NumberOfItems = NumberOfItems - 1
        return DelRecord

def EnterRecord():
    NewRSaleID = input("Enter ID")
    NewRQuantity = input("Enter Quantity")
    if Enqueue(SaleData(NewRSaleID, NewRQuantity)) == 1:
        print("Stored")
    else:
        print("Full")

# main
for i in range(5):
    CircularQueue.append(SaleData("", -1))

for j in range(6):
    EnterRecord()

DeRecord = Dequeue()
if DeRecord.Quantity == -1:
    print("ERROR: The queue is empty")
else:
    print(DeRecord.SaleID, "  ", DeRecord.Quantity)

EnterRecord()
for k in range(5):
    print(CircularQueue[k].SaleID, "  ", CircularQueue[k].Quantity)

