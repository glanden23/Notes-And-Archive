#   a113_flower.py
#   This code draws a flower.
import turtle as trtl
import random
painter = trtl.Turtle()
painter.speed(0)
# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)
# change pen
painter.penup()
painter.shape("triangle")
painter.turtlesize(3)
def randoColor():
     r=random.randint(0,255)
     g=random.randint(0,255)
     b=random.randint(0,255)
     return r,g,b      #return a tuple of rgb
trtl.colormode(255) #to allow the color to take RGB
# draw flower
for i in range(1000):
    painter.goto(12,90)
    painter.color("red")
    painter.stamp()
    painter.color(randoColor())
    painter.goto(20,180)
    petals = 0
    while (petals < 18):
        painter.color("white")     
        painter.right(20)
        painter.forward(30)
        painter.stamp()  #is literally a stamp
        painter.color("black")
        painter.stamp()
        petals = petals + 1
    painter.goto(12,90)
    painter.color("red")
    painter.stamp()
    painter.goto(20,150)        #CHANGED
    petals = 0
    while (petals < 12):        #CHANGED
        painter.color("white")     
        painter.right(30)        #CHANGED
        painter.forward(30)
        painter.stamp()
        painter.color("black")
        painter.stamp()
        petals = petals + 1
    painter.goto(12,90)
    painter.color("red")
    painter.stamp()
    painter.goto(20,120)        #CHANGED
    petals = 0
    while (petals < 6):        #CHANGED
        painter.color("white")     
        painter.right(60)        #CHANGED
        painter.forward(30)
        painter.stamp()
        painter.color("black")
        painter.stamp()
        petals = petals + 1
wn = trtl.Screen()
wn.mainloop()