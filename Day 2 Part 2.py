#Read file
f  = open('D:\Projecten\Python\AdventOfCode2017\Day 2\PuzzleInput.txt','r')

Checksum = 0

#Loop lines in file
for Line in f.readlines():
    print("Input is: ",Line)

    MyList = []

    #Loop to values in one line
    for number in Line.split():
        #Add number to list
        MyList.append(int(number))

    #for all numbers in my list (main loop)
    for CheckNumber1 in MyList:
        #for all number in my list (compare with main loop)
        for CheckNumber2 in MyList:
            if CheckNumber1 > CheckNumber2: #Only check if value from main loop is the biggest one. Else values get checked twice.
                if (CheckNumber1 % CheckNumber2) == 0: # % instruction gives remainder of divide. This should be zero
                    Checksum += CheckNumber1/CheckNumber2

print("Checksum is: ",Checksum)
