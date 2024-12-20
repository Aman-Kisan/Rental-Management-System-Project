
# Rental Management System Project
It is a GUI based application build using Python and MySQL RDBMS for household rental and electricity usage management.

## Contents
- [Steps to follow](#Steps-to-follow)
- [Preview](#Preview)
- [How this project helped me ?](#how-this-project-helped-me-)

## Steps to follow

- Install MySQL in your system then, follow the steps given in **'DB/Scripts/README.md'** to upload the tables and their records(if required), views, stored procedures and functions.
- Second, install the required modules from the requirements file in your python virtual environment.
- Then, RUN the **'main.py'** file.


## Preview

The app provides an interface to manage a database that stores the rentee's details, their monthly rental payments, their monthly electricity usage and its payments.

The database used in here is MySQL. The app doesn't provide you the remote access to your database for storing information, rather it requires to have the database in your device.

### Home Page 
![](https://github.com/Aman-Kisan/Rental-Management-System-Project/blob/main/screenshots/home_page.jpg)

The home page contains four buttons for adding details of new rentee, details of monthly rental payment for each rentee, details of electricity usage for each month and its payments.

### Add Rentee Page

![](https://github.com/Aman-Kisan/Rental-Management-System-Project/blob/main/screenshots/add_rentee_page.jpg)

This allows the user to add details (like:- Name,date they shifted etc) about the rentee.

The radiobutton <strong>North Pole</strong> sets the house number as 1 and <strong>South Pole</strong> sets 2.

### Rental Payment Page

![](https://github.com/Aman-Kisan/Rental-Management-System-Project/blob/main/screenshots/rental_payment_page.jpg)

This allows the user to make entry for the monthly payment received from the rentee.

The radiobutton <strong>Monthly</strong> is to be selected when payment made is a monthly payment and <strong>Advance</strong> is selected when payment made is an advance given by the rentee for reseving the house.

### Electricity Usage Page

![](https://github.com/Aman-Kisan/Rental-Management-System-Project/blob/main/screenshots/electricity_use_page.jpg)

This page is for to make entry for the electricity units that is recorded every end of the month from the houses.

### Electricity Payment Page

![](https://github.com/Aman-Kisan/Rental-Management-System-Project/blob/main/screenshots/electricity_payment_page.jpg)

This page is for to make entry for the payment made by the rentee for their electricity usage.

## How this project helped me ?

- I needed a simple way to manage our house renting system i.e recording every collection made by me from the rentees for monthly rental amount or their monthly eletric usage. So, doing this using a database was more comfortable rather doing it on a notebook.
- The development of the entire database in MySQL and the Python codes for the GUI and for connecting to SQL database, helped me have good grasp on MySQL, Python and its packages.
- This project truely has used the basic concepts of MySQL and Python(obviously some advance concept of Python has been used but I don't think they are advance anymore). Only a good understanding over the basics can help understand the codes.
- I did this project totally on an experimental mind to explore as much as possible, understanding the basics.
