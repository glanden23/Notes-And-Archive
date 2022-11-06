import turtle as t
from random import randint
from time import sleep

drawer = t.Turtle()
drawer.speed(0)
wn = t.Screen()

# Road
drawer.penup()
drawer.fillcolor("black")
drawer.begin_fill()
drawer.goto(-400, 150)
drawer.pendown()
#draw rectangle
for _ in range(2):
    drawer.forward(800)
    drawer.right(90)
    drawer.forward(200)
    drawer.right(90)
drawer.end_fill()
#draws yellow line
drawer.color("yellow")
drawer.penup()
drawer.goto(-400, 50)
drawer.pendown()
drawer.forward(800)
#draws first white line
drawer.color("white")
drawer.penup()
drawer.goto(-400, 0)
while drawer.xcor() < 400:
    drawer.forward(10)
    drawer.penup()
    drawer.forward(15)
    drawer.pendown()
#draws second white line
drawer.penup()
drawer.goto(-400, 100)
while drawer.xcor() < 400:
    drawer.forward(10)
    drawer.penup()
    drawer.forward(15)
    drawer.pendown()

# Road 2
drawer.penup()
drawer.fillcolor("black")
drawer.begin_fill()
drawer.goto(-100, 400)
drawer.pendown()
#draw rectangle
for _ in range(2):
    drawer.forward(200)
    drawer.right(90)
    drawer.forward(800)
    drawer.right(90)
drawer.end_fill()
#draws yellow line
drawer.color("yellow")
drawer.penup()
drawer.goto(0, 400)
drawer.pendown()
drawer.right(90)
drawer.forward(250)
drawer.penup()
drawer.forward(200)
drawer.pendown()
drawer.forward(250)
#draws first white line
drawer.color("white")
drawer.penup()
drawer.goto(50, 400)
while drawer.ycor() > -400:
    if (drawer.ycor() < 150 and drawer.ycor() > -35):
        drawer.penup()
        drawer.forward(10)
    else:
        drawer.forward(10)
        drawer.penup()
        drawer.forward(15)
        drawer.pendown()
#draws second white line
drawer.penup()
drawer.goto(-50, 400)
while drawer.ycor() > -400:
    if (drawer.ycor() < 150 and drawer.ycor() > -35):
        drawer.penup()
        drawer.forward(10)
    else:
        drawer.forward(10)
        drawer.penup()
        drawer.forward(15)
        drawer.pendown()

# Discard turtle
drawer.hideturtle()
drawer.penup()
drawer.shape("circle")

stopped = []
lights=["green","red"]

def drawLights():
    global lights, stopped
    stopped = []
    #First 4 way lights
    drawer.goto(100, 100)
    drawer.color(lights[0])
    drawer.stamp()
    drawer.goto(-100, 100)
    drawer.color(lights[0])
    drawer.stamp()
    drawer.goto(-100, 0)
    drawer.color(lights[0])
    drawer.stamp()
    drawer.goto(100, 0)
    drawer.color(lights[0])
    drawer.stamp()
    #Second 4 way lights
    drawer.goto(-50, -50)
    drawer.color(lights[1])
    drawer.stamp()
    drawer.goto(50, -50)
    drawer.color(lights[1])
    drawer.stamp()
    drawer.goto(-50, 150)
    drawer.color(lights[1])
    drawer.stamp()
    drawer.goto(50, 150)
    drawer.color(lights[1])
    drawer.stamp()
    if (lights[0] == "green"):
        lights=["red","green"]
    else:
        lights=["green","red"]
    wn.ontimer(drawLights,randint(10, 20)^10000)
        

drawLights()

traffic1 = []
traffic2 = []
traffic3 = []
traffic4 = []
#traffic 1
for _ in range(5):
    turtle = t.Turtle()
    turtle.color("blue")
    turtle.speed(10)
    turtle.shapesize(3)
    turtle.penup()
    turtle.goto(randint(-300,300), -20)
    traffic1.append(turtle)
#traffic 2
for _ in range(5):
    turtle = t.Turtle()
    turtle.color("blue")
    turtle.speed(10)
    turtle.shapesize(3)
    turtle.penup()
    turtle.setheading(180)
    turtle.goto(randint(-300,300), 120)
    traffic2.append(turtle)
#traffic 3
for _ in range(0):
    turtle = t.Turtle()
    turtle.color("orange")
    turtle.speed(10)
    turtle.shapesize(3)
    turtle.penup()
    turtle.setheading(90)
    turtle.goto(75, randint(-300,300))
    traffic3.append(turtle)
