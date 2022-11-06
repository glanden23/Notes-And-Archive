filename="./FileWriting/testdata.csv"
classes=["Advanced","Engineer","Collision","Automotive Service","Construction","CISCO","Software","Culinary","Diesel","Electrical","Graphic","Health","HVAC","Precision","Public","Radio","Vet","Welding"]
#advanced,engineer,collision,automotiveService,construction,cisco,software,culinary,diesel,electrical,graphic,health,hvac,precision,public,radio,vet,welding = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
listOfList=[]

for i in classes:
    listOfList.append([])

with open(filename,"r") as file:
    listOfLines = file.readlines()

for row in listOfLines:
    for i in range(len(classes)):
        if classes[i] in row:
            listOfList[i].append(row)

for i in range(len(classes)):
    with open(f"./Sorted/{classes[i]}.csv","w") as fileToWrite:
        for row in listOfList[i]:
            fileToWrite.write(row)