# ------ Dependencies ------ #
import turtle as t
from random import randint
wn = t.Screen()

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
        counter.write("Times up", font=("Arial",15,"normal"))
    else:
        timer-=1
        counter.write(timer, font=("Arial",30,"normal"))
        wn.ontimer(countdown,1000)
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

# ------ Events ------ #
mo.onclick(moClicked)


# ------ Main Window Loop ------ #
wn.mainloop()