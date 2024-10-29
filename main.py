import RMS
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Rental Management System Project")
root.geometry("480x360")    #height x width
root.configure(bg='lightblue')

root.columnconfigure(0,weight=1)

title = tk.Label(root,text="Rental Management System",bg="lightblue",font=(20))
title.grid(row=0,column=0,sticky="ew",pady=20)


def is_there_empty(args):
    for value in args:
        if len(value.get()) == 0:
            messagebox.showwarning('Empty box',message='No values entered - ALL ENTRIES ARE MANDATORY TO BE FILLED')
            return 0
    return 1

def update_database(args):
    DB_func = args[0]
    DB_msg = DB_func(args[1::])
    update_ack.config(text=DB_msg,fg='red')
    
def confirm_message_box(*args):
    signal = is_there_empty(args[1::])

    if signal:
        root2 = tk.Tk()
        root2.title('Do you confirm ?')
        root2.geometry('250x100')
        root2.config(bg='lightblue')

        root2.columnconfigure(0,weight=1)

        confirm_button = ttk.Button(root2,text='Confirm Update',width=20,command= lambda: update_database(args)).grid(row=0,column=0,padx=10,pady=30)
        # cancel_button = ttk.Button(root2,text='Cancel Update',width=20,command= root2.quit).grid(row=0,column=1,padx=10,pady=30)

def Main_Frame():
    frame1 = tk.Frame(root,bg="lightblue")
    frame1.grid(row=1,column=0,pady=40)
    
    button1 = ttk.Button(frame1,text="Add New Rentee",command=lambda: [Add_New_Rentee(),frame1.destroy(),title.config(text="Add New Rentee",font=(14))],width=20)
    button1.grid(row=1,column=0,padx=30,pady=10)

    button2 = ttk.Button(frame1,text="Rental Payment",command=lambda:[Rental_Payment(),frame1.destroy(),title.config(text="Rental Payment",font=(14))],width=20)
    button2.grid(row=1,column=1,padx=30,pady=10)

    button3 = ttk.Button(frame1,text="Electricity Use",command=lambda:[Electricity_Use(),frame1.destroy(),title.config(text="Electricity Use",font=(14))],width=20)
    button3.grid(row=2,column=0,padx=30,pady=10)

    button4 = ttk.Button(frame1,text="Electricity Payment",command=lambda: [Electricity_Payment(),frame1.destroy(),title.config(text="Electricity Payment",font=(14))],width=20)
    button4.grid(row=2,column=1,padx=30,pady=10)

    button5 = ttk.Button(frame1,text="Exit",command=root.quit,width=20)
    button5.grid(row=4,column=0,columnspan=2,pady=5)

def Add_New_Rentee():

    frame2 = tk.Frame(root,bg="lightblue")
    frame2.grid(row=1,column=0,pady=30)

    rentee_name_label = tk.Label(frame2,text='Rentee Name',bg='lightblue')
    rentee_name_value = ttk.Entry(frame2,width=30)
    rentee_name_label.grid(row=0,column=0,pady=5)
    rentee_name_value.grid(row=0,column=1)
    
    date_shifted_label = tk.Label(frame2,text='Date Shifted',bg='lightblue')
    date_shifted_value = ttk.Entry(frame2,width=30)
    date_shifted_label.grid(row=1,column=0,pady=5)
    date_shifted_value.grid(row=1,column=1)

    advance_payment_value = tk.StringVar()
    advance_payment_label = tk.Label(frame2,text='Advance Payment',bg='lightblue')
    advance_payment_radio1 = ttk.Radiobutton(frame2,variable=advance_payment_value,text='Yes',value='Yes').grid(row=3,column=0,pady=5)
    advance_payment_radio2 = ttk.Radiobutton(frame2,variable=advance_payment_value,text='No',value='No').grid(row=3,column=1,pady=5)
    advance_payment_label.grid(row=2,column=0)

    house_of_choice_value = tk.StringVar()
    house_of_choice_label = tk.Label(frame2,text='House of Choice',bg='lightblue')
    house_of_choice_radio1 = ttk.Radiobutton(frame2,variable=house_of_choice_value,text='North Pole',value='1').grid(row=5,column=0,pady=5)
    house_of_choice_radio2 = ttk.Radiobutton(frame2,variable=house_of_choice_value,text='South Pole',value='2').grid(row=5,column=1,pady=5)
    house_of_choice_label.grid(row=4,column=0)

    back_btn = ttk.Button(frame2,text="Back",command= lambda: [Main_Frame(),frame2.destroy(),title.config(text="Rental Management System",font=(20))],width=20)
    back_btn.grid(row=6,column=0,padx=10,pady=10)

    update_btn = ttk.Button(frame2,text="Update",width=20,command=lambda: confirm_message_box(RMS.new_comer,rentee_name_value,date_shifted_value,advance_payment_value,house_of_choice_value))
    update_btn.grid(row=6,column=1,padx=10,pady=10)

    global update_ack
    update_ack = tk.Label(frame2,text='Designed by Aman Kisan',bg='lightblue')
    update_ack.grid(row=7,column=0,columnspan=2,pady=10)

