import RMS
import tkinter as tk
from tkinter import ttk
from utils import *

root,title = initiate()

def mainFrame():

    root.geometry("480x360")

    frame1 = tk.Frame(root,bg=matchBgColor())
    frame1.grid(row=1,column=0,pady=40)

    button1 = ttk.Button(frame1,text="Rentee Details",command=lambda: [renteeDetailPage(),frame1.destroy(),title.config(text="Rentee Details",font=(14))],width=20)
    button1.grid(row=1,column=0,padx=30,pady=10)

    button2 = ttk.Button(frame1,text="Rental Payment",command=lambda:[rentalPaymentPage(),frame1.destroy(),title.config(text="Rental Payment",font=(14))],width=20)
    button2.grid(row=1,column=1,padx=30,pady=10)

    button3 = ttk.Button(frame1,text="Electricity Use",command=lambda:[electricityUsedPage(),frame1.destroy(),title.config(text="Electricity Use",font=(14))],width=20)
    button3.grid(row=2,column=0,padx=30,pady=10)

    button4 = ttk.Button(frame1,text="Electricity Payment",command=lambda: [electricityPaymentPage(),frame1.destroy(),title.config(text="Electricity Payment",font=(14))],width=20)
    button4.grid(row=2,column=1,padx=30,pady=10)

    button5 = ttk.Button(frame1,text="Status Page",command=lambda:[statusPage(),frame1.destroy(),title.config(text="Stats")],width=20)
    button5.grid(row=4,column=0,columnspan=2,pady=5)

    button6 = ttk.Button(frame1,text="Exit",command=root.quit,width=20)
    button6.grid(row=5,column=0,columnspan=2,pady=5)


def renteeDetailPage():
    frame2 = tk.Frame(root,bg=matchBgColor())
    frame2.grid(row=1,column=0,pady=30)

    button1 = ttk.Button(frame2,text="Add New Rentee",command=lambda:[addingNewRenteePage(),frame2.destroy(),title.config(text="Add New Rentee")],width=20)
    button1.pack(pady=10)

    button2 = ttk.Button(frame2,text="Update Leaving Date",command=lambda:[renteeLeavingDatePage(),frame2.destroy(),title.config(text="Update Leaving Date")])
    button2.pack(pady=10)

    back_btn = ttk.Button(frame2,text="Back",command= lambda: [mainFrame(),frame2.destroy(),title.config(text="Rental Management System",font=(20))],width=20)
    back_btn.pack(pady=10)


def renteeLeavingDatePage():

    frame2 = tk.Frame(root,bg=matchBgColor())
    frame2.grid(row=1,column=0)

    rentee_name_label = tk.Label(frame2,text='Rentee Name',bg=matchBgColor())
    rentee_name_value = ttk.Entry(frame2,width=30)
    # positioning
    rentee_name_label.grid(row=0,column=0,pady=5)
    rentee_name_value.grid(row=0,column=1)
    
    date_of_leaving_label = tk.Label(frame2,text='Date of Leave',bg=matchBgColor())
    date_of_leaving_value = ttk.Entry(frame2,width=30)
    # positioning
    date_of_leaving_label.grid(row=1,column=0,pady=5)
    date_of_leaving_value.grid(row=1,column=1)

    back_btn = ttk.Button(frame2,text="Back",command= lambda: [renteeDetailPage(),frame2.destroy(),title.config(text="Rentee Details",font=(20))],width=20)
    back_btn.grid(row=2,column=0,padx=10,pady=10)

    update_btn = ttk.Button(frame2,text="Update",width=20,command=lambda: confirm_Message_Box(RMS.updateRenteeLeavingDate,rentee_name_value,date_of_leaving_value))
    update_btn.grid(row=2,column=1,padx=10,pady=10)


