"""
DEPENDENCIES
"""

from colorama import Fore, Style

"""
FUNCTIONS
"""

def loadFile():
    try:
        rawData = open(input("Enter csv file name you want to load! (No need to type .csv) >>> ")+".csv").readlines()
    except:
        print("Invalid file! Please try again...")
        return loadFile()
    newData = []
    for i in rawData:
        data = i.replace("\n","").split(",")
        newData.append(data)
    return newData

def getWords():
    lineData = open("words.txt").readlines()
    cleanData = []
    for i in lineData:
        cleanData.append(i.replace("\n","").upper())
    return cleanData

def createCorrectList():
    correctList = []
    for i in range(len(data)):
        tempList = []
        for j in range(len(data)):
            tempList.append("_")
        correctList.append(tempList)
    return correctList

def dupInFound(found,word):
    wletters = {}
    fletters = {}
    for l in word:
        try:
            wletters[l]+=1
        except:
            wletters[l]=1
            fletters[l]=0
    for f in found:
        fletters[f[0]]+=1
        if wletters[f[0]] < fletters[f[0]]:
            for i in range(len(found)):
                if found[i][0] == f[0]:
                    del found[i]
                    return found
    return found

def verticalCheck(word):
    found = []
    for i in range(len(data[0])):
        for j in range(len(data)):
            if data[j][i] in word:
                found.append([data[j][i], j, i])
                found = dupInFound(found,word)
                if len(found) == len(word):
                    for n in range(len(found)):
                        correctList[found[n][1]][found[n][2]] = found[n][0]
                    return True
            else:
                found=[]

def horizontalCheck(word):
    found = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] in word:
                found.append([data[i][j], i, j])
                found = dupInFound(found,word)
                if len(found) == len(word):
                    for n in range(len(found)):
                        correctList[found[n][1]][found[n][2]] = found[n][0]
                    return True
            else:
                found=[]

def output():
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == correctList[i][j]:
                print(Fore.GREEN+ data[i][j]+ Style.RESET_ALL, end=" ")
            else:
                print(data[i][j], end=" ")
        print()
"""
MAIN
"""

if __name__ == "__main__":
    data = loadFile()
    words = getWords()
    correctList = createCorrectList()
    for i in range(len(words)):
        verticalCheck(words[i])
        horizontalCheck(words[i])
    output()