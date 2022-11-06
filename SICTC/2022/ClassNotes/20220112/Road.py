import turtle as t

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
drawer.forward(300)
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
        
wn = t.Screen()
wn.mainloop()