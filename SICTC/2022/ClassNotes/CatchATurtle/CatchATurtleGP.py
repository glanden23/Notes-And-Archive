# ------ Dependencies ------ #
import turtle as t
from random import randint
from os.path import exists
from time import sleep
import leaderboard as lb
wn = t.Screen()

# ------ Leaderboard ------ #
FILENAME = "leaderboard.txt"
#https://www.pythontutorial.net/python-basics/python-check-if-file-exists/
if not exists(FILENAME):
    open(FILENAME,"w+").close()

# ------ Game Settings ------ #
score=0
timer=10
timesUp=False

# ------ Draw/Startup ------ #
SCREENX, SCREENY = wn.window_width()/2-50, wn.window_height()/2-50
mo = t.Turtle()
mo.shape("turtle")
mo.shapesize(2)
mo.fillcolor("brown")

scoreKeeper = t.Turtle()
scoreKeeper.speed(0)
scoreKeeper.hideturtle()
scoreKeeper.penup()
scoreKeeper.goto(-320, 275)
scoreKeeper.write("Score: 0", False, align="Center", font=("Arial", 20, "normal"))

counter = t.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(300, 275)


# ------ FUNtions ------ #
def countdown():
    counter.clear()
    global timer, timesUp
    if timer <= 0:
        counter.goto(0,0)
        counter.write("Times up", align="center" , font=("Arial",30,"normal"))
        mo.hideturtle()
        manageLB()
    else:
        timer-=1
        counter.write(timer, font=("Arial",30,"normal"))
        wn.ontimer(countdown,1000)

# Prints current mouse cordinates along with the x and y of the mouse.
def moClicked(x,y):
    global score
    score+=1
    scoreKeeper.clear()
    scoreKeeper.write(f"Score: {score}", False, align="Center", font=("Arial", 20, "normal"))
    screenRandom()

# Move turtle to random location on screen.
def screenRandom():
    mo.penup()
    mo.hideturtle()
    mo.goto(randint(-SCREENX, SCREENX), randint(-SCREENY, SCREENY))
    mo.showturtle()
    mo.pendown()

#Read in top 5 scores and draw it on the screen.
def manageLB():
    scoreKeeper.clear()
    scoreKeeper.goto(0,0)
    
    #parallel list -> same length with data related to each other.
    namesList = lb.getNames(FILENAME)
    print(namesList)
    scoreList = lb.getScore(FILENAME)
    print(scoreList)
    
    #show leaderboard with current player
manageLB()
    

# ------ Events ------ #
mo.onclick(moClicked)
wn.ontimer(countdown,1000)


# ------ Main Window Loop ------ #
wn.mainloop()