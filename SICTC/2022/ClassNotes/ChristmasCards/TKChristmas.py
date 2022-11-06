from tkinter import *
from random import randint
from PIL import ImageTk, Image
root = Tk() #creates the window

width = 600
height = 600

root.geometry(f"{height}x{width}")

# create canvas
canvas = Canvas(root,height=height,width=width,bg="black")
canvas.grid()
canvas.create_text(300, 100, text="Merry Christmas!", fill="white",font=30)

snow = []
for _ in range(100):
    randomX = randint(0,width)
    randomY = randint(0,height)
    snow.append(canvas.create_oval(randomX-2, randomY-2, randomX+2, randomY+2, fill="white"))

def randomize():
    for i in range(len(snow)):
        x1, y1, x2, y2 = canvas.coords(snow[i])
        move = (randint(0, 10)/10)
        canvas.coords(snow[i], x1+move, y1+move, x2+move, y2+move)
        if y2 > height:
            canvas.coords(snow[i], x1, 0, x2, 4)
        elif x2 > width:
            canvas.coords(snow[i], 0, y1, 4, y2)
    root.after(3, randomize)
randomize()

imgFile = Image.open("snowyground.png")#.resize((height, width))
imgTK = ImageTk.PhotoImage(imgFile)
img = canvas.create_image(300, 500, image=imgTK)

def createTree():
    canvas.create_polygon(width/2,height/2-160,width/2+50,height/2-50,width/2-50,height/2-50, fill="green")
    canvas.create_polygon(width/2,height/2-75,width/2+75,height/2+25,width/2-75,height/2+25, fill="green")
    canvas.create_polygon(width/2,height/2,width/2+120,height/2+120,width/2-120,height/2+120, fill="green")
    canvas.create_rectangle(width/2+25,height/2+120,width/2-25,height/2+200, fill="brown")

def createPresent():
    canvas.create_rectangle(width/2+75+25,height/2+200,width/2+75-25,height/2+160, fill="red")
    canvas.create_rectangle(width/2+75+25,height/2+185,width/2+75-25,height/2+175, fill="orange")
    canvas.create_rectangle(width/2+75+5,height/2+200,width/2+75-5,height/2+160, fill="orange")

def createStar():
    canvas.create_polygon(width/2+25,height/2-150+5,width/2-25,height/2-150+5,width/2,height/2-150-5, fill="yellow")
    canvas.create_polygon(width/2+5,height/2-150+25,width/2-5,height/2-150+5,width/2,height/2-150-25, fill="yellow")

def createSnowman():
    canvas.create_oval(width/2+150, height/2+150, width/2+150+100, height/2+150+100, fill="white")
    canvas.create_oval(width/2+160, height/2+100, width/2+160+75, height/2+100+75, fill="white")
    canvas.create_oval(width/2+165, height/2+70, width/2+160+60, height/2+50+75, fill="white")
    canvas.create_line(width/2+165, height/2+150, width/2+120, height/2+150, fill="brown")
    canvas.create_line(width/2+260, height/2+150, width/2+230, height/2+150, fill="brown")
    canvas.create_oval(width/2+175, height/2+90, width/2+175+10, height/2+90+10, fill="black")
    canvas.create_oval(width/2+200, height/2+90, width/2+200+10, height/2+90+10, fill="black")

createTree()
createPresent()
createStar()
createSnowman()

#drawing
#rectangle
#canvas.create_rectangle(width,height,0,0, fill="black", outline="orange")
#canvas.create_oval(width - 100, height - 100, 100, 100, fill="blue")
#canvas.create_text(width/2,height/2, text="Hello World!", fill="black")
#canvas.create_line(width, height, 0, 0)
#canvas.create_line(height, 0, 0, width)
#canvas.create_polygon(width/2, height/2-50, width/2+25, height/2+25-50, width/2-25, height/2+25-50)
#canvas.create_image(0, 0, image=PhotoImage(file="earth.png"))

# Startup
root.mainloop() #runs the window