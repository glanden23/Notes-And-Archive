decimal = int(input("Give me a pos whole number: "))

def dec2bin(decimal):
    bitList=[]
    expo = 0
    while decimal>=2**expo:
        bitList.insert(0,2**expo)
        expo+=1

    for i in range(len(bitList)):
        if decimal >= bitList[i]:
            decimal-=bitList[i]
            bitList[i]="1"
        else:
            bitList[i]="0"

    out="0b"
    for b in bitList:
        out+=b
    print(out)

def dec2hex(decimal):
    bitList=[]
    expo = 0
    while decimal>=16**expo:
        bitList.insert(0,16**expo)
        expo+=1

    for i in range(len(bitList)):
        if decimal >= bitList[i]:
            numberOfTimes = decimal//bitList[i]
            decimal-=numberOfTimes*bitList[i]
            bitList[i]= numberOfTimes
        else:
            bitList[i]="0"
    print(bitList)
    
dec2hex(decimal)