def addingNewRenteePage():

    frame2 = tk.Frame(root,bg=matchBgColor())
    frame2.grid(row=1,column=0,pady=30)

    rentee_name_label = tk.Label(frame2,text='Rentee Name',bg=matchBgColor())
    rentee_name_value = ttk.Entry(frame2,width=30)
    rentee_name_label.grid(row=0,column=0,pady=5)
    rentee_name_value.grid(row=0,column=1)
    
    date_shifted_label = tk.Label(frame2,text='Date Shifted',bg=matchBgColor())
    date_shifted_value = ttk.Entry(frame2,width=30)
    date_shifted_label.grid(row=1,column=0,pady=5)
    date_shifted_value.grid(row=1,column=1)

    advance_payment_value = tk.StringVar()
    advance_payment_label = tk.Label(frame2,text='Advance Payment',bg=matchBgColor())
    advance_payment_radio1 = ttk.Radiobutton(frame2,variable=advance_payment_value,text='Yes',value='Yes').grid(row=3,column=0,pady=5)
    advance_payment_radio2 = ttk.Radiobutton(frame2,variable=advance_payment_value,text='No',value='No').grid(row=3,column=1,pady=5)
    advance_payment_label.grid(row=2,column=0)

    house_of_choice_value = tk.StringVar()
    house_of_choice_label = tk.Label(frame2,text='House of Choice',bg=matchBgColor())
    house_of_choice_radio1 = ttk.Radiobutton(frame2,variable=house_of_choice_value,text='North Pole',value='1').grid(row=5,column=0,pady=5)
    house_of_choice_radio2 = ttk.Radiobutton(frame2,variable=house_of_choice_value,text='South Pole',value='2').grid(row=5,column=1,pady=5)
    house_of_choice_label.grid(row=4,column=0)

    back_btn = ttk.Button(frame2,text="Back",command= lambda: [renteeDetailPage(),frame2.destroy(),title.config(text="Rentee Details",font=(20))],width=20)
    back_btn.grid(row=6,column=0,padx=10,pady=10)

    update_btn = ttk.Button(frame2,text="Update",width=20,command=lambda: confirm_Message_Box(RMS.new_comer,rentee_name_value,date_shifted_value,advance_payment_value,house_of_choice_value))
    update_btn.grid(row=6,column=1,padx=10,pady=10)

    # global update_ack
    # update_ack = tk.Label(frame2,text='Designed by Aman Kisan',bg=matchBgColor())
    # update_ack.grid(row=7,column=0,columnspan=2,pady=10)

def rentalPaymentPage():

    frame3 = tk.Frame(root,bg=matchBgColor())
    frame3.grid(row=1,column=0,pady=30)

    r_name_lbl = tk.Label(frame3,text='Rentee Name',bg=matchBgColor())
    r_name_val = ttk.Entry(frame3,width=30)
    r_name_lbl.grid(row=0,column=0,pady=5,padx=10)
    r_name_val.grid(row=0,column=1)

    payment_date_lbl = tk.Label(frame3,text='Payment Date',bg=matchBgColor())
    payment_date_val = ttk.Entry(frame3,width=30)
    payment_date_lbl.grid(row=1,column=0,pady=5,padx=10)
    payment_date_val.grid(row=1,column=1)

    payment_type_val = tk.StringVar()
    payment_type_lbl = tk.Label(frame3,text='Payment Type',bg=matchBgColor())
    radio1 = ttk.Radiobutton(frame3,variable=payment_type_val,value='Monthly Payment',text='Monthly').grid(row=3,column=0)
    radio2 = ttk.Radiobutton(frame3,variable=payment_type_val,value='Advance Payment',text='Advance').grid(row=3,column=1)
    payment_type_lbl.grid(row=2,column=0,pady=5)

    back_btn = ttk.Button(frame3,text="Back",command= lambda: [mainFrame(),frame3.destroy(),title.config(text="Rental Management System",font=(20))],width=20)
    back_btn.grid(row=4,column=0,padx=10,pady=15)

    update_btn = ttk.Button(frame3,text="Update",width=20,command=lambda: confirm_Message_Box(RMS.rent_payment,r_name_val,payment_date_val,payment_type_val))
    update_btn.grid(row=4,column=1,padx=10,pady=15)

    # global update_ack
    # update_ack = tk.Label(frame3,text='Designed by Aman Kisan',bg=matchBgColor())
    # update_ack.grid(row=5,column=0,columnspan=2,pady=10)

def electricityUsedPage():

    frame4 = tk.Frame(root,bg=matchBgColor())
    frame4.grid(row=1,column=0,pady=30)

    r_name_lbl = tk.Label(frame4,text='Rentee Name',bg=matchBgColor())
    r_name_val = ttk.Entry(frame4,width=30)
    r_name_lbl.grid(row=0,column=0,pady=5,padx=10)
    r_name_val.grid(row=0,column=1)

    c_unit_lbl = tk.Label(frame4,text='Current Unit',bg=matchBgColor())
    c_unit_val = ttk.Entry(frame4,width=30)
    c_unit_lbl.grid(row=1,column=0,pady=5,padx=10)
    c_unit_val.grid(row=1,column=1)

    # Date of observing current unit
    date_rec_lbl = tk.Label(frame4,text='Date of Record',bg=matchBgColor())
    date_rec_val = ttk.Entry(frame4,width=30)
    date_rec_lbl.grid(row=2,column=0,pady=5,padx=10)
    date_rec_val.grid(row=2,column=1)

    back_btn = ttk.Button(frame4,text="Back",command= lambda: [mainFrame(),frame4.destroy(),title.config(text="Rental Management System",font=(20))],width=20)
    back_btn.grid(row=3,column=0,padx=10,pady=15)

    update_btn = ttk.Button(frame4,text="Update",width=20,command=lambda: confirm_Message_Box(RMS.electric_use,r_name_val,c_unit_val,date_rec_val))
    update_btn.grid(row=3,column=1,padx=10,pady=15)

    # global update_ack
    # update_ack = tk.Label(frame4,text='Designed by Aman Kisan',bg=matchBgColor())
    # update_ack.grid(row=5,column=0,columnspan=2,pady=10)

