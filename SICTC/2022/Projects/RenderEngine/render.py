import timg as t
from time import sleep
import os
import glob

def create(file, type, delay):
    length = len(glob.glob(f"{os.getcwd()}\Frames\{type}\*"))
    while True:
        for i in range(length):
            sleep(delay)
            nFile = file.replace("REPLACEVALUE", str(i))
            obj = t.Renderer()
            obj.load_image_from_file(f"./Frames/{type}/"+nFile+".png")
            obj.resize(int(os.get_terminal_size()[0]/1.2),int(os.get_terminal_size()[0]/1.7))
            obj.render(t.ASCIIMethod)

def cleanNames(names):
    for i in names:
        i = i.split("\\")[-1]
        files = glob.glob(f"{os.getcwd()}\Frames\{i}\*")
        for j in range(len(files)):
            try:
                os.rename(files[j], f"{os.getcwd()}\Frames\{i}\\frame_{j}.png")
            except:
                pass

print("\n"*500)
validInputs = glob.glob(f"{os.getcwd()}\Frames\*")
cleanNames(validInputs)
print("Valid Renders")
for i in validInputs:
    print(i.split("\\")[-1])
ui = input(">>> ")
delay = float(input("Enter the delay >>> "))
create("frame_REPLACEVALUE", ui.lower(), delay)