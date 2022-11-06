from tkinter import *

root = Tk()
root.resizable(0,0)

inputs = []
output=StringVar()

def clearBTN():
    for i in inputs:
        i.delete(0,END)

def base10ToBase(n, b):
    try:
        if b == 16:
            return hex(n)
        elif b == 2:
            return bin(n)
        elif b == 10:
            return n
        elif b == 8:
            return oct(n)
        else:
            return "Must be 2, 8, 10 or 16..."
    except:
        return "ERROR"

def anyBasetoDec(n,base):
    letters="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    highestExp = len(n)-1
    decimal = 0
    for n in n:
        numba = letters.index(n)
        decimal+=(numba*base**highestExp)
        highestExp-=1
    return decimal

def createGUI(background, btnbackground, btnbackground2, textColor):
    root.title("Number Converter | Tkinter")
    root.geometry("362x224")
    root.config(background=background)

    inputFrame = Frame(root,width=312,height=272.5)
    inputFrame.config(background=background)
    inputFrame.pack()
    
    Label(inputFrame,fg=textColor,bg=background,text="Base being converted from:").grid(row=0,column=0,padx=1,pady=1)
    
    entryBase = Entry(inputFrame,fg=textColor,width=43,bd=0,bg=btnbackground,justify=CENTER)
    inputs.append(entryBase)
    entryBase.grid(row=1,column=0,padx=1,pady=1)
    
    Label(inputFrame,fg=textColor,bg=background,text="Number to convert:").grid(row=2,column=0,padx=1,pady=1)
    
    entry = Entry(inputFrame,fg=textColor,width=43,bd=0,bg=btnbackground,justify=CENTER)
    inputs.append(entry)
    entry.grid(row=3,column=0,padx=1,pady=1)
    
    Label(inputFrame,fg=textColor,bg=background,text="Base being converted to:").grid(row=4,column=0,padx=1,pady=1)
    
    entryBase = Entry(inputFrame,fg=textColor,width=43,bd=0,bg=btnbackground,justify=CENTER)
    inputs.append(entryBase)
    entryBase.grid(row=5,column=0,padx=1,pady=1)
    
    Label(inputFrame,fg=textColor,bg=background,wraplength=312,justify=CENTER,textvariable=output).grid(row=6,column=0,padx=1,pady=1)

    clear = Button(inputFrame,text="CLEAR",fg=textColor,width=12,height=2,bd=0,bg=btnbackground2,cursor="tcross",command=clearBTN)
    clear.grid(row=7,column=0,padx=1,pady=25)

if __name__ == "__main__":
    createGUI("gray","#4a4a4a","#2b2b2b","#ffffff")
    
while True:
    root.update()
    ob = inputs[0].get()
    n = inputs[1].get()
    b = inputs[2].get()
    if ob != "" and n != "" and b != "":
        n = anyBasetoDec(n,int(ob))
        output.set(base10ToBase(n,int(b)))
    else:
        output.set("")