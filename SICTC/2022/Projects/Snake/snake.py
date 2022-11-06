# Game Features: PvP, Speeds up as eat food, Window title, pause button (esc)
# Code is Dry, 

#import
from turtle import *
from random import randint

# Game Settings
snakeSpeed = 3 #start speed
snakeSize = 1 #start size
snakeColor = 0
# Players may not attack each other until 1 food has been picked up by both.
PvP = False
# Hunts down food for you
Bot = True

mainSnake = Turtle(shape="square")
mainSnake.up()
mainSnake.speed(0)
mainSnake.direction="stop"
snakeBody = []

if PvP:
    # Game Settings Player #2
    snakeSpeed2 = 3 #start speed
    snakeSize2 = 1 #start size
    snakeColor2 = 0
    
    mainSnake2 = Turtle(shape="square")
    mainSnake2.up()
    mainSnake2.speed(0)
    mainSnake2.direction="stop"
    snakeBody2 = []

if Bot:
    lastSwap = ""

notPaused = True

food = Turtle(shape="circle")
food.color("red")
food.up()
food.speed(0)

def snakeUp():
    if mainSnake.direction != "down":
        mainSnake.direction="up"  

def snakeDown():
    if mainSnake.direction != "up":
        mainSnake.direction="down"   

def snakeLeft():
    if mainSnake.direction!="right":
        mainSnake.direction="left"

def snakeRight():
    if mainSnake.direction!="left":
        mainSnake.direction="right"

if PvP:
    def snakeUp2():
        if mainSnake2.direction != "down":
            mainSnake2.direction="up"  

    def snakeDown2():
        if mainSnake2.direction != "up":
            mainSnake2.direction="down"   

    def snakeLeft2():
        if mainSnake2.direction!="right":
            mainSnake2.direction="left"

    def snakeRight2():
        if mainSnake2.direction!="left":
            mainSnake2.direction="right"

def randFood():
    food.goto(randint(int(-wn.window_width()/2+250), int(wn.window_width()/2-250)), randint(int(-wn.window_height()/2+250), int(wn.window_height()/2-250)))

def addSnakeLen():
    global snakeSpeed, snakeSize, snakeColor
    new = mainSnake.clone()
    if snakeColor == 0:
        new.color("blue")
        snakeColor = 1
    else:
        new.color("cyan")
        snakeColor = 0
    snakeBody.append(new)
    print(len(snakeBody))
    snakeSpeed+=3
    snakeSize+=0.1
    mainSnake.shapesize(snakeSize)
    for i in snakeBody:
        i.shapesize(snakeSize)

if PvP:
    def addSnakeLen2():
        global snakeSpeed2, snakeSize2, snakeColor2
        new = mainSnake2.clone()
        if snakeColor2 == 0:
            new.color("blue")
            snakeColor2 = 1
        else:
            new.color("cyan")
            snakeColor2 = 0
        snakeBody2.append(new)
        print(len(snakeBody2))
        snakeSpeed2+=3
        snakeSize2+=0.1
        mainSnake2.shapesize(snakeSize2)
        for i in snakeBody2:
            i.shapesize(snakeSize2)

def pause():
    global notPaused
    if (notPaused == True):
        notPaused = False
    else:
        notPaused = True

wn = Screen()
wn.title("Snake")
wn.setup(width=1.0, height=1.0)
wn.bgcolor("lightgreen")

randFood()

wn.listen()
if not Bot:
    wn.onkeypress(snakeUp,"Up")
    wn.onkeypress(snakeDown,"Down")
    wn.onkeypress(snakeRight,"Right")
    wn.onkeypress(snakeLeft, "Left")
if PvP:
    wn.onkeypress(snakeUp2,"w")
    wn.onkeypress(snakeDown2,"s")
    wn.onkeypress(snakeRight2,"d")
    wn.onkeypress(snakeLeft2, "a")
wn.onkeypress(pause, "Escape")

