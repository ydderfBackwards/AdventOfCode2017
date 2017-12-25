#Read file
f  = open('D:\Projecten\Python\AdventOfCode2017\Day 2\PuzzleInput.txt','r')

Checksum = 0

#Loop lines in file
for Line in f.readlines():
    print("Input is: ",Line)

    maxValue = 0
    minValue = 999999999999

    #Loop to values in one line
    for number in Line.split():
        print("Value in line is: ", number)

        if int(number) > maxValue:
            maxValue = int(number)

        if int(number) < minValue:
            minValue = int(number)

    print("Max is ",maxValue, " Min is ", minValue)
    Checksum += (maxValue - minValue)

print("Checksum is: ",Checksum)

#for i in Values:
#    print("i is ",i)
