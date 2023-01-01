import sqlite3
import os

confirm = None
reject = None
contact = None
location=["kudal","pawas","banda","ratnairi"]
booking=[]


def admin_login():
    adminId= "admin"
    adminPass= "password"
    print("\nEnter following details to login\n")
    adminName= input("Username: ")
    adminpwd= input("Password: ")
    if (adminId==adminName and adminPass==adminpwd):
        print("logged is as an Admin")
        updatePlace = input("Want to add new place(y/n): ")

        if updatePlace == "y":
            
            num=input("Enter number of location you want to add: ")
            num = int (num)
            for i in range (0,num):
                place=input()
                location.append(place)
            print(location)

        elif updatePlace == "n":
            print ("locations are: ")
            print(location)

        else:
            print("invalid input")

    print("User booking: ")
    print(booking)
    userBookingStatus=input(" \n1. accept\n2. reject\nEnter your responce: ")
    userBooking=int(userBookingStatus)
    if userBooking==1:
        confirm=contact
    elif userBooking==2:
        reject=contact
    
    end = input("Want to logout type y: ")
    if end=="y":
        login()



        



def user_login():        
    if os.path.exists("accounts.db"):
        conn = sqlite3.connect("accounts.db")
        c = conn.cursor()
    else:
        conn = sqlite3.connect("accounts.db")
        c = conn.cursor()

        c.execute('''CREATE TABLE accounts
            (uname text, pwd text)''')

    accOrLog = input("Enter 1 if you wanna add accounts, or 2 if you want to login: ")

    if accOrLog == "1":
        uname = input("Enter account username to add: ")
        pwd = input("Enter account password to add: ")

        c.execute("INSERT INTO accounts VALUES (?, ?)", [uname, pwd])

        conn.commit()
        conn.close()

        print("Account added")

    elif accOrLog == "2":
        uname = input("Enter username: ")
        pwd = input("Enter password: ")

        c.execute("SELECT * FROM accounts WHERE uname=? and pwd=?", [uname, pwd])
        
        if c.fetchone() == None:
            print("Incorrect credentials")

        else:
            print("Logged in!")
            print("select the place of your choice :")
            print('\n'.join(location))
            userPlace=input("\nenter your preferred location: ")
            contact=input("Enter your contact number: ")
            
            status=contact+userPlace
            booking.append(status)
            print(booking)
           
            if (confirm==contact):
                print("\n booking status: success")
            elif (reject==contact):
                print("\n booking status: rejected")
            else:
                print("\n booking status: pending")
        
    

    end = input("Want to logout type y: ")
    if end=="y":
        login()

def login():
    print("Select your account type: \n1.User \n2.Admin")
    choice=input("Enter 1 for User and 2 for Admin: ")
    choice=int(choice)
    if (choice==1):
        user_login()
    elif (choice==2):
        admin_login()
    else:
        print("invalid input")

print("Select your account type: \n1.User \n2.Admin")
choice=input("Enter 1 for User and 2 for Admin: ")
choice=int(choice)
if (choice==1):
    user_login()
elif (choice==2):
    admin_login()
else:
    print("invalid input")