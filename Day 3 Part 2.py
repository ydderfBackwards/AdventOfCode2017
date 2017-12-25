
TestValue = 277678
Size = 18 #size of array
Middle = int(Size / 2) #centerpoint of array

#Create two dimensional Array
myArray = [[0 for j in range(Size)] for i in range(Size)]

#Create two dimensional Array, Doesn't work because it's a copy of lists!!!!
#myArray = [[0]*Size]*Size

#Create two dimensional array simple version
#myArray = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
#Set value for center point
myArray[Middle][Middle] = 1 #[y][x]

for r in myArray:
    print(r)

#init Values
CalculatedValue = 0
x_Test = Middle + 1
y_Test = Middle
Direction = "Right"

TempIndex = 0

while CalculatedValue <= TestValue:
    x_Right = x_Test + 1
    x_Left = x_Test - 1
    y_Up = y_Test - 1
    y_Down = y_Test + 1

    CalculatedValue = 0
    #print("CalculatedValue is ", CalculatedValue)

    #Check all cells next to current cell (not yet calculated cells contain zero, so we can add every value around the cell)
    CalculatedValue += myArray[y_Test][x_Right]
    CalculatedValue += myArray[y_Test][x_Left]
    CalculatedValue += myArray[y_Up][x_Right]
    CalculatedValue += myArray[y_Up][x_Left]
    CalculatedValue += myArray[y_Down][x_Right]
    CalculatedValue += myArray[y_Down][x_Left]
    CalculatedValue += myArray[y_Up][x_Test]
    CalculatedValue += myArray[y_Down][x_Test]

    print("CalculatedValue is ", CalculatedValue)

    #Update Array
    myArray[y_Test][x_Test] = CalculatedValue

    ############################## Determine Direction ######################
    if Direction == "Right" and myArray[y_Up][x_Test] == 0:
        #print("Go up")
        Direction = "Up"

    elif Direction == "Up" and myArray[y_Test][x_Left] == 0:
        #print("Go Left")
        Direction = "Left"

    elif Direction == "Left" and myArray[y_Down][x_Test] == 0:
        #print("Go Down")
        Direction = "Down"

    elif Direction == "Down" and myArray[y_Test][x_Right] == 0:
        #print("Go Right")
        Direction = "Right"

    #print("New direction is: ",Direction)

    ########################### Determine new coordinate #############
    if Direction == "Right":
        x_Test += 1

    elif Direction == "Up":
        y_Test -=1

    elif Direction == "Left":
        x_Test -= 1

    elif Direction == "Down":
        y_Test +=1

    #print("New test coordinate is: ", y_Test, " en ", x_Test)



#print final array
for r in myArray:
    print(r)

print("The last calculated value is: ", CalculatedValue)