#traffic 4
for _ in range(0):
    turtle = t.Turtle()
    turtle.color("orange")
    turtle.speed(10)
    turtle.shapesize(3)
    turtle.penup()
    turtle.setheading(270)
    turtle.goto(-75, randint(-300,300))
    traffic4.append(turtle)

#checks if cars are too close and switches lanes if they are
def collisionCheck(traffic, type):
    for m in traffic:
        for i in traffic:
            if i != m:
                if abs(m.xcor() - i.xcor()) < 30 and abs(m.ycor() - i.ycor()) < 30:
                    if type == 1:
                        laneChange(i)
                    else:
                        laneChange2(i)
                    i.forward(100)

def stopCollisionCheck(traffic,type):
    for m in traffic:
        for i in traffic:
            if i != m:
                if abs(m.xcor() - i.xcor()) < 30 and abs(m.ycor() - i.ycor()) < 30:
                    if not m in stopped:
                        stopped.append(m)

#checks cords and moves car to other lane
def laneChange(i):
    if i.ycor() == -20:
        i.goto(i.xcor(), 20)
        i.speed(0)
    elif i.ycor() == 20:
        i.goto(i.xcor(), -20)
        i.speed(10)
    elif i.ycor() == 120:
        i.goto(i.xcor(), 80)
        i.speed(0)
    else:
        i.goto(i.xcor(), 120)
        i.speed(10)

def laneChange2(i):
    print(i.xcor())
    if i.xcor() == 25:
        i.goto(75, i.ycor())
        i.speed(10)
    elif i.xcor() == 75:
        i.goto(25, i.ycor())
        i.speed(0)
    elif i.xcor() == -25:
        i.goto(-75, i.ycor())
        i.speed(10)
    else:
        i.goto(-25, i.ycor())
        i.speed(0)
        

# movement loop to keep cars going and runs collision checks
while True:
    if lights[1] == "green":
        for i in traffic1:
            if i.speed() == 0:
                i.forward(randint(15, 20))
            else:
                i.forward(randint(5, 10))
            collisionCheck(traffic1,1)
            if i.xcor() > 400:
                speed = i.speed()
                i.speed(0)
                i.hideturtle()
                i.goto(-400, i.ycor())
                i.showturtle()
                i.speed(speed)
        for i in traffic2:
            if i.speed() == 0:
                i.forward(randint(15, 20))
            else:
                i.forward(randint(5, 10))
            collisionCheck(traffic2,1)
            if i.xcor() < -400:
                speed = i.speed()
                i.speed(0)
                i.hideturtle()
                i.goto(400, i.ycor())
                i.showturtle()
                i.speed(speed)
    else:
        for i in traffic1:
            stopCollisionCheck(traffic1, 1)
            if (i.xcor() > -90 and i.xcor() < 90):
                i.forward(100)
            elif(i.xcor() < -90 or i.xcor() > 90):
                if not i in stopped:
                    i.forward(10)
            if i.xcor() > 400:
                speed = i.speed()
                i.speed(0)
                i.hideturtle()
                i.goto(-400, i.ycor())
                i.showturtle()
                i.speed(speed)
        for i in traffic2:
            stopCollisionCheck(traffic2, 1)
            if (i.xcor() > -90 and i.xcor() < 90):
                i.forward(100)
            elif(i.xcor() > 130 or i.xcor() < -90):
                if not i in stopped:
                    i.forward(10)
            if i.xcor() < -400:
                speed = i.speed()
                i.speed(0)
                i.hideturtle()
                i.goto(400, i.ycor())
                i.showturtle()
                i.speed(speed)
        for i in traffic3:
            if i.speed() == 0:
                i.forward(randint(15, 20))
            else:
                i.forward(randint(5, 10))
            collisionCheck(traffic3,2)
            if i.ycor() > 400:
                speed = i.speed()
                i.speed(0)
                i.hideturtle()
                i.goto(i.xcor(), -400)
                i.showturtle()
                i.speed(speed)
        for i in traffic4:
            if i.speed() == 0:
                i.forward(randint(15, 20))
            else:
                i.forward(randint(5, 10))
            collisionCheck(traffic4,2)
            if i.ycor() < -400:
                speed = i.speed()
                i.speed(0)
                i.hideturtle()
                i.goto(i.xcor(), 400)
                i.showturtle()
                i.speed(speed)