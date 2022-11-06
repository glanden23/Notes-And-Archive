import turtle as t

horiz=[]
vert=[]

shapes=["arrow","turtle","circle","square","triangle","classic"]
hcolors=["red","blue","green","orange","purple","gold"]
vcolors=["magenta","black","darkred","silver","yellow","lime"]

# Create all turtles
loc=50
for s in shapes:
    # hor
    leonardo = t.Turtle(shape=s)
    leonardo.speed(0)
    horiz.append(leonardo)
    leonardo.penup()
    c = hcolors.pop()
    leonardo.fillcolor(c)
    leonardo.goto(-350,loc)
    leonardo.setheading(0)
    
    #vert
    leonardo = t.Turtle(shape=s)
    leonardo.speed(0)
    vert.append(leonardo)
    leonardo.penup()
    c = vcolors.pop()
    leonardo.fillcolor(c)
    leonardo.goto(-loc,350)
    leonardo.setheading(270)
    loc+=50

bob=t.Turtle()
bob.penup()
bob.goto(-350,350)
bob.pendown()
for i in range(4):
    bob.forward(350)
    bob.right(90)
    
#moving turtles
iterations = 0
while iterations < 50:
    for h in horiz:
        h.forward(10)
    for v in vert:
        v.forward(10)
    iterations+=1
    
    print(abs(h.xcor() - v.xcor()))
    print(abs(h.ycor() - v.ycor()))
    if (abs(h.xcor() - v.xcor()) < 10) or (abs(h.ycor() - v.ycor()) < 10):
        print("Got collide: ",h.xcor(), v.xcor())
        print("Got collide: ",h.ycor(), h.ycor())
        h.fillcolor("white")
        v.fillcolor("white")
        if len(horiz) >= 1:
            horiz.remove(h)
            vert.remove(v)
    

wn = t.Screen()
wn.mainloop()