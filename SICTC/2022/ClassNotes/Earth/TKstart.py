from tkinter import *
import tkinter as tk
from time import sleep
from random import randint
root = Tk() #creates the window

screenWidth = 600
screenHeight = 600

root.geometry("600x600")

# create canvas
canvas = Canvas(root,height=screenHeight,width=screenWidth)
canvas.grid()

def clearCanvas():
    print("Clearing...")
    canvas.delete("all")

def createGlobe():
    canvas.create_rectangle(screenWidth,screenHeight,0,0, fill="black")
    canvas.create_oval(screenWidth - 100, screenHeight - 100, 100, 100, fill="blue")
    button = tk.Button(root, text="Hello World", width=10, height=1, command=clearCanvas)
    button.place(x=screenWidth/2-40, y=screenHeight/2-215)
    generateLand(5)

def generateLand(amount):
    for i in range(amount):
        canvas.create_polygon(screenWidth/2, screenHeight/2, screenWidth/2+randint(-200, 200), screenHeight/2+randint(-200, 200), fill="green")   
createGlobe()

#drawing
#rectangle
#canvas.create_rectangle(screenWidth,screenHeight,0,0, fill="black", outline="orange")
#canvas.create_oval(screenWidth - 100, screenHeight - 100, 100, 100, fill="blue")
#canvas.create_text(screenWidth/2,screenHeight/2, text="Hello World!", fill="black")
#canvas.create_line(screenWidth, screenHeight, 0, 0)
#canvas.create_line(screenHeight, 0, 0, screenWidth)
#canvas.create_polygon(screenWidth/2, screenHeight/2-50, screenWidth/2+25, screenHeight/2+25-50, screenWidth/2-25, screenHeight/2+25-50)
#canvas.create_image(0, 0, image=PhotoImage(file="earth.png"))

# Startup
root.mainloop() #runs the window