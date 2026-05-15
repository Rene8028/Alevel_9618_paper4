import random

Stack = [] # ARRAY[0,29] FOR INTEGER
TopOfStack = -1 # INTEGER
for i in range(30):
    Stack.append(-1)

def Push(NewNum):
    global Stack, TopOfStack
    if TopOfStack < 29:
        Stack[TopOfStack + 1] = NewNum
        TopOfStack = TopOfStack + 1
        return True
    else:
        return False

def Pop():
    global Stack, TopOfStack
    if TopOfStack == -1:
        return -999
    else:
        popnum = Stack[TopOfStack]
        TopOfStack = TopOfStack - 1
        return popnum

def FindValues():
    maxn = -1
    minn = 1001
    empty = False
    while empty == False:
        num = Pop()
        if num == -999:
            empty = True
        else:
            if num > maxn:
                maxn = num
            if num < minn:
                minn = num
    print("Largest number: " + str(maxn))
    print("Smallest number: " + str(minn))

IsFull = False
for j in range(40):
    if IsFull == False:
        if Push(random.randint(0,1000)) == False:
            print("Stack full")
            IsFull = True

FindValues()
