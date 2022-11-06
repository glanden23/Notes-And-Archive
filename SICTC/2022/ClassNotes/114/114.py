amount = 0
max = 9999
while amount != max+1:
    pamount = []
    for i in range(10):
        pamount.append(str(amount))
        amount+=1
    print(" ".join(pamount))