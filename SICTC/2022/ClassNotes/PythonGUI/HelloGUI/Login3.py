#python3 uses tkinter / python2 uses Tkinter
from tkinter import *
masterUsername = "admin"
masterPassword = "admin"
BACKGROUND = "#414141"
FOREGROUND = "white"

def logOut():
    loginFrame.tkraise()

def pressMyButton():
    print("You pressed the button")
    if usernameEntry.get() == masterUsername and passwordEntry.get() == masterPassword:
        print("You're logged in")
        authFrame.tkraise()

root = Tk()
root.title("Login | Tkinter")
root.config(background=BACKGROUND)
root.wm_geometry("1280x720")

authFrame = Frame(root)
authFrame.config(background=BACKGROUND)
authFrame.grid(row=0,column=0,sticky='news')

loginFrame = Frame(root)
loginFrame.config(background=BACKGROUND)
loginFrame.grid(row=0,column=0,sticky='news')

usernameLBL = Label(loginFrame,text="Username: ")
usernameLBL.config(background=BACKGROUND,foreground=FOREGROUND)
usernameLBL.pack(pady=5,padx=5)

usernameEntry = Entry(loginFrame,bd=3)
usernameEntry.config(background=BACKGROUND,foreground=FOREGROUND)
usernameEntry.pack(pady=5,padx=5)

passwordLBL = Label(loginFrame,text="Password: ")
passwordLBL.config(background=BACKGROUND,foreground=FOREGROUND)
passwordLBL.pack(pady=5,padx=5)

passwordEntry = Entry(loginFrame,bd=3,show="*")
passwordEntry.config(background=BACKGROUND,foreground=FOREGROUND)
passwordEntry.pack(pady=5,padx=5)

loginBTN = Button(loginFrame,text="Log In",command=pressMyButton)
loginBTN.config(background=BACKGROUND,foreground=FOREGROUND)
loginBTN.pack(pady=20,padx=175)

helloLBL = Label(authFrame,text="Oh hello there")
helloLBL.config(background=BACKGROUND,foreground=FOREGROUND)
helloLBL.pack(padx=5)

LogoutBTN = Button(authFrame,text="Log Out",command=logOut)
LogoutBTN.config(background=BACKGROUND,foreground=FOREGROUND)
LogoutBTN.pack(pady=20,padx=175)

root.mainloop()