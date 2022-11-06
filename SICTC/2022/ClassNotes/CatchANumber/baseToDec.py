def anyBasetoDec(ui,base):
    letters="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    highestExp = len(ui)-1
    decimal = 0
    for n in ui:
        numba = letters.index(n)
        decimal+=(numba*base**highestExp)
        highestExp-=1
    print(decimal)

anyBasetoDec(input("Number >>> "),int(input("Base >>> ")))