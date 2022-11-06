#   a115_robot_maze.py
import turtle as t

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)
  
def turn_right():
  robot.speed(0)
  robot.rt(90)
  robot.speed(2)

def moveStraight(i):
    for _ in range(i):
        move()

def moveDag(i):
    for _ in range(i):
        move()
        turn_right()
        move()
        turn_left()

#----- init screen
wn = t.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "./media/Robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = t.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
def startup():
    robot.clear()
    robot.setheading(90)
    robot.goto(startx, starty)
    robot.speed(2)
startup()
robot.turtlesize(turtle_scale, turtle_scale)
robot.showturtle()

#maze 1
wn.bgpic("./media/Maze1.png")

moveDag(4)

#maze 2
wn.bgpic("./media/Maze2.png")
startup()
moveStraight(3)
turn_right()
moveStraight(2)

#maze 3
wn.bgpic("./media/Maze3.png")
startup()
moveDag(2)
robot.pencolor("red")
moveDag(2)

#done
wn.clear()

#---- end robot movement 

wn.mainloop()
