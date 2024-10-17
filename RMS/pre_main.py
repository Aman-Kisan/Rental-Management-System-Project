# This file is the outdated version of the "main.py" 

import mysql.connector as connector
import os,dotenv
from datetime import datetime

dotenv.load_dotenv()

USER = os.getenv("USER")
PASS = os.getenv("PASS")
DB  = os.getenv("DB")
TABLE = ("electric_slab","rentee_details","rental_payments","electricity_used","electricity_payment")
PRICE_PER_UNIT=int(os.getenv("PRICE_PER_UNIT"))


class InvalidDataTypeException(Exception):

    def __init__(self,expected_data_type):
        self.EDT = expected_data_type

    def __str__(self):
        return(f'{self.EDT} was expected')


class DataTypeChecker:

    def __init__(self,input,ADT):               # Acceptable Data Type abbr. ADT
        self.input = input
        self.acceptable_data_type = ADT
        self. __checker()

    def __checker(self):
        if self.acceptable_data_type == "str" and not self.input.isascii():
            raise InvalidDataTypeException("CHAR")
        elif self.acceptable_data_type == "int" and not self.input.isdecimal():
            raise InvalidDataTypeException("INT")
        elif self.acceptable_data_type == "float" :
            for value in self.input.split('.'):
                if not value.isdecimal():
                    raise InvalidDataTypeException("FLOAT")
        elif self.acceptable_data_type == "date":
            for x in self.input.split('-'):
                if x.isdigit == False:
                     raise InvalidDataTypeException("DATE")

#OPTIONS
#1. New Comers 
def new_comer():
    R_NAME = input("Enter the name of the new Rentee = ")       # rentee_name(RN)
    DataTypeChecker(R_NAME,"str")

    DateShifted = input("Enter the date of shift(dd-mm-yyyy) =")            # shifted_on(DS)
    DataTypeChecker(DateShifted,"date")
    date = DateShifted.split('-')
    x = datetime(int(date[2]),int(date[1]),int(date[0]))
    DateShifted=x.strftime("%Y-%m-%d")

    ADV = input("Given Advance = ")                             # advance_given
    DataTypeChecker(ADV,"str")

    HouseNumber = input("Enter house allocated =")              # house_number(HN)
    DataTypeChecker(HouseNumber,"int")

    with connector.connect(host="localhost",user=USER,password=PASS,database=DB) as myDB:
        push_query = myDB.cursor()
        push_query.callproc(procname=InsertNewRentee,args=(R_NAME,DateShifted,ADV,HouseNumber))         # calling the stored procedure
        myDB.commit()               #  by default Connector/Python does not autocommit
       

#2. data entry to rental_payment
def rent_payment():
    R_NAME = input("Enter Rentee name =")
    DataTypeChecker(R_NAME,"str")
    
    PaymentDate=input("ENter the date of payment(dd-mm-yyyy) >> ")
    DataTypeChecker(PaymentDate,"date")
    date = PaymentDate.split('-')
    x = datetime(int(date[2]),int(date[1]),int(date[0]))
    PaymentDate=x.strftime("%Y-%m-%d")

    print("({})Monthly Rent   ({})Advance Payment\n".format(1,2))
    PaymentType = int(input("Choose from above >>"))
    # DataTypeChecker(PaymentType,"int")
    if PaymentType > 2 or PaymentType < 1:
        raise Exception
    else:
        PaymentType = "Monthly Rent" if PaymentType == 1 else "Advance Payment"
    
    
    with connector.CMySQLConnection(host="localhost",user = USER,password=PASS,database=DB) as myDB:
        push_query = myDB.cursor()
        push_query.callproc(procname='UpdateRentalPayment',args=(R_NAME,PaymentDate,PaymentType))       # calling the stored procedure
        myDB.commit()


#3. data entry to electricity_use_payment
def electric_use():
    R_NAME=input("Enter rentee name >>")
    DataTypeChecker(R_NAME,"str")

    c_unit=input("Enter current unit >>")
    DataTypeChecker(c_unit,'float')

    date_recorded=input('Enter the date unit recorded(dd-mm-yyyy) >>')
    DataTypeChecker(date_recorded,'date')
    date = date_recorded.split('-')
    x = datetime(int(date[2]),int(date[1]),int(date[0]))
    date_recorded=x.strftime("%Y-%m-%d")

    with connector.connect(host="localhost",user = USER,password=PASS,database=DB) as myDB:
        push_query=myDB.cursor()
        push_query.callproc(procname='UpdateElectricityUsed',args=(R_NAME,c_unit,PRICE_PER_UNIT,date_recorded))         # calling the stored procedure
        myDB.commit()


