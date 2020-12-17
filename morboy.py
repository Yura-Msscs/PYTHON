import time
from tkinter import *
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()
ship_image=PhotoImage(file='ship.gif')
canvas.create_rectangle(190,480,310,500,fill='black')
canvas.create_rectangle(240,460,260,480,fill='black')
shots=0
canvas.create_text(420,100,text="кількість пострілів"+str(shots))
b=0
def ball(event):
    global b,shots
    if shots<10:
        canvas.delete(b)
        b=canvas.create_oval(240,460,260,480,fill='gray')
        canvas.create_text(420,100,text="кількість пострілів"+str(shots),fill='#F0F0ED')
        shots=shots+1
        canvas.create_text(420,100,text="кількість пострілів"+str(shots))
    else:
        canvas.create_text(50,100,text='Ядра закінчились')
canvas.bind_all('<space>',ball)
for z in range(10):
    s=canvas.create_image(500,0,anchor=NW,image=ship_image)
    for y in range (200):
        canvas.move(s,-3,0)
        canvas.move(b,0,-5)
        tk.update()
        time.sleep(0.02)
