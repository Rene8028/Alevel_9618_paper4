Jobs = []  # Global 2D array of Integer 
NumberOfJobs = -1 # Global Integer

def Initialise():
    global Jobs
    global NumberOfJobs
    for i in range(0,100):
        Jobs.append([-1,-1])
    NumberOfJobs = 0

def AddJob(JN, JP):
    global Jobs
    global NumberOfJobs
    if NumberOfJobs == 100:
        print("Not added")
    else:
        Jobs[NumberOfJobs] = [JN, JP]
        NumberOfJobs = NumberOfJobs + 1
        print("Added")

def InsertionSort():
    global Jobs
    global NumberOfJobs

    for i in range(1, NumberOfJobs):
        select = Jobs[i]
        compare = i - 1
        
        while compare >= 0 and select[1] < Jobs[compare][1]:
            Jobs[compare + 1] = Jobs[compare]
            compare = compare - 1
        Jobs[compare + 1] = select

def PrintArray():
    global Jobs
    global NumberOfJobs

    for i in range(0, NumberOfJobs):
        print(Jobs[i][0], " priority ", Jobs[i][1])
            

# main
Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)

InsertionSort()
PrintArray()