def electric_payment():

    R_NAME = input("ENter rentee name =")
    DataTypeChecker(R_NAME,'str')

    paid_amount = input('Enter paid amount =')
    DataTypeChecker(paid_amount,'int')
    paid_amount = int(paid_amount)

    paid_on = input('Enter the date of payment(dd-mm-yyyy) =')
    DataTypeChecker(paid_on,'date')
    date = paid_on.split('-')
    x = datetime(int(date[2]),int(date[1]),int(date[0]))
    paid_on=x.strftime("%Y-%m-%d")

    with connector.connect(host="localhost",user = USER,password=PASS,database=DB) as myDB:
        push_query = myDB.cursor()
        sql_query1=f'SELECT rentee_id FROM {TABLE[1]} WHERE rentee_name=%s'
        push_query.execute(sql_query1,(R_NAME,))
        result = push_query.fetchmany(size=1)

        if(result != None):
            rentee_id=result[0][0]
            # print(rentee_id)
            sql_query2=f'SELECT E_id,amount FROM {TABLE[3]} WHERE E_id NOT IN(SELECT e_id FROM {TABLE[4]}) AND rentee_id={rentee_id}'     # fetching the unpaid amounts by the rentee
            push_query.execute(sql_query2)
            payment_left=push_query.fetchall()
            try:
                No_of_payment_left = len(payment_left)
            except TypeError:
                No_of_payment_left=0

            sql_query3=f'SELECT unsettled_amount,e_id FROM {TABLE[4]} WHERE e_id IN (SELECT E_id FROM {TABLE[3]} WHERE rentee_id={rentee_id}) ORDER BY payment_id DESC LIMIT 1'              # fetching unsettled amount from the last payment made by the rentee

            sql_query4=f'INSERT INTO {TABLE[4]}(e_id,paid_amount,paid_on,unsettled_amount) VALUES( %s, %s, %s, %s)'

            if No_of_payment_left <= 0:
                if No_of_payment_left < 0:
                    print("-------------------------------------------------")
                    print(" PROBLEM: NUMBER OF PAYMENTS CANNOT BE NEGATIVE")
                    print("-------------------------------------------------")
                else:
                    push_query.execute(sql_query3)
                    result = push_query.fetchone()
                    try:
                        last_unsettled_amount=result[0]
                    except TypeError:
                        last_unsettled_amount=0
                    if last_unsettled_amount > 0:
                        push_query.execute(f'INSERT INTO {TABLE[4]}(e_id,paid_amount,paid_on,unsettled_amount) VALUES(%s,%s,%s,%s)',(result[1],paid_amount,paid_on,last_unsettled_amount-paid_amount))
                        myDB.commit()

            else:   
                # code for clearing the pending electricity use amounts
                for x in range(No_of_payment_left):
                    push_query.execute(sql_query3)
                    last_unsettled_amount = push_query.fetchone()
                    try:
                        last_unsettled_amount=last_unsettled_amount[0]
                    except TypeError:
                        last_unsettled_amount=0
                    current_unsettled_amount = 0

                    if paid_amount > 0:
                        monthly_electric_price = payment_left[x][1] + last_unsettled_amount
                        if paid_amount > monthly_electric_price:
                            if x == No_of_payment_left-1:
                                current_unsettled_amount = monthly_electric_price - paid_amount
                                push_query.execute(sql_query4,(payment_left[x][0],paid_amount,paid_on,current_unsettled_amount))
                                myDB.commit()

                            else:
                                push_query.execute(sql_query4,(payment_left[x][0],monthly_electric_price,paid_on,current_unsettled_amount))
                                myDB.commit()
                            paid_amount = paid_amount - monthly_electric_price

                        else:
                            current_unsettled_amount = monthly_electric_price - paid_amount
                            push_query.execute(sql_query4,(payment_left[x][0],paid_amount,paid_on,current_unsettled_amount))
                            paid_amount = 0
                            myDB.commit()
                    else:
                        break
        