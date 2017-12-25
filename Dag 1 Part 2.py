#Read file
f  = open('D:\Projecten\Python\AdventOfCode2017\Day 1\PuzzleInput.txt','r')

Values = f.read()
print("Input is: ",Values)

#Determine length
Length = len(Values)
print("Lenght is: ",Length)

#Offset for first part = 1
#Offset for second part = Half Lengt of the string
#Offset = 1
Offset = Length/2

#init total counter
TotalCount = 0
#init j
j = int(Offset-1)

#loop Input
for i in range(Length):
    j +=1

    if j >= Length:
        j = 0

    #if this number is equal to previous value
    if Values[i] == Values[j]:
        TotalCount+=int(Values[i])

print("Totalcount = ", TotalCount)
