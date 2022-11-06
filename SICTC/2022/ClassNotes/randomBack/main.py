import turtle as t
from random import randint
from PIL import ImageGrab

MAXTURTLES = 5
turtles = []

for i in range(MAXTURTLES):
    turtle = t.Turtle()
    turtle.speed(0)
    turtles.append(turtle)

def dump_gui():
    """
    takes a png screenshot of a tkinter window, and saves it on in cwd
    """
    print('...dumping gui window to png')
    ImageGrab.grab().crop().save("background.png")
    
dump_gui()


while True:
    for turtle in turtles:
        turtle.setheading(randint(0,360))
        turtle.forward(100)