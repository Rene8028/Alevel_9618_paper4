class Record:
    def __init__(self, my_key, my_data):
        self.Key = my_key # INTEGER
        self.Data = my_data # STRING

HashTable = []
def InitialiseHashTable():
    global HashTable
    for i in range(100):
        row = []
        for j in range(10):
            row.append(Record(-1, ""))
        HashTable.append(row)

def Hash(num):
    return num % 100

def InsertData(new_record):
    global HashTable
    hash_vaule = Hash(new_record.Key)
    setted = False
    for ix in range(10):
        if HashTable[hash_vaule][ix].Key == -1:
            if not setted:
                HashTable[hash_vaule][ix] = new_record
                setted = True

def ReadData():
    myfile = open("HashTableData.txt")
    lines = myfile.readlines()
    for l in lines:
        the_line = l.split(",")
        InsertData(Record(int(the_line[0]), the_line[1]))
    myfile.close()

def GetRecord(the_key):
    global HashTable
    hash_key = Hash(the_key)
    result = ""
    for jx in range(10):
        if HashTable[hash_key][jx].Key == the_key:
            result = HashTable[hash_key][jx].Data
    if result == "":
        return "NotFound"
    else:
        return result

InitialiseHashTable()
ReadData()
for kx in range(5):
    inkey = input("Please enter a key field: ")
    print(GetRecord(int(inkey)))
