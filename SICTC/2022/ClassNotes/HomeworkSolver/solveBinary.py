def returnIndexValue(index):
    if index == 0:
        return 1
    else:
        return 2**index

ui = list(input("Binary >>> "))
ui.reverse()
print(ui)
total = 0
for i in range(len(ui)):
    if ui[i] == "1":
        total+=returnIndexValue(i)
        print(total)