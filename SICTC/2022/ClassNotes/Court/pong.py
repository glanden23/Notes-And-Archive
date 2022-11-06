from tkinter.tix import MAX
from turtle import *
from random import randint

# Game Settings
AI = True
# both of these can't be enabled.
AIVAI = False
bspeed = 20
MAXSPEED = 35
LOWSPEED = 10



collide1 = 60
collide2 = 60
size1=6
size2=6
bScore = 0
rScore = 0
bScoreRow = 0
rScoreRow = 0
lastScore = ""

def drawField():
    border = Turtle()
    border.color("white")
    border.speed(0)
    border.up()
    border.goto(500, 300)
    border.pensize(3)
    border.down()
    border.goto(-500, 300)
    border.up()
    border.goto(-500, -300)
    border.down()
    border.goto(500, -300)
    border.up()
    border.goto(0, -300)
    border.down()
    border.left(90)
    while border.ycor() < 300:
        border.forward(26)
        border.up()
        border.forward(26)
        border.down()
    border.hideturtle()

wn = Screen()
wn.bgcolor("black")
wn.setup(width = 1.0, height = 1.0)

paddle1 = Turtle(shape="square")
paddle2 = Turtle(shape="square")
paddle1.color("blue")
paddle2.color("red")
paddle1.speed(0)
paddle2.speed(0)
paddle1.turtlesize(size1,1)
paddle2.turtlesize(size2,1)
paddle1.up()
paddle2.up()
paddle1.goto(500, 0)
paddle2.goto(-500, 0)

writer = Turtle()
writer.hideturtle()
writer.up()
writer.color("white")
writer.speed(0)
writer2 = Turtle()
writer2.hideturtle()
writer2.up()
writer2.color("red")
writer2.speed(0)
writer3 = Turtle()
writer3.hideturtle()
writer3.up()
writer3.color("blue")
writer3.speed(0)

ball = Turtle(shape="circle")
ball.color("white")
ball.speed(0)
ball.up()

def up1():
    if paddle1.ycor() < 300:
        paddle1.sety(paddle1.ycor()+25)

def down1():
    if paddle1.ycor() > -300:
        paddle1.sety(paddle1.ycor()-25)

def up2():
    if paddle2.ycor() < 300:
        paddle2.sety(paddle2.ycor()+25)

def down2():
    if paddle2.ycor() > -300:
        paddle2.sety(paddle2.ycor()-25)

def writeSpeed():
    writer.clear()
    writer.goto(-500, 300)
    writer.write("Ball Speed: "+str(bspeed))

def writeScoreR():
    writer2.clear()
    writer2.goto(430, 300)
    writer2.write("Red Score: "+str(rScore))
    writer2.goto(330, 300)
    writer2.write("Red Streak: "+str(rScoreRow))

def writeScoreB():
    writer3.clear()
    writer3.goto(230, 300)
    writer3.write("Blue Score: "+str(bScore))
    writer3.goto(130, 300)
    writer3.write("Blue Streak: "+str(bScoreRow))

def ai(paddle):
    if (ball.ycor() > paddle.ycor() and ball.ycor() - paddle.ycor() > 25):
        if (randint(0,3) == 0):
            paddle.sety(paddle.ycor()+25)
    elif(ball.ycor() < paddle.ycor() and ball.ycor() - paddle.ycor() < -25):
        if (randint(0,3) == 0):
            paddle.sety(paddle.ycor()-25)
    
wn.listen()
if AIVAI != True:
    wn.onkeypress(up1, "Up")
    wn.onkeypress(down1, "Down")
    if AI != True:
        wn.onkeypress(up2, "w")
        wn.onkeypress(down2, "s")

drawField()
writeSpeed()
writeScoreR()
writeScoreB()

while True:
    wn.update()
    if paddle1.ycor() < -300:
        paddle1.goto(paddle1.xcor(), paddle1.ycor()+50)
    elif paddle1.ycor() > 300:
        paddle1.goto(paddle1.xcor(), paddle1.ycor()-50)
    if paddle2.ycor() < -300:
        paddle2.goto(paddle2.xcor(), paddle2.ycor()+50)
    elif paddle2.ycor() > 300:
        paddle2.goto(paddle2.xcor(), paddle2.ycor()-50)
    ball.forward(bspeed)
    if ball.distance(paddle1) < collide1:
        ball.setheading(180+((paddle1.ycor()+randint(-25,25))/10))
        if bspeed < MAXSPEED and bspeed > LOWSPEED:
            bspeed+=randint(-2, 2)
        elif bspeed >= MAXSPEED:
            bspeed+=randint(-2, 0)
        elif bspeed <= LOWSPEED:
            bspeed+=randint(0, 2)
        writeSpeed()
    elif ball.distance(paddle2) < collide2:
        ball.setheading(0+((paddle2.ycor()+randint(-25,25))/10))
        if bspeed < MAXSPEED and bspeed > LOWSPEED:
            bspeed+=randint(-2, 2)
        elif bspeed >= MAXSPEED:
            bspeed+=randint(-2, 0)
        elif bspeed <= LOWSPEED:
            bspeed+=randint(0, 2)
        writeSpeed()
    if ball.ycor() < -300:
        ball.goto(ball.xcor(),-290)
        ball.setheading(ball.heading()+25)
    elif ball.ycor() > 300:
        ball.goto(ball.xcor(),290)
        ball.setheading(ball.heading()-25)
    elif ball.xcor() > 500:
        ball.setheading(0)
        ball.goto(0,0)
        rScore+=1
        if lastScore == "Blue":
            bScoreRow=0
            writeScoreB()
            size2=6
            collide2=60
            paddle2.turtlesize(size2,1)
        lastScore="Red"
        rScoreRow+=1
        if rScoreRow % 3 == 0 and size1 > 1:
            size1-=1
            collide2-=10
            paddle1.turtlesize(size1,1)
        writeScoreR()
    elif ball.xcor() < -500:
        ball.setheading(180)
        ball.goto(0,0)
        bScore+=1
        if lastScore == "Red":
            rScoreRow=0
            writeScoreR()
            size1=6
            collide1=60
            paddle1.turtlesize(size2,1)
        lastScore="Blue"
        bScoreRow+=1
        if bScoreRow % 3 == 0 and size2 > 1:
            size2-=1
            collide2-=10
            paddle1.turtlesize(size2,1)
        writeScoreB()
    if AI:
        ai(paddle2)
    if AIVAI:
        ai(paddle1)
        ai(paddle2)