#python3 uses lowercase while python2 uses cap.
from tkinter import *

root = Tk()
root.title("Color Window | Tkinter")
root.wm_geometry("1280x720")
myLabel = Label(root,text="Input the color you want your window to be!",font=("Times New Roman", 40))
myLabel.pack()

#myButton = Button(root,text="Button!")
#myButton.pack()

myUserInput = Entry(root)
myUserInput.pack()

colorLabel = Label(root,text="",font=("Times New Roman", 10))
colorLabel.pack()

btn = Button(root,text="Quit",command=root.destroy)
btn.pack()

while True:
    root.update()
    #https://docs.python.org/3/tutorial/errors.html
    if myUserInput.get() == "":
        root.configure(background="white")
        colorLabel.config(text="white")
    else:
        try:
            root.configure(background=myUserInput.get())
            colorLabel.config(text=myUserInput.get().lower())
        except:
            root.configure(background="white")