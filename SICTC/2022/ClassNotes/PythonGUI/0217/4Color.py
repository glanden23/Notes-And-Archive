from tkinter import *

root = Tk()
root.title("4 colors | Tkinter")

color1 = Frame(root)
color1.config(background="blue", width=150, height=150)
color1.grid(row=0,column=0,sticky='news')

color2 = Frame(root)
color2.config(background="green", width=100, height=150)
color2.grid(row=0,column=1,sticky='news')

color3 = Frame(root)
color3.config(background="red", width=150, height=150)
color3.grid(row=1,column=0,sticky='news')

color4 = Frame(root)
color4.config(background="yellow", width=100, height=150)
color4.grid(row=1,column=1,sticky='news')

root.mainloop()