#Read file
f  = open('D:\Prive\Projecten\Python\AdventOfCode2017\Day 4\Input.txt','r')

NrOffValid = 0

#Loop lines in file
for PassPhrase in f.readlines():

    CheckPassPhrase = ""
    Valid = 1

    #Loop to values in one line
    for Word in PassPhrase.split():

        if Word in CheckPassPhrase:
            print("Value in line is: ", Word, "PassPhrase is ", CheckPassPhrase)

            print("Not valid")
            Valid = 0

        CheckPassPhrase += Word

        CheckPassPhrase += " "

    if Valid == 1:
        NrOffValid +=1

print("Nr off valid passphrases is: ",NrOffValid)
