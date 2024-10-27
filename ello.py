from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="122826", database="python")


def insert(name, dept):
    tab = con.cursor()
    sql = "insert into student (Name,Dept) values (%s,%s)"
    hello = (name, dept)
    tab.execute(sql, hello)
    con.commit()
    print("Data inserted successfully")


def update(name,dept):
    tab = con.cursor()
    sql = "update student set Dept=%s where name=%s"
    hello = (dept,name)
    tab.execute(sql, hello)
    con.commit()
    print("Data updated successfully")


def select():
    tab = con.cursor()
    sql = "select name,dept from student"
    tab.execute(sql)
    result = tab.fetchall()
    print(tabulate(result, headers=["NAME", "DEPT"]))


def delete(name):
    tab = con.cursor()
    sql = "Delete from student where name=%s"
    hello = (name,)
    tab.execute(sql,hello)
    con.commit()
    print("Data deleted successfully")

while True:
    choice=input("If you want to continue the process : ")

    if choice == "yes" or choice == "y":
        print("Please select the below options to proceed : ")
        print("1.Insert Data")
        print("2.Update Data")
        print("3.Select Data")
        print("4.Delete Data")
        print("5.Exit")
        option = int(input("select a option : "))
        if option == 1:
            name = input("Enter the Name : ")
            dept = input("Enter the dept : ")
            insert(name, dept)
        elif option == 2:
            name = input("Enter the Name : ")
            dept = input("Enter the dept : ")
            update(name,dept)
        elif option == 3:
            select()
        elif option == 4:
            name = input("Enter the Name : ")
            delete(name)
        elif option == 5:
            quit()
        else:
            print("Invalid option")
    else:
        print("Exited")
        quit()


