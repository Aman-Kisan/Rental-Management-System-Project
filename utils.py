import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def setBgColor(clr):
    return lambda: clr

matchBgColor = setBgColor("lightpink")

def initiate():
    root = tk.Tk()
    root.title("Rental Management System Project")
    root.geometry("480x360")    #width x height
    root.configure(bg=matchBgColor())

    root.columnconfigure(0,weight=1)

    frame0 = tk.Frame(root,bg=matchBgColor())
    frame0.grid(row=0,column=0,sticky="ew",pady=20)
    title = tk.Label(frame0,text="Rental Management System",bg=matchBgColor(),font=(20))
    title.pack()

    footer_frame = tk.Frame(root,bg=matchBgColor())
    footer_frame.grid(row=2,column=0)
    global update_ack,status_output
    status_output = tk.Label(footer_frame,text="",bg=matchBgColor())
    status_output.pack()
    update_ack = tk.Label(footer_frame,text='Designed by Aman Kisan',bg=matchBgColor())
    update_ack.pack()

    return root,title

def is_There_Empty(args):
    for value in args:
        if len(value.get()) == 0:
            messagebox.showwarning('Empty box',message='No values entered - ALL ENTRIES ARE MANDATORY TO BE FILLED')
            return 0
    return 1

def update_Database(args):
    DB_func = args[0]
    DB_msg = DB_func(args[1::])
    update_ack.config(text=DB_msg,fg='red')
    
def confirm_Message_Box(*args):
    signal = is_There_Empty(tuple(args[1::]))

    if signal:
        root2 = tk.Tk()
        root2.title('Do you confirm ?')
        root2.geometry('250x100')
        root2.config(bg=matchBgColor())

        root2.columnconfigure(0,weight=1)

        confirm_button = ttk.Button(root2,text='Confirm Update',width=20,command= lambda: update_Database(tuple(args)))
        confirm_button.grid(row=0,column=0,padx=10,pady=30)
        # cancel_button = ttk.Button(root2,text='Cancel Update',width=20,command= root2.quit).grid(row=0,column=1,padx=10,pady=30)

def askStatus(*args):
    signal = is_There_Empty(tuple(args[1::]))

    if signal:
        func = args[0]
        value = func(args[1::])
        print(value)
        status_output.config(text=value,fg="green")