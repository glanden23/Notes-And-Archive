from tkinter import *
from random import randint
from PIL import ImageTk, Image
height, width = 600, 600

root = Tk()
root.geometry(f"{height}x{width}")

canvas = Canvas(root, height=height, width=width, bg="black")
canvas.grid()
canvas.create_text(300, 100, text="Merry Christmas!", fill="white",font=30)

imgFile = Image.open("snowyground.png").resize((height, width))
imgTK = ImageTk.PhotoImage(imgFile)
img = canvas.create_image(300, 500, image=imgTK)

snow = []
for _ in range(50):
    randomX = randint(0,width)
    randomY = randint(0,height)
    snow.append(canvas.create_rectangle(randomX-2, randomY-2, randomX+2, randomY+2, fill="white"))

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

root.mainloop()