Queue = [-1 for _ in range(100)] #Integer
HeadP = -1
TailP = 0


def Enqueue(Data):
    global Queue, HeadP, TailP
    if HeadP == -1:
        HeadP = 0
    if TailP < 100:
        Queue[TailP] = Data
        TailP = TailP + 1
        return True
    else:
        return False

Success = True
for i in range(1,21):
    Flag = Enqueue(i)
    if not Flag:
        Success = False
if Success:
    print("Successful")
else:
    print("Unsuccessful")

def RecursiveOutput(Start):
    global Queue, HeadP, TailP
    if Start == HeadP:
        return Queue[Start]
    else:
        return RecursiveOutput(Start - 1) + Queue[Start]
    
print(str(RecursiveOutput(TailP - 1)))

