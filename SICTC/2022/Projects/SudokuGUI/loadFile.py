from random import randint

class file:
    #https://qqwing.com/generate.html
    def loadData():
        data = open("games.txt").readlines()
        data = data[randint(0,len(data)-1)]
        data = data.split(",")
        rawPuzzle = list(data[0])
        puzzleData = []
        data = []
        for i in range(len(rawPuzzle)):
            data.append(rawPuzzle[i].replace(".",""))
            if (i+1) % 9 == 0:
                puzzleData.append(data)
                data = []
        return puzzleData