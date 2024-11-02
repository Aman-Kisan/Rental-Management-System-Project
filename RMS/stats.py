# This peice of code shows the stats about the data in DB

''' WHAT KIND OF STATS WE CAN DISPLAY OR FIND OUT FROM THE EXISTING rental_management_system database

        Rentee_Details
    - To know if the rentee has advance booking/payment for the house -
    - To know for how many days the house was not on rent -
    - For how many days/months/years did the rentee stayed for in a house - 
    
        Rental_Payments
    - To get the number of payments made by the rentee -

        Electricity_Used
    - To know how much unit, actual price and price after cut-off did it cost in that month -

        Electricity_Payment
    - To know how much money do we owe to the rentee -'''

import mysql.connector as connector
import os,dotenv
from .main import DataTypeChecker,InvalidDataTypeException
import mysql.connector.errors as MysqlErrors
from datetime import datetime


if __name__!= "__main__":

    timestamp = lambda:f"[{datetime.now()}] :"

    def ConnectToDatabase(func):
        def ConnectToDatabaseWrapper(argms):
            with connector.connect(host="localhost",user=USER,password=PASS,database=DB) as myDB:
                try:
                    SQL_cursor = myDB.cursor()
                    result = func(argms,SQL_cursor)
                except (MysqlErrors.DatabaseError,TypeError) as DBerror:
                    print(f"[{datetime.now()}]: Database Error Occurred")
                    print(f"Message : {DBerror}")
                    return 'Failed To Check'
                return result
                # myDB.commit()
        return ConnectToDatabaseWrapper

    # Stats from rentee_details table

    # To know if the rentee has advance booking/payment for the house
    @ConnectToDatabase
    def func1(argms,SQL_cursor):
        rentee_name = argms[0].get()
        try:
            DataTypeChecker(rentee_name,"str")
        except (AttributeError,InvalidDataTypeException) as e:
            print(f"{timestamp()} Invalid data input AS",e)

        query = f"SELECT advance_given FROM {TABLE[1]} WHERE rentee_name=%s"
        SQL_cursor.execute(query,(rentee_name,))
        record = SQL_cursor.fetchone()
        if record[0] == "YES":
            return f"{record[0]} advance payment given"
        else:
            return f"{record[0]} advance payment not given"


    # For how many days/months/years did the rentee stayed for in a house
    @ConnectToDatabase
    def func2(argms,SQL_cursor):
        rentee_name = argms[0].get()
        try:
            DataTypeChecker(rentee_name,"str")
        except (AttributeError,InvalidDataTypeException) as e:
            print(f"{timestamp()} Invalid data input AS",e)

        SQL_cursor.callproc(procname='NoOfMonthsStayed',args=(rentee_name,0 ))
        for record in SQL_cursor.stored_results():      #stored_results is a genereator object that returns an MySQLBufferedCursor object which then returns an iterator through fetchone() that has the stored procedure's output
            record = record.fetchone()
            break
        if record[0] < 1 :
             print(f"{timestamp()} {rentee_name} stayed = {record[1]} days")
             return(f"{rentee_name} stayed {record[1]} days")
        elif record[0] > 12 :
            print(f"{timestamp()} {rentee_name} stayed = {record[0]/12} year {record[0]%12} months")
            return(f"{rentee_name} stayed {record[0]/12} year {record[0]%12} months")
        else:
             print(f"{timestamp()} {rentee_name} stayed = {record[0]} months")
             return(f"{rentee_name} stayed {record[0]} months")
         #showing the result

    #To know for how many days the house was not on rent
    @ConnectToDatabase
    def func3(argms,SQL_cursor):
        rentee_name = argms[0].get()
        try:
            DataTypeChecker(rentee_name,"str")
        except (AttributeError,InvalidDataTypeException) as e:
            print(f"{timestamp()} Invalid data input AS",e)

        query = f"SELECT house_no,Not_On_Rent FROM house_not_on_rent_status WHERE r1_rentee_name = \"{rentee_name}\""
        SQL_cursor.execute(query)
        record = SQL_cursor.fetchone()
        print(f"{timestamp()} Number of days house {record[0]} remained vacant after {rentee_name} left = {record[1]}")  #showing result
        return(f"House {record[0]} remained vacant for {record[1]} days after {rentee_name} left ")  #showing result

    # Stats from rental_payments table

    #To get the number of payments made by the rentee
    @ConnectToDatabase
    def func4(argms,SQL_cursor):
        rentee_name = argms[0].get()
        try:
            DataTypeChecker(rentee_name,"str")
        except (AttributeError,InvalidDataTypeException) as e:
            print(f"{timestamp()} Invalid data input AS",e)
        
        query = f"SELECT COUNT(payment_id) FROM rental_payments WHERE rentee_id=FetchRenteeID(\"{rentee_name}\")"
        SQL_cursor.execute(query)
        record = SQL_cursor.fetchone()
        # print(f"No. of payments made by {rentee_name}:{record[0]}") 
        return(f"No. of payments made by {rentee_name} : {record[0]}") 
        #showing results

    #Stats from electricity_used table
        
    #To know how much unit, actual price and price after cut-off did it cost in that month
    @ConnectToDatabase
    def func5(argms,SQL_cursor):        
        rentee_name = argms[0].get()
        try:
            DataTypeChecker(rentee_name,"str")
        except (AttributeError,InvalidDataTypeException) as e:
            print(f"{timestamp()} Invalid data input AS",e)

        SQL_cursor.callproc(procname='FetchElectricityUseAmount',args=(rentee_name,0,0,0,0,0))
        for record in SQL_cursor.stored_results():
            record = record.fetchone()
            break

        # print(record)       #(p_unit,c_unit,no_of_months,u_amount,actual_amount,final_amount)
        return f"Your electricity use status :\nprevious unit : {record[0]}\ncurrent unit : {record[1]}\npending months : {record[2]}\nactual amount : {record[4]}\namount after cut-off : {record[5]}"


    #Electricity_Payment
    # To know how much money do we owe to the rentee
    @ConnectToDatabase
    def func6(argms,SQL_cursor):
        rentee_name = argms[0].get()
        try:
            DataTypeChecker(rentee_name,"str")
        except (AttributeError,InvalidDataTypeException) as e:
            print(f"{timestamp()} Invalid data input AS",e)

        query = f"SELECT sum(paid_amount)-sum(instant_amount) FROM electricity_uses_and_payments WHERE rentee_id=FetchRenteeID(\"{rentee_name}\") and paid_amount != \"Null\""

        SQL_cursor.execute(query)
        record = SQL_cursor.fetchone()
        # print(record)       #showing the results
        if record[0] > 0:
            return f"{rentee_name} will recieve Rs.{record[0]}"
        elif record[0] < 0:
            return f"{rentee_name} will give Rs.{(-1)*record[0]}"
        else:
            return "Its even"

    dotenv.load_dotenv()

    USER = os.getenv("USER")
    PASS = os.getenv("PASS")
    DB  = os.getenv("DB")
    TABLE = ("electric_slab","rentee_details","rental_payments","electricity_used","electricity_payment")
    # VIEW = ("house_not_on_rent_status")
