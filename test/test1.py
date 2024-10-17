import mysql.connector as connector
import os,dotenv
from datetime import datetime


dotenv.load_dotenv()

USER = os.getenv("USER")
PASS = os.getenv("PASS")
DB  = 'rental_management_system'

class InvalidDataTypeException(Exception):

    def __init__(self,expected_data_type):
        self.EDT = expected_data_type

    def __str__(self):
        return(f'{self.EDT} was expected')


class DataTypeChecker:

    def __init__(self,input,ADT):
        self.input = input
        self.acceptable_data_type = ADT
        self. __checker()

    def __checker(self):
        if self.acceptable_data_type == "str" and not self.input.isascii():
            raise InvalidDataTypeException("CHAR")
        elif self.acceptable_data_type == "int" and not self.input.isdigit():
            raise InvalidDataTypeException("INT")
        elif self.acceptable_data_type == "float" and not self.input.isdecimal():
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
        push_query.execute("INSERT INTO rentee_details(rentee_name,shifted_on,advance_given,house_no) VALUES(%s,%s,%s,%s)",(R_NAME,DateShifted,ADV,HouseNumber))
        myDB.commit()               #  by default Connector/Python does not autocommit
       
# new_comer()

#2. data enntry to rental_payment
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
        push_query.execute(f"SELECT rentee_id FROM rentee_detail WHERE rentee_name= %s",(R_NAME,))
        my_result=push_query.fetchone()
        if my_result != None:
            rentee_id = my_result[0]
            data = (9,rentee_id,PaymentDate,PaymentType)
            push_query.execute("INSERT INTO rental_payment(payment_id,rentee_id,paid_on,payment_type) VALUES(%s,%s,%s,%s)",data)
            myDB.commit()

# rent_payment()

conn = connector.connect(host="localhost",user = 'root',password=PASS,database=DB)

my_cursor = conn.cursor()
my_cursor.execute('SELECT * FROM electricity_used')
result = my_cursor.fetchall()
print(result)
