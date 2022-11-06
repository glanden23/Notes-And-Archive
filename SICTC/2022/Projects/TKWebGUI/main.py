from datetime import datetime
import tkinter as tk
import os

root = tk.Tk()
root.resizable(0,0)
root.title("Networking GUI | Tkinter")
root.geometry("512x478")
root.config(background="gray")

output = tk.StringVar()

def runCommand(command):
    global output
    output.set(os.popen(f"{command} {ipAddress.get()}").read())

def save():
    open(datetime.ctime(datetime.now()).replace(":",".")+".txt", "w").write(output.get())

buttonFrame = tk.Frame(root,width=312,height=272.5)
buttonFrame.config(background="gray")
buttonFrame.pack()

tk.Button(buttonFrame,text="Send Ping",justify=tk.CENTER,command=lambda:runCommand("ping")).grid(row=0,column=0)
tk.Button(buttonFrame,text="Trace Route",justify=tk.CENTER,command=lambda:runCommand("tracert")).grid(row=0,column=1)
tk.Button(buttonFrame,text="NSLookup",justify=tk.CENTER,command=lambda:runCommand("nslookup")).grid(row=0,column=2)
ipAddress = tk.Entry(buttonFrame,justify=tk.CENTER)
ipAddress.grid(row=1, column=0,columnspan=3)

outputFrame = tk.Frame(root,width=312,height=272.5)
outputFrame.config(background="gray")
outputFrame.pack()

label = tk.Label(outputFrame,background="black",foreground="white",width=60,height=25,textvariable=output)
label.grid(row=0,column=0)
label.config(wraplength=400)
tk.Button(outputFrame,text="Save",justify=tk.CENTER,command=save).grid(row=1,column=0)

root.mainloop()