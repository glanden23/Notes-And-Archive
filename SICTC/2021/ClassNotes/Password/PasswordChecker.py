# 1 num, 1 cap, 1 low, 1 special, 8 len
checkList = [False,False,False,False,False]
password = "@bc123OO"
specialCharacters="$&@!#$%^*()"

if len(password) >= 8:
    checkList[4] = True

for c in password:
    if ord(c) in range(48,58):
        checkList[0] = True
    elif ord(c) in range(65,91):
        checkList[1] = True
    elif ord(c) in range(97,123):
        checkList[2] = True
    elif c in specialCharacters:
        checkList[3] = True
    else:
        break
    
print(checkList)
if False in checkList:
    print("Your password is too weak...")
