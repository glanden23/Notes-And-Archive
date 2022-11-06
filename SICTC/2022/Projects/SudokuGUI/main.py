from tkinter import *
import loadFile

root = Tk()
root.resizable(0,0)

puzzleFromFile = []

def clearBoard():
    for i in puzzleFromFile:
        for j in i:
            j.delete(0,END)

def horizontalCheck(boardToCheck):
    for i in boardToCheck:
        nList = []
        for j in i:
            text = j.get()
            if text != "" and text != "!" and text in nList:
                j.delete(0,END)
                j.insert(0,"!")
            nList.append(text)

def verticalCheck(boardToCheck):
    i = 0
    while i != len(boardToCheck[0]):
        nList = []
        for j in boardToCheck:
            text = j[i].get()
            if text != "" and text != "!" and text in nList:
                j[i].delete(0,END)
                j[i].insert(0,"!")
            nList.append(text)
        i+=1

def blockCheck(boardToCheck):
    cRBlock=0
    cCBlock=0
    for _ in range(len(boardToCheck)):
        nList = []
        r=0+cRBlock
        for _ in range(3):
            c=0+cCBlock
            for _ in range(3):
                text = boardToCheck[r][c].get()
                if text != "" and text != "!" and text in nList:
                    boardToCheck[r][c].delete(0,END)
                    boardToCheck[r][c].insert(0,"!")
                nList.append(text)
                c+=1
            r+=1
        cRBlock+=3
        if cRBlock > 6:
            cCBlock+=3
            cRBlock=0

def loadFun():
    data = loadFile.file.loadData()
    for i in range(len(data)):
        for j in range(len(data[i])):
            puzzleFromFile[i][j].delete(0,END)
            puzzleFromFile[i][j].insert(0,data[i][j])

def drawGUI(background,btnbackground, btnbackground2, textColor,highlight):
    root.title("Sudoku GUI | Tkinter")
    root.geometry("312x278")
    root.config(background=background)

    inputFrame = Frame(root,width=312,height=272.5)
    inputFrame.config(background=background)
    inputFrame.pack()

    for i in range(9):
        puzzleFromFile.append([])
        for j in range(9):
            entry = Entry(inputFrame,fg=textColor,width=5,bd=0,bg=btnbackground,justify=CENTER)
            puzzleFromFile[i].append(entry)
            entry.grid(row=i+1,column=j,padx=1,pady=1)
    
    clear = Button(inputFrame,text="CLEAR",fg=textColor,width=43,height=3,bd=0,bg=btnbackground2,cursor="tcross",command=clearBoard)
    clear.grid(row=10,column=0,columnspan=9,padx=1,pady=1)
    
    loadFile = Button(inputFrame,text="NEW GAME",fg=textColor,width=43,height=3,bd=0,bg=btnbackground2,cursor="tcross",command=loadFun)
    loadFile.grid(row=13,column=0,columnspan=9,padx=1,pady=1)
    
    return entry

if __name__ == "__main__":
    fileInput = drawGUI("black","#4a4a4a","#2b2b2b","#ffffff", "#878787")

while True:
    horizontalCheck(puzzleFromFile)
    blockCheck(puzzleFromFile)
    verticalCheck(puzzleFromFile)
    root.update()