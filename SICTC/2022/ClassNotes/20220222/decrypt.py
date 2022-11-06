from random import randint

data = open("./words.txt").readlines()
wordList = []
for i in data:
    i = i.replace("\n","")
    wordList.append(i)
print(wordList)

while True:
    old = list("zkdw lv wkh dluvshhg ri dq xqodghq vzdoorz")
    new = ""
    for i in range(len(old)):
        n = randint(0, len(old)-1)
        new+=old[n]
        old.remove(old[n])
    for i in new.split(" "):
        if i in wordList:
            print(i)