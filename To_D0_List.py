from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task!="":
        lb.insert(END,task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def  deleteTask():
    lb.delete(ANCHOR)

ws = Tk()
ws.geometry('800x750+800+600')
ws.title('To Do List')
ws.config(bg='#691883')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=50,
    height=18,
    font=('Times', 18),
    bd=0,
    fg='#691883',
    bg='#f3ccff',
    highlightthickness=0,
    selectbackground='#f3ccff',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'To Do List',
    'Calculator',
    'Password Generator',
    'Rock-Paper-Scissor Game',
    'Contact Book',
    ]

for item in task_list:
    lb.insert(END, item)


sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#e79aff',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#b148d2',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()
