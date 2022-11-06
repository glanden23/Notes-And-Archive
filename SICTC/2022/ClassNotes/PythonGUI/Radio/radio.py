from tkinter import *

# Global Variables
root = Tk() #creates screen
var = IntVar() #creates int variable for radio value

def radioBTNUpdate():
    output = str(var.get())
    gItems[0].config(text=output)

def createGUI():
    #sets screen name and size
    root.title("Radio | Tkinter")
    root.geometry("300x200")
    
    #radio buttons
    r1 = Radiobutton(root,text="option #1", value=10, variable=var, command=radioBTNUpdate)
    r2 = Radiobutton(root,text="option #2", value=20, variable=var, command=radioBTNUpdate)
    valueLBL = Label(root)
    
    #packs GUI items
    r1.pack();r2.pack();valueLBL.pack()
    return [valueLBL]

#Removes worry of calling a function before it is loaded.
if __name__ == "__main__":
    #Creates the GUI
    gItems = createGUI()

#Keeps GUI open
root.mainloop()