#python3 uses lowercase while python2 uses cap.
from tkinter import *
BACKGROUND = "#414141"
FOREGROUND = "white"

masterUser = "admin"
masterPass = "admin"

def pressedButton():
    if userInput.get() == masterUser and passInput.get() == masterPass:
        print("Logged in.")

root = Tk()
root.title("Login | Tkinter")
root.config(background=BACKGROUND)
root.wm_geometry("1280x720")

loginWindow = Frame(root)
loginWindow.grid(row=0,column=0,sticky='news')
loginWindow.config(background=BACKGROUND)

authWindow = Frame(root)
authWindow.grid(row=0,column=0,sticky='news')
authWindow.config(background=BACKGROUND)

titleLBL = Label(loginWindow,text="Please enter your login details!",font=("Times New Roman", 20))
titleLBL.config(background=BACKGROUND,foreground=FOREGROUND)
titleLBL.pack(pady=25,padx=25)

passLBL = Label(loginWindow,text="Username:",font=("Times New Roman", 10))
passLBL.config(background=BACKGROUND,foreground=FOREGROUND)
passLBL.pack(pady=5,padx=5)

userInput = Entry(loginWindow)
userInput.config(background=BACKGROUND,foreground=FOREGROUND)
userInput.pack()

passLBL = Label(loginWindow,text="Password:",font=("Times New Roman", 10))
passLBL.config(background=BACKGROUND,foreground=FOREGROUND)
passLBL.pack(pady=5,padx=5)

#https://stackoverflow.com/questions/2416486/how-to-create-a-password-entry-field-using-tkinter
passInput = Entry(loginWindow,show="*")
passInput.config(background=BACKGROUND,foreground=FOREGROUND)
passInput.pack()

loginBTN = Button(loginWindow, text="Login",command=pressedButton)
loginBTN.pack(pady=125,padx=125)

helloLBL = Label(authWindow,text="Oh hello there")
helloLBL.config(background=BACKGROUND,foreground=FOREGROUND)
helloLBL.pack()

root.mainloop()