def Rental_Payment():

    frame3 = tk.Frame(root,bg='lightblue')
    frame3.grid(row=1,column=0,pady=30)

    r_name_lbl = tk.Label(frame3,text='Rentee Name',bg='lightblue')
    r_name_val = ttk.Entry(frame3,width=30)
    r_name_lbl.grid(row=0,column=0,pady=5,padx=10)
    r_name_val.grid(row=0,column=1)

    payment_date_lbl = tk.Label(frame3,text='Payment Date',bg='lightblue')
    payment_date_val = ttk.Entry(frame3,width=30)
    payment_date_lbl.grid(row=1,column=0,pady=5,padx=10)
    payment_date_val.grid(row=1,column=1)

    payment_type_val = tk.StringVar()
    payment_type_lbl = tk.Label(frame3,text='Payment Type',bg='lightblue')
    radio1 = ttk.Radiobutton(frame3,variable=payment_type_val,value='Monthly Payment',text='Monthly').grid(row=3,column=0)
    radio2 = ttk.Radiobutton(frame3,variable=payment_type_val,value='Advance Payment',text='Advance').grid(row=3,column=1)
    payment_type_lbl.grid(row=2,column=0,pady=5)

    back_btn = ttk.Button(frame3,text="Back",command= lambda: [Main_Frame(),frame3.destroy(),title.config(text="Rental Management System",font=(20))],width=20)
    back_btn.grid(row=4,column=0,padx=10,pady=15)

    update_btn = ttk.Button(frame3,text="Update",width=20,command=lambda: confirm_message_box(RMS.rent_payment,r_name_val,payment_date_val,payment_type_val))
    update_btn.grid(row=4,column=1,padx=10,pady=15)

    global update_ack
    update_ack = tk.Label(frame3,text='Designed by Aman Kisan',bg='lightblue')
    update_ack.grid(row=5,column=0,columnspan=2,pady=10)

def Electricity_Use():

    frame4 = tk.Frame(root,bg='lightblue')
    frame4.grid(row=1,column=0,pady=30)

    r_name_lbl = tk.Label(frame4,text='Rentee Name',bg='lightblue')
    r_name_val = ttk.Entry(frame4,width=30)
    r_name_lbl.grid(row=0,column=0,pady=5,padx=10)
    r_name_val.grid(row=0,column=1)

    c_unit_lbl = tk.Label(frame4,text='Current Unit',bg='lightblue')
    c_unit_val = ttk.Entry(frame4,width=30)
    c_unit_lbl.grid(row=1,column=0,pady=5,padx=10)
    c_unit_val.grid(row=1,column=1)

    # Date of observing current unit
    date_rec_lbl = tk.Label(frame4,text='Date of Record',bg='lightblue')
    date_rec_val = ttk.Entry(frame4,width=30)
    date_rec_lbl.grid(row=2,column=0,pady=5,padx=10)
    date_rec_val.grid(row=2,column=1)

    back_btn = ttk.Button(frame4,text="Back",command= lambda: [Main_Frame(),frame4.destroy(),title.config(text="Rental Management System",font=(20))],width=20)
    back_btn.grid(row=3,column=0,padx=10,pady=15)

    update_btn = ttk.Button(frame4,text="Update",width=20,command=lambda: confirm_message_box(RMS.electric_use,r_name_val,c_unit_val,date_rec_val))
    update_btn.grid(row=3,column=1,padx=10,pady=15)

    global update_ack
    update_ack = tk.Label(frame4,text='Designed by Aman Kisan',bg='lightblue')
    update_ack.grid(row=5,column=0,columnspan=2,pady=10)

def Electricity_Payment():
    frame5 = tk.Frame(root,bg='lightblue')
    frame5.grid(row=1,column=0,pady=30)

    r_name_lbl = tk.Label(frame5,text='Rentee Name',bg='lightblue')
    r_name_val = ttk.Entry(frame5,width=30)
    r_name_lbl.grid(row=0,column=0,pady=5,padx=10)
    r_name_val.grid(row=0,column=1)

    amount_paid_lbl = tk.Label(frame5,text='Amount',bg='lightblue')
    amount_paid_val = ttk.Entry(frame5,width=30)
    amount_paid_lbl.grid(row=1,column=0,pady=5,padx=10)
    amount_paid_val.grid(row=1,column=1)

    # Date of observing current unit
    payment_date_lbl = tk.Label(frame5,text='Payment Date',bg='lightblue')
    payment_date_val = ttk.Entry(frame5,width=30)
    payment_date_lbl.grid(row=2,column=0,pady=5,padx=10)
    payment_date_val.grid(row=2,column=1)

    back_btn = ttk.Button(frame5,text="Back",command= lambda: [Main_Frame(),frame5.destroy(),title.config(text="Rental Management System",font=(20))],width=20)
    back_btn.grid(row=3,column=0,padx=10,pady=15)

    update_btn = ttk.Button(frame5,text="Update",width=20,command=lambda: confirm_message_box(RMS.electric_payment,r_name_val,amount_paid_val,payment_date_val))
    update_btn.grid(row=3,column=1,padx=10,pady=15)

    global update_ack
    update_ack = tk.Label(frame5,text='',bg='lightblue')
    update_ack.grid(row=5,column=0,columnspan=2,pady=10)

Main_Frame()

root.mainloop()
