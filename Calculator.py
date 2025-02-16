# Calculator by method 1 used pack(side=LEFT) inside frames.


from tkinter import *


def click(event):
     text = event.widget.cget("text")
     print(text)
     if text == "=":
          if scvalue.get().isdigit():
               value = int(scvalue.get())
          else:
               value = eval(screen.get())

          scvalue.set(value)
          screen.update()     
                         

     elif text == "C":
           scvalue.set("")  
           screen.update()  
     
     elif text == "x":
            current_text = scvalue.get()  
            scvalue.set(current_text[:-1])  
            screen.update()    


     else:
          scvalue.set(scvalue.get() + text)
          screen.update()

# Initialise window
ws = Tk()
ws.geometry('525x700')
ws.title('Calculator by Varsha')
ws.config(bg='#cdc0ee')
# ws.resizable(width=False, height=False)


# Initialise screen
scvalue = StringVar()
scvalue.set("")
screen = Entry(ws, textvar = scvalue , font = "lucida 40 bold" ,  bg = "#e6dff6", justify=RIGHT)
screen.pack()


# Frames and buttons layout
f = Frame(ws , bg = "#cdc0ee")

b = Button(f , text = "C", font ="lucida 40 bold" ,  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 2 , pady = 2)
b.bind("<Button-1>",click)

b = Button(f , text = "x", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = "%", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = "/", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)


f.pack(pady = 4)

f = Frame(ws, bg = "#cdc0ee")

b = Button(f , text = "9", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = "8", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = "7", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = "*", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

f.pack(pady = 4)

f = Frame(ws , bg = "#cdc0ee")

b = Button(f , text = "6", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = "5", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = "4", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = "-", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

f.pack(pady = 4)

f = Frame(ws , bg = "#cdc0ee")

b = Button(f , text = "3", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = "2", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = "1", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = "+", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

f.pack(pady = 4)

f = Frame(ws , bg = "#cdc0ee")

b = Button(f , text = "00",font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = "0", font ="lucida 40 bold",  bg = "#e6dff6",width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

b = Button(f , text = ".",  font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)


b = Button(f , text = "=", font ="lucida 40 bold",  bg = "#e6dff6" ,width=2, height=1)
b.pack(side = LEFT , padx = 4 , pady = 4)
b.bind("<Button-1>",click)

f.pack(pady = 4)


ws.mainloop()