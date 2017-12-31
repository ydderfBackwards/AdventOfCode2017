#Read file
f  = open('D:\Prive\Projecten\Python\AdventOfCode2017\Day 5\Input.txt','r')


MyList = []

#Loop lines in file
for Line in f.readlines():
    #Add number to list
    MyList.append(int(Line))


Index = 0
StepCounter = 0

#while not end of list
while Index < len(MyList):
    #Read number of steps
    Steps = MyList[Index]
    #Increment one
    MyList[Index] += 1

    Index += Steps
    StepCounter +=1

    #print("Steps is ",Steps,"Index is", Index)

print("It takes ",StepCounter, "steps")
