## Requirements

First install MySQL into your device from the [official MySQL page](https://dev.mysql.com/downloads/installer/) and download all the neccessary applicaton from it.

## How to use the MySQL scripts to create the tables,functions and procedure ?

### Using Workbench
- Just open the SQL script files in MySQL Workbench and RUN it.

### Using MySQL command line client
- Type the following lines step by step

1. Open MySQL in your CMD by typing the following and then enter your password set for the root user. <br>

   ```
    mysql -u root -p
   ```
   
<!--![](https://github.com/Aman-Kisan/Rental-Management-System-Project/blob/main/DB/MySQL%20scripts/pic1.jpg)-->

2.  Do this for all the above files to create the Tables, Functions, Procedures and Views<br>

    ```
    source DB\MySQLScripts\Tables.sql
    ```
<!--![](https://github.com/Aman-Kisan/Rental-Management-System-Project/blob/main/DB/MySQL%20scripts/pic2.jpg)-->

## How to insert data into tables ?

- [Check out](https://www.mysqltutorial.org/mysql-basics/import-csv-file-mysql-table/#:~:text=Importing%20a%20CSV%20file%20on%20the%20MySQL%20server%20into%20a%20table%20using%20LOAD%20DATA%20INFILE%20statement) this page and see how to insert records from csv files into tables in MySQL ?

