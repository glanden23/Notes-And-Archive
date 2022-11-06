#opens the file and grabs each line from the file
data=open(input("File Name? >>> ")+".txt").readlines()
puzzleFromFile = []
#this takes the lines and removes any "\n" from it.
for i in data:
    i = i.replace("\n","")
    puzzleFromFile.append(i)
#cleans up data variable as we don't need it anymore
del data

#these two lists are used to print out any failures that occur in the checks
failedHor = []
failedVer = []
failedBlock = []

def horizontalCheck(boardToCheck):
    #loops through each row
    for i in boardToCheck:
        #nList is where numbers are checked for duplicates
        nList = []
        #This is looping through every number in the row
        for j in i:
            #if the number is found in nList then we know it is a duplicate
            if j in nList:
                #adds any failures to a list to be printed out later
                #first index is the row that it occured at and second is what number caused the failure
                failedHor.append([boardToCheck.index(i)+1, j])
            #adds the number to nList for checking later
            nList.append(j)
    #if the length of failedHor is bigger than 0 then we know a failure occured.
    #this makes sure it gets printed in the end out to the user
    if len(failedHor) > 0:
        return False
    return True

def blockCheck(boardToCheck):
    cRBlock=0
    cCBlock=0
    for _ in range(len(boardToCheck)):
        nList = []
        r=0+cRBlock
        for _ in range(3):
            c=0+cCBlock
            for _ in range(3):
                text = boardToCheck[r][c]
                if text in nList:
                    failedBlock.append([_,boardToCheck[r][c]])
                nList.append(text)
                c+=1
            r+=1
        cRBlock+=3
        if cRBlock > 6:
            cCBlock+=3
            cRBlock=0
    if len(failedBlock) > 0:
        return False
    return True

def verticalCheck(boardToCheck):
    #i = the current column being checked.
    i = 0
    #keeps going until the number of i(iterations) is equal to the length of the board
    #which basically just keeps looping until no more columns exist.
    while i != len(boardToCheck[0]):
        #nList is where the numbers are put as they are checked to make sure no duplicates exist.
        nList = []
        #Loops through each line of the file where the iteration is the index.
        for j in boardToCheck:
            if j[i] in nList:
                #adds any failures to a list to be printed out later.
                #first index is the column that it occured at and second is what number caused the failure
                failedVer.append([i+1, j[i]])
            #appends number to nList for checking next number
            nList.append(j[i])
        #moves iteration up to check next column
        i+=1
    #if the length of failedVer is bigger than 0 then we know a failure occured.
    #this makes sure it gets printed in the end out to the user
    if len(failedVer) > 0:
        return False
    return True

#Calls horizontal function to check if file is correct.
if horizontalCheck(puzzleFromFile):
    print("Passed horizontal check.")
else:
    #This loops through the failures and prints each one out.
    #Stops the program from just printing out the first error it runs into.
    for i in failedHor:
        print(f"Horizontally failed at row {i[0]} at number {i[1]}.")
        
#Same as above but vertical.
if verticalCheck(puzzleFromFile):
    print("Passed vertical check.")
else:
    for i in failedVer:
        print(f"Vertically failed at column {i[0]} at number {i[1]}.")

#Same as above but block.
if blockCheck(puzzleFromFile):
    print("Passed block check.")
else:
    for i in failedBlock:
        print(f"Failed in block {9-int(i[0])} at number {i[1]}.")