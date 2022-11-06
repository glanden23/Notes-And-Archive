from turtle import *
from random import randint
from os.path import exists
from datetime import datetime
from time import sleep

# Game Settings

multiplay = False
size = 50
lineLength = 700
wallChance = 20
openChance = 3

# ---------------

runner = Turtle()
runner.hideturtle()
runner.color("white")
maze = Turtle()
maze.hideturtle()
maze.color("white")
timer = Turtle()
timer.hideturtle()
timer.up()
timer.speed(0)
timer.goto(400, 400)
timer.color("white")
scoreT = Turtle()
scoreT.hideturtle()
scoreT.up()
scoreT.speed(0)
scoreT.goto(300, 400)
scoreT.color("white")
leaderboardT = Turtle()
leaderboardT.hideturtle()
leaderboardT.up()
leaderboardT.speed(0)
leaderboardT.goto(0, 100)
leaderboardT.color("white")

time = 0
speed = 0.5
score = 0
walls = []
ghosts = []
cuser = str(datetime.now()).split(".")[0]

for _ in range(3):
    ghost = Turtle(shape="circle")
    ghost.color("gray")
    ghost.speed(0)
    ghost.up()
    ghost.goto(randint(-300, 300),randint(-300, 300))
    ghosts.append(ghost)
del ghost

if multiplay:
    runner2 = Turtle()
    runner2.hideturtle()
    runner2.color("red")
    runner.color("blue")
    speed2 = 0.5

def databaseStartup():
    file = exists('./leaderboard.data')
    if file == False:
        open("./leaderboard.data", "w+")
        return True
    else:
        return False

def databaseInput(search, value):
    file = open('./leaderboard.data', "r")
    data = file.read()
    if search in data:
        datalist = data.split(" | ")
        for x in range(len(datalist)):
            if datalist[x].startswith(search):
                datalist[x] = search+"; "+value
                file = open('./leaderboard.data', "w")
                newdata = " | ".join(datalist)
                file.write(newdata)
    else:
        file = open('./leaderboard.data', "w")
        file.write(data+search+"; "+value+" | ")

databaseStartup()

def PtoW():
    if maze.heading() == 0:
        for i in range(size):
            walls.append([round(maze.xcor(),0)+i, round(maze.ycor(),0)])
    elif maze.heading() == 90:
        for i in range(size):
            walls.append([round(maze.xcor(),0), round(maze.ycor(),0)+i])
    elif maze.heading() == 180:
        for i in range(size):
            walls.append([round(maze.xcor(),0)-i, round(maze.ycor(),0)])
    elif maze.heading() == 270:
        for i in range(size):
            walls.append([round(maze.xcor(),0), round(maze.ycor(),0)-i])

def createMaze():
    global time
    maze.speed(0)
    maze.pensize(5)
    maze.up()
    maze.goto(350, 350)
    maze.right(90)
    maze.down()
    loops = 0
    wall = 0
    while lineLength-(loops*size) > 0:
        for _ in range(2):
            time = -1
            lineLen = lineLength-(loops*size)
            while lineLen > 0:
                if (randint(0, openChance) == 0 and loops > 1 and lineLength-(loops*size) > 200):
                    maze.up()
                    maze.forward(size)
                    maze.down()
                elif(randint(0, wallChance) == 0 and loops > 1 and lineLength-(loops*size) > 200):
                    maze.right(90)
                    PtoW()
                    maze.forward(size)
                    maze.back(size)
                    maze.left(90)
                    maze.forward(size)
                else:
                    PtoW()
                    maze.forward(size)
                lineLen-=size
            wall+=1
            maze.right(90)
        loops+=1
    maze.up()
    maze.goto(0,0)
    maze.color("red")
    maze.shape("circle")
    maze.stamp()
    maze.shape("arrow")
    maze.color("white")
    maze.setheading(0)

def runRunner():
    global speed, time, score
    runner.showturtle()
    runner.setheading(0)
    runner.speed(0)
    runner.up()
    runner.goto(337.5, 300)
    runner.right(90)
    gameOver = False
    while gameOver != True:
        wn.update()
        runner.forward(speed)
        if randint(0, 50) == 0:
            ghost = ghosts[randint(0, len(ghosts)-1)]
            #https://stackoverflow.com/questions/35530937/how-to-make-a-turtle-object-look-at-where-the-mouse-has-clicked
            ghost.left(ghost.towards(runner.xcor(), runner.ycor()) - ghost.heading())
            #----
            ghost.forward(randint(25, 30))
            if ghost.distance(runner) < 20:
                gameOver = True
                reRun()
        if [round(runner.xcor(),0), round(runner.ycor(),0)] in walls or runner.ycor() > 350 or runner.ycor() < -350 or runner.xcor() < -350 or runner.xcor() > 350:
            gameOver = True
            reRun()
        elif round(runner.xcor(),0) < 10 and round(runner.ycor(),0) < 10 and round(runner.xcor(),0) > -10 and round(runner.ycor(),0) > -10:
            gameOver = True
            score+=1
            writeScore()
            reRun()

