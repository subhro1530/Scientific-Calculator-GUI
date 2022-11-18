from tkinter import *
from PIL import Image,ImageTk
import math

root=Tk()
root.geometry("730x500")
root.minsize(450,600)
root.maxsize(800,600)
root.title("My Calculator")

# Setting the textbox entry
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,padx=10,pady=10,ipadx=2)

# To change the icon feather
# window_icon = ImageTk.PhotoImage(file="calculator.jpg")
# root.iconphoto(True, window_icon)

# Configuring the background as grey
root.configure(background="grey")

# Functions
def click(event):
    global scvalue
    global f
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())     # Eval evaluates  strings and every other stuffs
            except Exception as e:
                value="Err"
                print(e)
                f=1
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        if(f==1):
            scvalue.set("")
        scvalue.set(scvalue.get()+text)
        screen.update()


# For key press
def key_pressed(event):
#    "Key Pressed:"+event.char
    global scvalue
    text=event.char+""
    if text=="=" or text=="\r":     #  Equals or Enter
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())     # Eval evaluates  strings and every other stuffs
            except Exception as e:
                value="Err"
                print(e)
        scvalue.set(value)
        screen.update()
    elif text=="\x08":     #    Backspace
        ntxt = scvalue.get()[0:len(scvalue.get())-1]   
        scvalue.set(ntxt)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root.bind("<Key>",key_pressed)

# Functions for scientific calculator
def btnsin():
    txt = math.sin(math.radians(float(scvalue.get()[0:scvalue.get().index("sin")])))
    scvalue.set(txt)
    screen.update()
def btnasin():
    txt = math.asin(math.radians(float(scvalue.get()[0:scvalue.get().index("asin")])))
    scvalue.set(txt)
    screen.update()
def btncos():
    txt = math.cos(math.radians(float(scvalue.get()[0:scvalue.get().index("cos")])))
    scvalue.set(txt)
    screen.update()
def btnacos():
    txt = math.acos(math.radians(float(scvalue.get()[0:scvalue.get().index("acos")])))
    scvalue.set(txt)
    screen.update()
def btntan():
    txt = math.tan(math.radians(float(scvalue.get()[0:scvalue.get().index("tan")])))
    scvalue.set(txt)
    screen.update()
def btnatan():
    txt = math.atan(math.radians(float(scvalue.get()[0:scvalue.get().index("atan")])))
    scvalue.set(txt)
    screen.update()
def roundfun():
    txt = round(float(scvalue.get()[0:scvalue.get().index("rnd")]),1)
    scvalue.set(txt)
    screen.update()

# Frame 1
f = Frame(root,background="grey")

b=Button(f,text="9",padx=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="C",padx=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="sin",command=btnsin,padx=25,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="asin",command=btnasin,padx=25,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

f.pack()


# Frame 2
f = Frame(root,background="grey")

b=Button(f,text="6",padx=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="cos",command=btncos,padx=22,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="acos",command=btnacos,padx=22,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)


f.pack()


# Frame 3
f = Frame(root,background="grey")

b=Button(f,text="3",padx=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=15,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="tan",command=btntan,padx=25,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="atan",command=btnatan,padx=25,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

f.pack()


# Frame 4
f = Frame(root,background="grey")

b=Button(f,text=".",padx=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="0",padx=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="(",command=btncos,padx=5,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text=")",command=btncos,padx=5,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="%",padx=5,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="rnd",command=roundfun,padx=0,pady=15,font="lucida 25 bold")   
b.pack(side=LEFT,padx=3,pady=2)
b.bind("<Button-1>",click)

f.pack()
    
# Frame 5
f = Frame(root,background="grey")

Button(text="Close",padx=10,font="lucida 15 ",command=root.destroy).pack(pady=10)

f.pack()

root.mainloop()
