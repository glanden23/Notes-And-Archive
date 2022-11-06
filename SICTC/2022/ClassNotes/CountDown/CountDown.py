import turtle as t

wn = t.Screen()
counter = t.Turtle()
timer=5
timesUp=False

def countdown():
    counter.clear()
    global timer, timesUp
    if timer <= 0:
        counter.write("Times up", font=("Arial",30,"normal"))
    else:
        timer-=1
        counter.write(timer, font=("Arial",30,"normal"))
        wn.ontimer(countdown,1000)

wn.ontimer(countdown,1000)
wn.mainloop()