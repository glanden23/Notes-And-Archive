import os
import turtle as t

os.system('exit')
turtle = t.Turtle()
turtle.shape("square")
turtle.speed(0)
turtle.shapesize(3)
turtle.color("red")
turtle.up()
turtle.hideturtle()
wn = t.Screen()

color=0
x=-300
y=-300
while(y<300):
    if (x>300):
        y+=60
        x=-300
    turtle.goto(x,y)
    if (y<300):
        turtle.stamp()
    x+=60
    if (color == 0):
        turtle.color("black")
        color=1
    else:
        color=0
        turtle.color("red")

wn.mainloop()