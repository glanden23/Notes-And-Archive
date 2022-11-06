from random import randint
import turtle as t
wn = t.Screen()

def checkCollide():
    for m in turtles:
        for i in turtles:
            if (i != m):
                if (abs(m.xcor() - i.xcor()) < 15) and (abs(m.ycor() - i.ycor()) < 15):
                    m.hideturtle()
                    i.hideturtle()
                    try:
                        turtles.remove(i)
                        turtles.remove(m)
                    except ValueError:
                        print("Couldn't remove value.")
                    if len(turtles) == 0:
                        exit()

line = t.Turtle()
line.speed(0)
line.penup()
line.goto(-300, 300)
line.pendown()
for i in range(4):
    line.forward(600)
    line.right(90)
    line.hideturtle()

turtles = []
for i in range(1000):
    turtle = t.Turtle(shape="circle")
    turtle.speed(0)
    turtle.color("red")
    turtle.penup()
    turtle.goto(randint(-300, 300), randint(-300, 300))
    turtles.append(turtle)

for i in range(10000):
    i = turtles[randint(0, len(turtles)-1)]
    for _ in range(randint(1, 5)):
        i.setheading(randint(0, 360))
        for _ in range(5):
            i.forward(15)
            checkCollide()
        if (i.xcor() > 300):
            i.goto(-300,i.ycor())
        elif(i.xcor() < -300):
            i.goto(300,i.ycor())
        elif (i.ycor() < -300):
            i.goto(i.xcor(),300)
        elif (i.ycor() > 300):
            i.goto(i.xcor(),-300)
            
    
wn.mainloop()