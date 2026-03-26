def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    if NumberElements == 0:
        return 0
    ans = RecursiveCount(ArrayCopy[1:], NumberElements - 1, DataToFind)
    if ArrayCopy[0] == DataToFind:
        return ans + 1
    else:
        return ans

def SplitData(Rawstr):
    tmpline = ""
    linecount = 0
    ansstr = []
    for word in Rawstr:
        if word != ';':
            tmpline = tmpline + word
        else:
            ansstr.append(tmpline)
            linecount = linecount + 1
            tmpline = ""
    return ansstr
            
    

#MAIN
Thearray = [0,5,1,2,5,9,9,6,5,0]
print(RecursiveCount(Thearray, 10, 0))

Code = "x=0;y=1;x=x+y;y++;"

for i in SplitData(Code):
    print(i)
