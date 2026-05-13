import random
MyArray = []
for i in range(20):
    unique = False
    while not unique:
        num = random.randint(0, 100)
        if num not in MyArray:
            unique = True
            MyArray.append(num)

def PrintArray(TheArray):
    out = ""
    for n in TheArray:
        out = out + str(n) + " "
    print(out)

def BubbleSort(TheArray):
    moved = True
    while moved:
        moved = False
        for index in range(len(TheArray) - 1):
            if TheArray[index] > TheArray[index + 1]:
                Tmp = TheArray[index + 1]
                TheArray[index + 1] = TheArray[index]
                TheArray[index] = Tmp
                moved = True

def RecursiveBinarySearch(TheArray, Low, Upp, Tofind):
    mid = int((Upp + Low) / 2)
    if Low > Upp or Upp < Low:
        return -1
    if Tofind == TheArray[mid]:
        return mid
    if Tofind > TheArray[mid]:
        return RecursiveBinarySearch(TheArray, mid + 1, Upp, Tofind)
    if Tofind < TheArray[mid]:
        return RecursiveBinarySearch(TheArray, Low, mid - 1, Tofind)

PrintArray(MyArray)
BubbleSort(MyArray)
print("Sorted")
PrintArray(MyArray)

Target = input("Enter the number to find: ")
result = RecursiveBinarySearch(MyArray, 0, len(MyArray) - 1, int(Target))
if result == -1:
    print("Not found")
else:
    print("Found at position ", result)

