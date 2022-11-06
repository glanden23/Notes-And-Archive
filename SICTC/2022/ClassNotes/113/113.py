import turtle as t
from random import randint

bob = t.Turtle()
bob.speed(0)
bob.shape("turtle")
poly = 0
while poly!=10000:
    bob.goto(randint(-100, 100), randint(-100, 100))
    poly+=1

window = t.Screen()
window.mainloop()