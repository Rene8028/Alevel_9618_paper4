EMPTYSTRING = ""
NullPointer = -1
MaxStackSize = 8

Stack = ["" for i in range(0, MaxStackSize)]
BaseOfStackPointer = -1
TopOfStackPointer = -1

def InitialiseStack():
    global Stack, BaseOfStackPointer, TopOfStackPointer
    BaseOfStackPointer = 0
    TopOfStackPointer = NullPointer
    
def Push(NewItem):
    global Stack, TopOfStackPointer
    if TopOfStackPointer < MaxStackSize - 1:
        TopOfStackPointer = TopOfStackPointer + 1
        Stack[TopOfStackPointer] = NewItem
    
def Pop():
    global Stack, TopOfStackPointer    
    Item = EMPTYSTRING
    if TopOfStackPointer > NullPointer:
        Item = Stack[TopOfStackPointer]
        TopOfStackPointer = TopOfStackPointer - 1
    return Item
    
def Cal_Postfix(postfix):
    postfixList = postfix.split()
    for i in postfixList:
        if i.isdigit():
            Push(i)
        else:
            op1 = int(Pop())
            op2 = int(Pop())
            if i == '+':
                Push(op1 + op2)
            if i == '-':
                Push(op2 - op1)
            if i == '*':
                Push(op1 * op2)
            if i == '/':
                Push(op1 / op2)
    return Pop()


InitialiseStack()
print(Cal_Postfix("3 4 + 7 2 - *"))
