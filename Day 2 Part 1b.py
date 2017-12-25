#Read file
f  = open('D:\Prive\Projecten\Python\AdventOfCode2017\Day 2\PuzzleInput.txt','r')

Checksum = 0
MinValue = 0
MaxValue = 0

#Loop lines in file
for Line in f.readlines():
    print("Input is: ",Line)

    MyList = []

    #Loop to values in one line
    for number in Line.split():

        #Add
        MyList.append(int(number))

        #print("Mylist is ", MyList)


        result = float(number)/2

#        if result.is_integer():
#            print("waarde ", number, " is even")

    MaxValue = max(MyList)
    MinValue = min(MyList)


    Checksum += (MaxValue - MinValue)

print("Checksum is: ",Checksum)
