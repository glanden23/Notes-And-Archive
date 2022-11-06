import turtle
from shapes import *
from random import randint
from time import sleep
window = turtle.Screen()
drawPen = turtle.Turtle()
snowPen = turtle.Turtle()
drawPen.speed(0)
drawPen.hideturtle()
snowPen.speed(0)
snowPen.hideturtle()

draw_circle(drawPen, "LightBlue", 0, -300, 300)
draw_triangle(drawPen, "Red", -200, -160, 400)
draw_circle(drawPen, "White", 0, -200, 30)
draw_circle(drawPen, "White", -30, -200, 30)
draw_circle(drawPen, "White", -60, -200, 30)
draw_circle(drawPen, "White", -90, -200, 30)
draw_circle(drawPen, "White", -120, -200, 30)
draw_circle(drawPen, "White", -150, -200, 30)
draw_circle(drawPen, "White", 30, -200, 30)
draw_circle(drawPen, "White", 60, -200, 30)
draw_circle(drawPen, "White", 90, -200, 30)
draw_circle(drawPen, "White", 120, -200, 30)
draw_circle(drawPen, "White", 150, -200, 30)
draw_circle(drawPen, "White", 180, -200, 30)
draw_circle(drawPen, "White", -180, -200, 30)
draw_circle(drawPen, "White", 0, 180, 30)

def snow():
    snowA = 0
    while True:
        snowA+=1
        snowPen.up()
        snowPen.goto(randint(-300, 300),randint(-300, 300))
        snowPen.down()
        snowPen.fillcolor("White")
        snowPen.begin_fill()
        snowPen.circle(5)
        snowPen.end_fill()
        if (snowA > 30):
            sleep(3)
            snowPen.clear()
            snowA = 0
snow()