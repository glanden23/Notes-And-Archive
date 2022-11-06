'''
    Sequences:
        Strings - "concatenated data"
        List - "list of data that can be different types"
        Tuple - immutable or they can change
        Array - immutable or they can change
        *Dictionaries
for i in range(5):
    print("hi")

i = 0
while i <5:
    print("hi")
    i+=1
'''

import turtle as t
from random import randint

shapes=["arrow","turtle","circle","square","triangle","classic"]
colors=["red","blue","green","orange","pale goldenrod","medium violet red", "red"]
myturds = []
i=0
for s in shapes:
    i+=1
    c = colors[i]
    turtle = t.Turtle(shape=s)
    turtle.speed(0)
    turtle.fillcolor(c)
    turtle.pencolor(c)
    turtle.penup()
    myturds.append(turtle)

i=0
for s in shapes:
    i+=1
    c = colors[i]
    turtle = t.Turtle(shape=s)
    turtle.speed(0)
    turtle.fillcolor(c)
    turtle.pencolor(c)
    turtle.penup()
    myturds.append(turtle)
    
i=0
for s in shapes:
    i+=1
    c = colors[i]
    turtle = t.Turtle(shape=s)
    turtle.speed(0)
    turtle.fillcolor(c)
    turtle.pencolor(c)
    turtle.penup()
    myturds.append(turtle)

x,y=0,0
direction=90
for turt in myturds:
    turt.goto(x,y)
    turt.pendown()
    turt.right(direction)
    direction+=45
    turt.forward(50)
    x,y=turt.xcor()+5,turt.ycor()+5

"""for i in range(100):
    for turtle in myturds:
        turtle.shapesize(randint(1, 3))
        turtle.color(colors[randint(0, len(colors)-1)])
        random1 = randint(-400, 400)
        random2 = randint(-400, 400)
        turtle.goto(random1, random2)
        turtle.stamp()"""

wn = t.Screen()
wn.mainloop()