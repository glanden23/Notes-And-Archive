UI = input("Height? >>> ")
while UI != "stop":
    while UI.isdigit() == False:
        UI = input("Height? >>> ")
        if UI == "stop":
            print("Goodbye.")
            exit()
    UI = int(UI)
    if UI > 0:
        spaces = UI
        for i in range(UI):
            spaces-=1
            blocks = "#"*(i+1)
            print(" "*spaces+blocks + " " + blocks)
            i-=1
    else:
        print("Too small of a number.")
    UI = input("Height? >>> ")
print("Goodbye.")