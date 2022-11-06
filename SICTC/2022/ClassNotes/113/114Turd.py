import turtle as t

donny = t.Turtle()
donny.shape("circle")
donny.speed(0)
wn = t.Screen()
donny.shapesize(3)
donny.up()

sX=float(wn.window_width())/2
sY=float(wn.window_height())/2
cx=-sX
cy=-sY
donny.color("purple")
while(cy<sY):
    x=float(wn.window_width())/2
    y=float(wn.window_height())/2
    if (sX != x or sY != y):
        t.clearscreen()
        cx=-x
        cy=-y
        sX=x
        sY=y
    donny.goto(cx,cy)
    donny.stamp()
    if (cx>x):
        cx=-x
        cy+=20
        donny.color("purple")
        donny.goto(cx,cy)
        donny.stamp()
    cx+=50
    donny.color("orange")

wn.mainloop()