def player1():
    global snakeSpeed, snakeSize, lastSwap
    mainSnake.goto(mainSnake.xcor(), mainSnake.ycor())
    if (mainSnake.distance(food) < 20+snakeSpeed):
        randFood()
        addSnakeLen()
    
    for i in range(len(snakeBody)-1, 0, -1):
        snakeBody[i].goto(snakeBody[i-1].xcor(),snakeBody[i-1].ycor())
    
    if len(snakeBody)>0:
        snakeBody[0].goto(mainSnake.xcor(), mainSnake.ycor())

    if Bot:
        if food.xcor() > mainSnake.xcor() and mainSnake.direction != "left":
            mainSnake.direction = "right"
            lastSwap = "right"
        elif food.xcor() < mainSnake.xcor() and mainSnake.direction != "right":
            mainSnake.direction = "left"
            lastSwap = "left"
        elif food.ycor() > mainSnake.ycor() and mainSnake.direction != "down":
            mainSnake.direction = "up"
            lastSwap = "up"
        elif food.ycor() < mainSnake.ycor() and mainSnake.direction != "up":
            mainSnake.direction = "down"
            lastSwap = "down"
            
    if mainSnake.direction == "up":
        y = mainSnake.ycor()
        mainSnake.sety(y+snakeSpeed)
    elif mainSnake.direction == "down":
        y = mainSnake.ycor()
        mainSnake.sety(y-snakeSpeed)
    elif mainSnake.direction == "right":
        x = mainSnake.xcor()
        mainSnake.setx(x+snakeSpeed)
    elif mainSnake.direction == "left":
        x = mainSnake.xcor()
        mainSnake.setx(x-snakeSpeed)
        
    for i in snakeBody:
        if (mainSnake.distance(i) < snakeSize*2):
            for i in snakeBody:
                i.hideturtle()
            snakeBody.clear()
            mainSnake.goto(0,0)
            snakeSpeed = 3
            snakeSize = 1
            mainSnake.shapesize(snakeSize)
    
    if (mainSnake.xcor() > wn.window_width()/2):
        mainSnake.goto(-wn.window_width()/2,mainSnake.ycor())
    elif(mainSnake.xcor() < -wn.window_width()/2):
        mainSnake.goto(wn.window_width()/2,mainSnake.ycor())
    elif(mainSnake.ycor() > wn.window_height()/2):
        mainSnake.goto(mainSnake.xcor(),-wn.window_height()/2)
    elif(mainSnake.ycor() < -wn.window_height()/2):
        mainSnake.goto(mainSnake.xcor(),wn.window_height()/2)

def player2():
    global snakeSpeed2, snakeSize2
    mainSnake2.goto(mainSnake2.xcor(), mainSnake2.ycor())
    if (mainSnake2.distance(food) < 20+snakeSpeed2):
        randFood()
        addSnakeLen2()
    
    for i in range(len(snakeBody2)-1, 0, -1):
        snakeBody2[i].goto(snakeBody2[i-1].xcor(),snakeBody2[i-1].ycor())
    
    if len(snakeBody2)>0:
        snakeBody2[0].goto(mainSnake2.xcor(), mainSnake2.ycor())
    
    if mainSnake2.direction == "up":
        y = mainSnake2.ycor()
        mainSnake2.sety(y+snakeSpeed2)
    elif mainSnake2.direction == "down":
        y = mainSnake2.ycor()
        mainSnake2.sety(y-snakeSpeed2)
    elif mainSnake2.direction == "right":
        x = mainSnake2.xcor()
        mainSnake2.setx(x+snakeSpeed2)
    elif mainSnake2.direction == "left":
        x = mainSnake2.xcor()
        mainSnake2.setx(x-snakeSpeed2)
        
    for i in snakeBody2:
        if (mainSnake2.distance(i) < snakeSize2*2):
            for i in snakeBody2:
                i.hideturtle()
            snakeBody2.clear()
            mainSnake2.goto(0,0)
            snakeSpeed2 = 3
            snakeSize2 = 1
            mainSnake2.shapesize(snakeSize)
    
    if (mainSnake2.xcor() > wn.window_width()/2):
        mainSnake2.goto(-wn.window_width()/2,mainSnake2.ycor())
    elif(mainSnake2.xcor() < -wn.window_width()/2):
        mainSnake2.goto(wn.window_width()/2,mainSnake2.ycor())
    elif(mainSnake2.ycor() > wn.window_height()/2):
        mainSnake2.goto(mainSnake2.xcor(),-wn.window_height()/2)
    elif(mainSnake2.ycor() < -wn.window_height()/2):
        mainSnake2.goto(mainSnake2.xcor(),wn.window_height()/2)

# Singleplayer loop
if not PvP:
    while True:
        wn.update()
        if (notPaused):
            player1()
# PVP loop
else:
    while True:
        wn.update()
        if (notPaused):
            player1()
            player2()
            
            # PVP exclusive checks
            for i in snakeBody:
                if (mainSnake2.distance(i) < snakeSize*2):
                    for i in snakeBody2:
                        i.hideturtle()
                    snakeBody2.clear()
                    mainSnake2.goto(0,0)
                    snakeSpeed2 = 3
                    snakeSize2 = 1
                    mainSnake2.shapesize(snakeSize2)
            
            for i in snakeBody2:
                if (mainSnake.distance(i) < snakeSize2*2):
                    for i in snakeBody:
                        i.hideturtle()
                    snakeBody.clear()
                    mainSnake.goto(0,0)
                    snakeSpeed = 3
                    snakeSize = 1
                    mainSnake.shapesize(snakeSize)