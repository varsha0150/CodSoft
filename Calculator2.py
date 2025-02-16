# Calculator by method 2 uses grid(row, column) to arrange buttons in a structured table which 
# aligns buttons evenly and simplifies the structure efficiently.


from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(scvalue.get())
            scvalue.set(value)
        except Exception as e:
            scvalue.set("Error")
    elif text == "C":
        scvalue.set("")
    elif text == "x":
        scvalue.set(scvalue.get()[:-1])
    else:
        scvalue.set(scvalue.get() + text)
    
    screen.update()

# Initialize Window
ws = Tk()
ws.geometry('425x600')
ws.title('Calculator by Varsha')
ws.config(bg='#cdc0ee')
ws.resizable(width=False, height=False)

scvalue = StringVar()
scvalue.set("")
screen = Entry(ws, textvar=scvalue, font="lucida 20 bold", bg="#e6dff6", justify=RIGHT)
screen.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)

# Button Layout
buttons = [
    ["C", "x", "%", "/"],
    ["9", "8", "7", "*"],
    ["6", "5", "4", "-"],
    ["3", "2", "1", "+"],
    ["00", "0", ".", "="]
]

# Create buttons with grid layout
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        btn = Button(ws, text=btn_text, font="lucida 20 bold", width=5, height=2, bg="#e6dff6")
        btn.grid(row=i+1, column=j, padx=5, pady=5)
        btn.bind("<Button-1>", click)

ws.mainloop()