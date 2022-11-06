#import
import turtle as t
import time
import random

#game configuration
delay = 0.1
bodyParts=[]

#create turtle objects

wn = t.Screen()
wn.bgcolor("pink")
wn.setup(width=600,height=600)        #give a default screen size

head = t.Turtle(shape="square")
head.speed(0)
head.penup()
head.direction="stop"

#create food

food=t.Turtle()
food.speed(0)
food.shape("circle")
food.shapesize(.5,.5)
food.color("green")
food.penup()
food.goto(100,100)

#create the food

#function 
def hideTheBody():
    time.sleep(1)
    head.goto(0,0)
    head.direction="stop"
    for i in bodyParts:
        i.hideturtle()
    bodyParts.clear()
def up():
    if head.direction != "down":
        head.direction="up"  
def down():
    if head.direction != "up":
        head.direction="down"   
def left():
    if head.direction!="right":
        head.direction="left"      
def right():
    if head.direction!="left":
        head.direction="right"
def move():
    #depending on the direction, the coordinates change
    if head.direction == "up":
        y = head.ycor()     #get the y coordinate
        head.sety(y+20)     #set the new y coordinate
        
    elif head.direction == "down":
        y = head.ycor()     #get the y coor
        head.sety(y-20)     #set the new y coordinate
    
    elif head.direction == "right":
        x = head.xcor()     #get the x coor
        head.setx(x+20)     #set the new x coordinate
    
    elif head.direction == "left":
        x = head.xcor()     #get the x coor
        head.setx(x-20)     #set the new x coordinate

#events or running code
wn.listen()
wn.onkeypress(up,"w")
wn.onkeypress(right,"d")
wn.onkeypress(left,"a")
wn.onkeypress(down,"s")

#main game loop
while True:
    wn.update()    #updates or refreshes the screen
    
    #Border Collision?
    #turtle.ditance(turtle)----->distance between 2 turtle obj
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        hideTheBody()
    #Food Collision?
    if head.distance(food)<20:
        y=random.randint(-290,290)
        x=random.randint(-290,290)
        food.goto(x,y)
        #add a body part
        for i in range(5):
            part = t.Turtle()
            part.speed(0)
            part.shape("turtle")
            part.color("gray")
            part.penup()
            bodyParts.append(part)
        
    for i in range(len(bodyParts)-1, 0, -1):
        x=bodyParts[i-1].xcor()
        y=bodyParts[i-1].ycor()
        bodyParts[i].goto(x,y)
        
    #move the snake
    
    if len(bodyParts)>0:
        x=head.xcor()
        y=head.ycor()
        bodyParts[0].goto(x,y)
    move()
    
    #Did we hit ourselves?
    
    
    
    time.sleep(delay)