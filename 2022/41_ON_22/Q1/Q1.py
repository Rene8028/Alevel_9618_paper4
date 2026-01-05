DataArray = [0 for I in range (100)]

def ReadFile():
    global DataArray
    try:
        TheF = open("IntegerData.txt", 'r')
        for n in range(0,100):
            DataArray[n] = int(TheF.readline()[:-1])
        TheF.close()
    except IOError:
        print("File not found")

def FindValues():
    global DataArray
    Target = -1
    while (Target < 1 or Target > 100):
        Target = int(input("Please input a whole number: "))
    Found = 0
    for num in DataArray:
        if num == Target:
            Found = Found + 1
    return Found

def BubbleSort():
    global DataArray
    NeedSwap = True
    while NeedSwap:
        NeedSwap = False
        for i in range(99): 
            if DataArray[i] > DataArray[i+1]:
                DataArray[i], DataArray[i+1] = DataArray[i+1], DataArray[i]
                NeedSwap = True
                

ReadFile()
Result = FindValues()
print("The number input appears in the array", Result, "times")

BubbleSort()
print(DataArray)

