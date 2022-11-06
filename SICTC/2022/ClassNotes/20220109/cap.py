print("Type \"quit\" to exit the program.")

ui = ""
while ui!="quit":
    ui = input("Give word >>> ")
    case=0
    formatted = ""
    for i in ui:
        if case == 0:
            case+=1
            formatted+=i.upper()
        else:
            case-=1
            formatted+=i.lower()
    print(formatted)