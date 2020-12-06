from tkinter import *
import math

def BC_click():
    ent.delete(0,END)
def Equal_click():
    global a,b
    c=float(ent.get())
    ent.delete(0,END)
    if b=='+':
        a=a+c
        if a==int(a):
            ent.insert(END,int(a))
        else:
            ent.insert(END,a)
    if b=='-':
        a=a-c
        if a==int(a):
            ent.insert(END,int(a))
        else:
            ent.insert(END,a)
    if b=='*':
        a=a*c
        if a==int(a):
            ent.insert(END,int(a))
        else:
            ent.insert(END,a) 
    if b=='/':
        if c!=0:
            a=a/c
            if a==int(a):
                ent.insert(END,int(a))
            else:
                ent.insert(END,a)
        else:
            ent.insert(END,'помилка') 
            
    
def B7_click():
    ent.insert(END,'7')
def B8_click():
    ent.insert(END,'8')
def B9_click():
    ent.insert(END,'9')
def B4_click():
    ent.insert(END,'4')
def B5_click():
    ent.insert(END,'5')
def B6_click():
    ent.insert(END,'6')
def B1_click():
    ent.insert(END,'1')
def B2_click():
    ent.insert(END,'2')
def B3_click():
    ent.insert(END,'3')
def B0_click():
    ent.insert(END,'0')
def Plus_click():
    global a,b
    a=float(ent.get())
    b='+'
    ent.delete(0,END)
def Minus_click():
    global a,b
    a=float(ent.get())
    b='-'
    ent.delete(0,END)
def Mult_click():
    global a,b
    a=float(ent.get())
    b='*'
    ent.delete(0,END)
def Divide_click():
    global a,b
    a=float(ent.get())
    b='/'
    ent.delete(0,END)
def point_click():
    ent.insert(END, ".")
def Radical_click():
    a=float(ent.get())
    ent.delete(0,END)
    if a>=0:
        a=math.sqrt(a)
        if a==int(a):
            ent.insert(END,int(a))
        else:
            ent.insert(END,a)
    else:
        ent.insert(END,'помилка')
def Modul_click():
    a=float(ent.get())
    ent.delete(0,END)
    a=abs(a)
    if a==int(a):
        ent.insert(END,int(a))
    else:
        ent.insert(END,a)

root=Tk()
root.title('Ю. В. Боднар')
root.geometry('260x370')

ent=Entry(justify='right', font='14')
ent.place(x=20, y=20, width=220, height=30)

BC=Button(text='C', font='14',command=BC_click)
BC.place(x=20, y=70, width=40, height=40)
Equal=Button(text='=', font='14',command=Equal_click)
Equal.place(x=200, y=70, width=40, height=40)
Radical=Button(text='√', font='14', command=Radical_click)
Radical.place(x=80, y=70, width=40, height=40)
Modul=Button(text='|x|', font='14',command=Modul_click)
Modul.place(x=140, y=70, width=40, height=40)
B7=Button(text='7', font='14',command=B7_click)
B7.place(x=20, y=130, width=40, height=40)
B8=Button(text='8', font='14',command=B8_click)
B8.place(x=80, y=130, width=40, height=40)
B9=Button(text='9', font='14',command=B9_click)
B9.place(x=140, y=130, width=40, height=40)
B4=Button(text='4', font='14',command=B4_click)
B4.place(x=20, y=190, width=40, height=40)
B5=Button(text='5', font='14',command=B5_click)
B5.place(x=80, y=190, width=40, height=40)
B6=Button(text='6', font='14',command=B6_click)
B6.place(x=140, y=190, width=40, height=40)
B1=Button(text='1', font='14',command=B1_click)
B1.place(x=20, y=250, width=40, height=40)
B2=Button(text='2', font='14',command=B2_click)
B2.place(x=80, y=250, width=40, height=40)
B3=Button(text='3', font='14',command=B3_click)
B3.place(x=140, y=250, width=40, height=40)
B0=Button(text='0', font='14',command=B0_click)
B0.place(x=20, y=310, width=100, height=40)
Point=Button(text='.', font='14',command=point_click)
Point.place(x=140, y=310, width=40, height=40)
Plus=Button(text='+', font='14',command=Plus_click)
Plus.place(x=200, y=130, width=40, height=40)
Minus=Button(text='-', font='14',command=Minus_click)
Minus.place(x=200, y=190, width=40, height=40)
Mult=Button(text='*', font='14',command=Mult_click)
Mult.place(x=200, y=250, width=40, height=40)
Divide=Button(text='/', font='14',command=Divide_click)
Divide.place(x=200, y=310, width=40, height=40)
