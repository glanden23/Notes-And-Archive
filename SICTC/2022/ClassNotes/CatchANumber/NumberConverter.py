def dec2bin(decimal):
    # 1 byte = 8 bits = 256 unique integers = hightest value is 255
    decimal = int(input("give me a positive whole number:"))


    #1st find the amount of bits
    #while the decimal is greater > 2**exp, keep finding the hightest bit value
    bitList=[]
    exp=0
    while decimal>=2**exp:      #to change base 2 into a different one change the 2 into another number
        bitList.insert(0,2**exp)  #insert instead of add to the end
        exp+=1
    #print(bitList)

    #2nd we iterated through the bitList to find how many of each bit is in our number
    for i in range(len(bitList)):
        if decimal>= bitList[i]:
            decimal-=bitList[i]
            bitList[i]="1"
        else:
            bitList[i]="0"
    #print(bitList)

    #3rd concatenated our 1's and 0's to output our string
    out="0b"
    for b in bitList:
        out+=b
    print(out)
    
def dec2hex(decimal):
    values="0123456789ABCDEF"
    # 1 byte = 8 bits = 256 unique integers = hightest value is 255
    decimal = int(input("give me a positive whole number:"))


    #1st find the amount of bits
    #while the decimal is greater > 2**exp, keep finding the hightest bit value
    digitList=[]
    exp=0
    while decimal>=16**exp:      #to change base 2 into a different one change the 2 into another number
        digitList.insert(0,2**exp)  #insert instead of add to the end
        exp+=1

    #2nd we iterated through the digitList to find how many of each bit is in our number
    for i in range(len(digitList)):
        temp=digitList[i]
        digitList[i]=decimal//digitList[i]
        decimal-=(digitList[i]*temp)
        digitList[i]=values[digitList[i]]

    #3rd convert out 10-15 to A-F
    #4th concate the digitList together
    out="0x"
    for b in digitList:
        out+=b
    print(out)
    
dec2hex(int(input()))