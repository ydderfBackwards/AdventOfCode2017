#For example:
  #- 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
  #- 1111 produces 4 because each digit (all 1) matches the next.
  #- 1234 produces 0 because no digit matches the next.
  #- 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

#Read file
f  = open('D:\Prive\Projecten\Python\AdventOfCode2017\Day 1\PuzzleInput.txt','r')
Values = f.read()
print("Input is: ",Values)

#Determine length (not used)
Length = len(Values)
print("Lenght is: ",Length)

#init total counter
TotalCount = 0
PreviousValue = "NotANumber"

#loop Input
for CheckValue in Values:
    #if this number is equal to previous value
    if CheckValue == PreviousValue:
        TotalCount+=int(CheckValue)

    #Remember value for next loop
    PreviousValue = CheckValue

if PreviousValue == Values[0]:
    TotalCount+=int(Values[0])

print("Totalcount = ", TotalCount)
