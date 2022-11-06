from tkinter import *
expression = ""

def BTNClicked(btn):
    global expression
    expression += btn
    inputField.insert(len(inputField.get()),btn)

def clearBTN():
    global expression
    expression=""
    output.set(expression)

def equalBTN():
    global expression
    if len(expression) < 9:
        if checkExpress():
            #Detected two arithmetics next to each other
            result = "EXPRESSION EVAL ERROR"
        else:
            #Try and except to grab majority of errors rather than checking them all
            # and return smoothly to user
            try:
                result=str(eval(expression))
            except:
                result="EXPRESSION EVAL ERROR"
    else:
        #Expression is bigger than 8
        result="OVERFLOW ERROR"
    #Sets the visible user input to the result variable
    output.set(result)

def checkExpress():
    #https://www.geeksforgeeks.org/python-arithmetic-operators/
    arithmetics = "*/%+-"
    for i in range(len(expression)):    
        #Loops through expression.
        #Checks if expression behind currently checked is in arithmetics as well
        #Returns True when two arithmetics is detected next to each other
        if expression[i] in arithmetics and expression[i-1] in arithmetics:
            return True
    #Returns False when no issue was detected
    return False

root = Tk()
root.resizable(0,0)
output = StringVar()

def drawGUI(background,btnbackground, btnbackground2, textColor,highlight):
    root.title("Calculator | Tkinter")
    root.geometry("312x324")
    root.config(background=background)
    
    inputFrame = Frame(root,width=312,height=32,bd=0,highlightbackground=highlight,highlightcolor=highlight,highlightthickness=1)
    inputFrame.pack(side=TOP)
    inputFrame.config(background=background)

    inputField = Entry(inputFrame, bd=0,width=312, justify=RIGHT, textvariable=output)
    inputField.grid(column=0,row=0)
    inputField.pack(ipady=10)
    inputField.config(background=background,foreground=textColor)

    buttonFrame = Frame(root,width=312,height=272.5)
    buttonFrame.config(background=background)
    buttonFrame.pack()

    clear = Button(buttonFrame,text="C",fg=textColor,width=32,height=3,bd=0,bg=btnbackground2,cursor="tcross",command=lambda:clearBTN())
    clear.grid(row=0,column=0,columnspan=3,padx=1,pady=1)
    divide = Button(buttonFrame,text="/",fg=textColor,width=10,height=3,bd=0,bg=btnbackground2,cursor="tcross",command=lambda:BTNClicked("/"))
    divide.grid(row=0,column=3,padx=1,pady=1)

    seven = Button(buttonFrame,text="7",fg=textColor,width=10,height=3,bd=0,bg=btnbackground,cursor="tcross",command=lambda:BTNClicked("7")).grid(row=1,column=0,padx=1,pady=1)
    eight = Button(buttonFrame,text="8",fg=textColor,width=10,height=3,bd=0,bg=btnbackground,cursor="tcross",command=lambda:BTNClicked("8")).grid(row=1,column=1,padx=1,pady=1)
    nine = Button(buttonFrame,text="9",fg=textColor,width=10,height=3,bd=0,bg=btnbackground,cursor="tcross",command=lambda:BTNClicked("9")).grid(row=1,column=2,padx=1,pady=1)
    multiply = Button(buttonFrame,text="*",fg=textColor,width=10,height=3,bd=0,bg=btnbackground2,cursor="tcross",command=lambda:BTNClicked("*")).grid(row=1,column=3,padx=1,pady=1)

    four = Button(buttonFrame,text="4",fg=textColor,width=10,height=3,bd=0,bg=btnbackground,cursor="tcross",command=lambda:BTNClicked("4")).grid(row=2,column=0,padx=1,pady=1)
    five = Button(buttonFrame,text="5",fg=textColor,width=10,height=3,bd=0,bg=btnbackground,cursor="tcross",command=lambda:BTNClicked("5")).grid(row=2,column=1,padx=1,pady=1)
    six = Button(buttonFrame,text="6",fg=textColor,width=10,height=3,bd=0,bg=btnbackground,cursor="tcross",command=lambda:BTNClicked("6")).grid(row=2,column=2,padx=1,pady=1)
    subtract = Button(buttonFrame,text="-",fg=textColor,width=10,height=3,bd=0,bg=btnbackground2,cursor="tcross",command=lambda:BTNClicked("-")).grid(row=2,column=3,padx=1,pady=1)

    one = Button(buttonFrame,text="1",fg=textColor,width=10,height=3,bd=0,bg=btnbackground,cursor="tcross",command=lambda:BTNClicked("1")).grid(row=3,column=0,padx=1,pady=1)
    two = Button(buttonFrame,text="2",fg=textColor,width=10,height=3,bd=0,bg=btnbackground,cursor="tcross",command=lambda:BTNClicked("2")).grid(row=3,column=1,padx=1,pady=1)
    three = Button(buttonFrame,text="3",fg=textColor,width=10,height=3,bd=0,bg=btnbackground,cursor="tcross",command=lambda:BTNClicked("3")).grid(row=3,column=2,padx=1,pady=1)
    add = Button(buttonFrame,text="+",fg=textColor,width=10,height=3,bd=0,bg=btnbackground2,cursor="tcross",command=lambda:BTNClicked("+")).grid(row=3,column=3,padx=1,pady=1)

    zero = Button(buttonFrame,text="0",fg=textColor,width=21,height=3,bd=0,bg=btnbackground,cursor="tcross",command=lambda:BTNClicked("0")).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
    decimal = Button(buttonFrame,text=".",fg=textColor,width=10,height=3,bd=0,bg=btnbackground,cursor="tcross",command=lambda:BTNClicked(".")).grid(row=4,column=2,padx=1,pady=1)
    equal = Button(buttonFrame,text="=",fg=textColor,width=10,height=3,bd=0,bg=btnbackground2,cursor="tcross",command=lambda:equalBTN()).grid(row=4,column=3,padx=1,pady=1)
    
    return inputField

if __name__ == "__main__":
    inputField = drawGUI("black","#4a4a4a","#2b2b2b","#ffffff", "#878787")

while True:
    if (inputField.get() != expression):
        expression = inputField.get()
    root.update()