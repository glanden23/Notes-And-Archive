# ------ Dependencies ------ #
import turtle as t
from random import randint
from time import sleep
wn = t.Screen()
mClicks=0
clicks=0
size=5

# ------ Game Settings ------ #
score=0
timer=10
timesUp=False

# ------ Startup ------ #
SCREENX, SCREENY = wn.window_width()/2-100, wn.window_height()/2-100
start=t.Turtle()
start.penup()
start.speed(0)
# Create Turtles
mo = t.Turtle()
scoreKeeper = t.Turtle()
counter = t.Turtle()
mo.shape("turtle")
mo.shapesize(size)
mo.color("red")
mo.pencolor("white")
mo.hideturtle()
scoreKeeper.speed(0)
scoreKeeper.penup()
scoreKeeper.goto(-320, 275)
scoreKeeper.hideturtle()
counter.speed(0)
counter.penup()
counter.goto(300, 275)
counter.hideturtle()

def begin(x,y):
    start.hideturtle()
    start.clear()
    scoreKeeper.write("Score: 0", False, align="Center", font=("Arial", 20, "normal"))
    countdown()
    screenRandom()

def startup():
    start.shape('square')
    start.goto(0, 200)
    start.write("Click the square to start!", align="center", font=("Comic Sans",30,"bold"))
    start.goto(0,0)
    start.shapesize(12)
    start.fillcolor('gray')
    start.onclick(begin)
startup()

# ------ FUNtions ------ #

# Countdown until 0 is reached.
def countdown():
    counter.clear()
    global timer, timesUp
    if timer <= 0:
        counter.goto(0, 0)
        scoreKeeper.clear()
        mo.hideturtle()
        wn.bgcolor("orange")
        counter.write("Times up! Your score was " + str(score) + "\nwith an accuracy of " + str(round((clicks/mClicks)*100, 2))+"%!", align="center", font=("Arial",30,"normal"))
        sleep(10)
        exit()
    else:
        timer-=1
        counter.write(timer, font=("Arial",30,"normal"))
        wn.ontimer(countdown,1000)

# Prints current mouse cordinates along with the x and y of the mouse.
def moClicked(x,y):
    global score,size,clicks
    score+=1
    clicks+=1
    size-=0.5
    mo.shapesize(size)
    scoreKeeper.clear()
    scoreKeeper.write(f"Score: {score}", False, align="Center", font=("Arial", 20, "normal"))
    mo.color("white")
    mo.pencolor("red")
    mo.stamp()
    mo.pencolor("black")
    mo.color("red")
    screenRandom()

# Move turtle to random location on screen.
def screenRandom():
    mo.penup()
    mo.hideturtle()
    wn.bgcolor("red")
    mo.goto(randint(-SCREENX, SCREENX), randint(-SCREENY, SCREENY))
    wn.bgcolor("white")
    mo.showturtle()
    mo.pendown()

def sClicked(x,y):
    global mClicks
    mClicks+=1

# ------ Events ------ #
mo.onclick(moClicked)
wn.onclick(sClicked)

# ------ Main Window Loop ------ #
wn.mainloop()