def runRunnerM():
    global speed, speed2, time, score
    runner.showturtle()
    runner.setheading(0)
    runner.speed(0)
    runner.up()
    runner.goto(337.5, 300)
    runner.right(90)
    runner2.showturtle()
    runner2.setheading(0)
    runner2.speed(0)
    runner2.up()
    runner2.goto(325, 300)
    runner2.right(90)
    gameOver = False
    while gameOver != True:
        wn.update()
        runner.forward(speed)
        runner2.forward(speed2)
        if randint(0, 50) == 0:
            ghost = ghosts[randint(0, len(ghosts)-1)]
            #https://stackoverflow.com/questions/35530937/how-to-make-a-turtle-object-look-at-where-the-mouse-has-clicked
            ghost.left(ghost.towards(runner.xcor(), runner.ycor()) - ghost.heading())
            #----
            ghost.forward(randint(25, 30))
            if ghost.distance(runner) < 20:
                gameOver = True
                reRunM()
        if randint(0, 50) == 0:
            ghost = ghosts[randint(0, len(ghosts)-1)]
            #https://stackoverflow.com/questions/35530937/how-to-make-a-turtle-object-look-at-where-the-mouse-has-clicked
            ghost.left(ghost.towards(runner2.xcor(), runner2.ycor()) - ghost.heading())
            #----
            ghost.forward(randint(25, 30))
            if ghost.distance(runner2) < 20:
                gameOver = True
                reRunM()
        if [round(runner.xcor(),0), round(runner.ycor(),0)] in walls or runner.ycor() > 350 or runner.ycor() < -350 or runner.xcor() < -350 or runner.xcor() > 350:
            gameOver = True
            reRunM()
        elif round(runner.xcor(),0) < 10 and round(runner.ycor(),0) < 10 and round(runner.xcor(),0) > -10 and round(runner.ycor(),0) > -10:
            gameOver = True
            score+=1
            writeScore()
            reRunM()
        if [round(runner2.xcor(),0), round(runner2.ycor(),0)] in walls or runner2.ycor() > 350 or runner2.ycor() < -350 or runner2.xcor() < -350 or runner2.xcor() > 350:
            gameOver = True
            reRunM()
        elif round(runner2.xcor(),0) < 10 and round(runner2.ycor(),0) < 10 and round(runner2.xcor(),0) > -10 and round(runner2.ycor(),0) > -10:
            gameOver = True
            score+=1
            writeScore()
            reRunM()

def runTimer():
    global time
    timer.clear()
    time+=1
    timer.write("Current Time: "+str(time))
    wn.ontimer(runTimer, 1000)

def writeScore():
    scoreT.clear()
    scoreT.write("Score: "+str(score))

def writeLeaderboard():
    leaderboardT.clear()
    top3s = [-1,-1,-1]
    top3n = ["NO USER","NO USER","NO USER"]
    data = open("./leaderboard.data").read().split(" | ")
    data.pop()
    for i in data:
        data = int(i.split(";")[1])
        name = i.split(";")[0]
        data1, data2, data3 = top3s[0], top3s[1], top3s[2]
        name1, name2, name3 = top3n[0], top3n[1], top3n[2]
        if data > data1:
            top3s[0] = data
            top3n[0] = name
            top3s[1] = data1
            top3n[1] = name1
        elif data > data2:
            top3s[1] = data
            top3n[1] = name
            top3s[2] = data2
            top3n[2] = name2
        elif data > data3:
            top3s[2] = data
            top3n[2] = name
        if data1 < data2:
            top3s[1] = data2
            top3s[2] = data1
            top3n[1] = name2
            top3n[2] = name1
        elif data2 < data3:
            top3s[2] = data2
            top3s[1] = data3
            top3n[1] = name3
            top3n[2] = name2
    leaderboardT.write(f"{top3n[0]}: {top3s[0]}\n{top3n[1]}: {top3s[1]}\n{top3n[2]}: {top3s[2]}",font=("Arial",30,"normal"),align="center")
    sleep(3)
    leaderboardT.clear()

writeScore()

def reRun():
    for i in ghosts:
        i.goto(randint(-300, 300),randint(-300, 300))
    maze.clear()
    runner.hideturtle()
    walls.clear()
    databaseInput(cuser, str(score))
    writeLeaderboard()
    createMaze()
    runRunner()

def reRunM():
    for i in ghosts:
        i.goto(randint(-300, 300),randint(-300, 300))
    maze.clear()
    runner.hideturtle()
    runner2.hideturtle()
    walls.clear()
    databaseInput(cuser, str(score))
    writeLeaderboard()
    createMaze()
    runRunnerM()

def right():
    runner.setheading(0)
def left():
    runner.setheading(180)
def down():
    runner.setheading(270)
def up():
    runner.setheading(90)
def speedUp():
    global speed
    speed = 1
def slowDown():
    global speed
    speed = 0.5

def rightM():
    runner2.setheading(0)
def leftM():
    runner2.setheading(180)
def downM():
    runner2.setheading(270)
def upM():
    runner2.setheading(90)
def speedUpM():
    global speed2
    speed2 = 1
def slowDownM():
    global speed2
    speed2 = 0.5

wn = Screen()
#https://stackoverflow.com/questions/34687998/turtle-screen-fullscreen-on-program-startup
wn.screensize()
wn.setup(width = 1.0, height = 1.0)
#-----
wn.listen()
wn.bgcolor("black")
#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
if multiplay != True:
    wn.onkeypress(up, "w")
    wn.onkeypress(up, "W")
    wn.onkeypress(left, "a")
    wn.onkeypress(left, "A")
    wn.onkeypress(right, "d")
    wn.onkeypress(right, "D")
    wn.onkeypress(down, "S")
    wn.onkeypress(down, "s")
else:
    wn.onkeypress(upM, "w")
    wn.onkeypress(upM, "W")
    wn.onkeypress(leftM, "a")
    wn.onkeypress(leftM, "A")
    wn.onkeypress(rightM, "d")
    wn.onkeypress(rightM, "D")
    wn.onkeypress(downM, "S")
    wn.onkeypress(downM, "s")
    wn.onkeypress(speedUpM, "Shift_L")
    wn.onkeyrelease(slowDownM, "Shift_L")
wn.onkeypress(speedUp, "space")
wn.onkeyrelease(slowDown, "space")
wn.ontimer(runTimer, 1000)

createMaze()
if multiplay:
    runRunnerM()
else:
    runRunner()