def electricityPaymentPage():
    frame5 = tk.Frame(root,bg=matchBgColor())
    frame5.grid(row=1,column=0,pady=30)

    r_name_lbl = tk.Label(frame5,text='Rentee Name',bg=matchBgColor())
    r_name_val = ttk.Entry(frame5,width=30)
    r_name_lbl.grid(row=0,column=0,pady=5,padx=10)
    r_name_val.grid(row=0,column=1)

    amount_paid_lbl = tk.Label(frame5,text='Amount',bg=matchBgColor())
    amount_paid_val = ttk.Entry(frame5,width=30)
    amount_paid_lbl.grid(row=1,column=0,pady=5,padx=10)
    amount_paid_val.grid(row=1,column=1)

    # Date of observing current unit
    payment_date_lbl = tk.Label(frame5,text='Payment Date',bg=matchBgColor())
    payment_date_val = ttk.Entry(frame5,width=30)
    payment_date_lbl.grid(row=2,column=0,pady=5,padx=10)
    payment_date_val.grid(row=2,column=1)

    back_btn = ttk.Button(frame5,text="Back",command= lambda: [mainFrame(),frame5.destroy(),title.config(text="Rental Management System",font=(20))],width=20)
    back_btn.grid(row=3,column=0,padx=10,pady=15)

    update_btn = ttk.Button(frame5,text="Update",width=20,command=lambda: confirm_Message_Box(RMS.electric_payment,r_name_val,amount_paid_val,payment_date_val))
    update_btn.grid(row=3,column=1,padx=10,pady=15)

    # global update_ack
    # update_ack = tk.Label(frame5,text='',bg=matchBgColor())
    # update_ack.grid(row=5,column=0,columnspan=2,pady=10)

def statusPage():

    root.geometry("480x500")
    frame1 = tk.Frame(root,bg=matchBgColor())
    frame1.grid(row=1,column=0,pady=40)

    button1 = ttk.Button(frame1,text="Check Advance Booking",command=lambda:[statusInputPage(RMS.stats.func1),frame1.destroy()])
    button1.pack(pady=5)

    button2 = ttk.Button(frame1,text="Check Number of days rentee stayed",command=lambda:[statusInputPage(RMS.stats.func2),frame1.destroy()])
    button2.pack(pady=5)

    button3 = ttk.Button(frame1,text="Check No. of days house was vacant",command=lambda:[statusInputPage(RMS.stats.func3),frame1.destroy()])
    button3.pack(pady=5)    # this actually takes the rentee's name who last stayed in the 
    
    button4 = ttk.Button(frame1,text="Check No. of payments rentee made",command=lambda:[statusInputPage(RMS.stats.func4),frame1.destroy()])
    button4.pack(pady=5)

    button5 = ttk.Button(frame1,text="Check the pending electric used amount",command=lambda:[statusInputPage(RMS.stats.func5),frame1.destroy()])
    button5.pack(pady=5)

    button6 = ttk.Button(frame1,text="Check money to be returned to rentee",command=lambda:[statusInputPage(RMS.stats.func6),frame1.destroy()])
    button6.pack(pady=5)

    back_btn = ttk.Button(frame1,text="Back",command= lambda: [mainFrame(),frame1.destroy(),title.config(text="Rental Management System",font=(20))],width=20)
    back_btn.pack(pady=5)


def statusInputPage(func):

    root.geometry("420x360")

    frame2 = tk.Frame(root,bg=matchBgColor())
    frame2.grid(row=1,column=0,pady=30)

    rentee_name_label = tk.Label(frame2,text='Rentee Name',bg=matchBgColor())
    rentee_name_value = ttk.Entry(frame2,width=30)
    rentee_name_label.grid(row=0,column=0,pady=5)
    rentee_name_value.grid(row=0,column=1)

    back_btn = ttk.Button(frame2,text="Back",command= lambda: [statusPage(),frame2.destroy(),title.config(text="Stats",font=(20))],width=20)
    back_btn.grid(row=1,column=0,padx=5,pady=5)

    check_button = ttk.Button(frame2,text="Check",width=20,command=lambda:askStatus(func,rentee_name_value))
    check_button.grid(row=1,column=1,padx=5,pady=5)


mainFrame()

root.mainloop()