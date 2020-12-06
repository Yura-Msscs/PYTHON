from tkinter import *

root=Tk()
root.geometry('440x330')
root.title('Піцерія')

#Labels
Name=Label(root, text='Найменування', font=('Arial',12,'bold'))
Name.place(x=20, y=20)
Price=Label(root, text='Ціна, грн.', font=('Arial',12,'bold'))
Price.place(x=150, y=20)
Num=Label(root, text='Кількість', font=('Arial',12,'bold'))
Num.place(x=230, y=20)
Price=Label(root, text='Вартість, грн.', font=('Arial',12,'bold'))
Price.place(x=310, y=20)
Pizza=Label(root, text='Піца', font=('Arial',12))
Pizza.place(x=25, y=70)
Icecr=Label(root, text='Морозиво', font=('Arial',12))
Icecr.place(x=25, y=120)
Bun=Label(root, text='Тістечко', font=('Arial',12))
Bun.place(x=25, y=170)
Juice=Label(root, text='Сік', font=('Arial',12))
Juice.place(x=25, y=220)


def s1_click(val):
    global y1,y2,y3,y4
    k1=int(val)
    x1=float(P1.get())
    y1=x1*k1
    if y1==int(y1):
        var1.set(int(y1))
    else:
        var1.set(y1)
var1=StringVar()

C1=Label(root, bg='lawn green', text=0, font=('Arial',12), textvariable=var1)
C1.place(x=310, y=70, width=60, height=30)

def s2_click(val1):
    global y1,y2,y3,y4
    k2=int(val1)
    x2=float(P2.get())
    y2=x2*k2
    if y2==int(y2):
        var2.set(int(y2))
    else:
        var2.set(y2)
var2=StringVar()
C2=Label(root, bg='lawn green', text=0, font=('Arial',12),textvariable=var2)
C2.place(x=310, y=120, width=60, height=30)

def s3_click(val2):
    global y1,y2,y3,y4
    k3=int(val2)
    x3=float(P3.get())
    y3=x3*k3
    if y3==int(y3):
        var3.set(int(y3))
    else:
        var3.set(y3)
var3=StringVar()
C3=Label(root, bg='lawn green', text=0, font=('Arial',12),textvariable=var3)
C3.place(x=310, y=170, width=60, height=30)

def s4_click(val3):
    global y1,y2,y3,y4
    k4=int(val3)
    x4=float(P4.get())
    y4=x4*k4
    if y4==int(y4):
        var4.set(int(y4))
    else:
        var4.set(y4)
var4=StringVar()
C4=Label(root, bg='lawn green', text=0, font=('Arial',12),textvariable=var4)
C4.place(x=310, y=220, width=60, height=30)

Lprice=Label(root, text='Вартість замовлення:', font=('Arial',12))
Lprice.place(x=25, y=290)
UAH=Label(root, text='грн.', font=('Arial',12))
UAH.place(x=270, y=290)

#Button
def btn_click():
    global y1,y2,y3,y4
    y=y1+y2+y3+y4
    var5.set(y)
var5=StringVar()
Count=Button(text='Розрахувати', font=('Arial',12),command=btn_click)
Count.place(x=310, y=290)
C5=Label(root, bg='lime green', text=0, font=('Arial',12),textvariable=var5)
C5.place(x=200, y=290, width=60, height=30)

#Entries
P1=Entry(bg='green yellow', justify='center', font='12')
P1.place(x=150, y=70, width=60, height=30)
P1.insert(END, '75')
P2=Entry(bg='green yellow',justify='center', font='12')
P2.place(x=150, y=120, width=60, height=30)
P2.insert(END, '12')
P3=Entry(bg='green yellow',justify='center', font='12')
P3.place(x=150, y=170, width=60, height=30)
P3.insert(END, '16')
P4=Entry(bg='green yellow',justify='center', font='12')
P4.place(x=150, y=220, width=60, height=30)
P4.insert(END, '8')

#Scales
S1=Scale(orient=HORIZONTAL, length=50, from_=0, to=20, command=s1_click)
S1.place(x=230, y=60)
S2=Scale(orient=HORIZONTAL, length=50, from_=0, to=20, command=s2_click)
S2.place(x=230, y=110)
S3=Scale(orient=HORIZONTAL, length=50, from_=0, to=20, command=s3_click)
S3.place(x=230, y=160)
S4=Scale(orient=HORIZONTAL, length=50, from_=0, to=20, command=s4_click)
S4.place(x=230, y=210)
