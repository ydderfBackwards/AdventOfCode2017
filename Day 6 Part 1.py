import math

#Read file
f  = open('D:\Projecten\Python\AdventOfCode2017\Day 6\Input.txt','r')

############ Create list with all numbers
#Loop lines in file
for Line in f.readlines():
    print("Input is: ",Line)

    MyList = []

    #Loop to values in one line
    for number in Line.split():

        #Add
        MyList.append(int(number))

print(MyList)

NrOffValues = len(MyList)
Unique = 1
NrOffLoops = 0
OldList = []
######## while unique
while MyList not in OldList:

    OldList.append(list(MyList))

    #Find biggest value
    IndexBiggestValue = MyList.index(max(MyList))
    BiggestValue = max(MyList)

    #Reset to zerro
    MyList[IndexBiggestValue] = 0

    #Calculate number to add at each position
    ToShare = math.ceil(BiggestValue / NrOffValues)

    Index = IndexBiggestValue + 1
    if Index >= NrOffValues:
        Index = 0
    Shared = 0

    #While not all realocated
    while Shared < (BiggestValue - ToShare):

        MyList[Index] += ToShare
        Index +=1
        if Index >= NrOffValues:
            Index = 0
        Shared += ToShare

    #Realocate remainder
    Remainder = BiggestValue - Shared
    MyList[Index] += Remainder

    NrOffLoops +=1



    Unique +=1

    #print(IndexBiggestValue)
    #print(Index)
print(MyList)
print(NrOffLoops)
