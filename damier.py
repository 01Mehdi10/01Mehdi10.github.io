from tkinter import *
from random import randrange

def rang(y,y1,color): # rangées de cases
    c = 0
    x = 10
    x1 = 110
    while c < len(color):
        can.create_rectangle(x,y,x1,y1,fill=color[c])
        x += 100
        x1 += 100
        c += 1
    
def damier():
    c = 1
    y = 10
    y1 = 110
    color1 = ['navy','white','navy','white','navy','white','navy','white','navy','white']
    color2 = ['white','navy','white','navy','white','navy','white','navy','white','navy']
    while c < 11:
        if c % 2 == 0:
            color = color2
        if c % 2 != 0:
            color = color1
        rang(y,y1,color)
        y += 100
        y1 += 100
        c += 1
        
def pion():
    l1 = [15]
    l2 = [15]
    l3 = [105]
    l4 = [105]
    x = 15
    y = 15
    x1 = 105
    y1 = 105
    c = 1
    while c < 10:
        l1.append(x)
        l2.append(y)
        l3.append(x1)
        l4.append(y1)
        x += 100
        y += 100
        x1 += 100
        y1 += 100
        c +=1
    c1 = randrange(10)
    c2 = randrange(10)
    x = l1[c1]
    x1 = l3[c1]
    y = l2[c2]
    y1 = l4[c2]
    can.create_oval(x,y,x1,y1,fill='red')
        
        
##### Programme principal #####
fen = Tk()
can = Canvas(fen, width=1020, height=1020, bg='white')
can.pack(side=TOP, padx=5, pady=5)
b1 = Button(fen, text='Damier',command=damier)
b1.pack(side=LEFT, padx=3, pady=3)
b2 = Button(fen, text='Pions',command=pion)
b2.pack(side=RIGHT, padx=3, pady=3)
fen.mainloop()