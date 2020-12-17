import time
from tkinter import *
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()
ship_image=PhotoImage(file='ship.gif')
s=canvas.create_image(500,0,anchor=NW,image=ship_image)
canvas.create_rectangle(190,480,310,500,fill='black')
canvas.create_rectangle(240,460,260,480,fill='black')
for y in range (200):
    canvas.move(s,-3,0)
    tk.update()
    time.sleep(0.02)
