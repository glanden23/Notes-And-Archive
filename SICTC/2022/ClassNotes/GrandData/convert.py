data = open("data.txt").readlines()
cleanData = []

for i in data:
    cleanData.append(i.replace("\n","").replace("]","").replace("[","").split(" "))

newData = []
for i in cleanData:
    tempList=[]
    while "" in i:
        i.remove("")
    for j in i:
        tempList.append(str(-int(j)))
    newData.append(tempList)

finalData = []
for i in newData:
    finalData.append(" ".join(i))
open("newData.txt", "w").write("[ "+"\n".join(finalData)+" ]")