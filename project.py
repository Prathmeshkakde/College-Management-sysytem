import mysql.connector as mysql
from datetime import date,datetime

db=mysql.connect(host="localhost",user="root",password="",database="college")
command_handler=db.cursor(buffered=True)

def admin_session():
    print("login successfull")
    while 1:
        print("")
        print("admin menu")
        print("1.Register new student")
        print("2.Register new teacher")
        print("3.Delete existing student")
        print("4.Delete existing teacher")
        print("5.Logout")

        user_option=input("option:")
        if user_option=="1":
            print("")
            print("Resgister new student")
            username=input("student username:")
            password=input("student password:")
            query_vals=(username,password)
            command_handler.execute("INSERT INTO users(username,password,privilage) VALUES(%s,%s,'student')",query_vals)
            db.commit()
            print(username +" has been registered as student")

        elif user_option=="2":
            print("")
            print("Resgister new teacher")
            username=input("Teacher username:")
            password=input("Teacher password:")
            query_vals=(username,password)
            command_handler.execute("INSERT INTO users(username,password,privilage) VALUES(%s,%s,'teacher')",query_vals)
            db.commit()
            print(username +" has been registered as teacher")

        elif user_option=="3":
            print("")
            print("Delete existing student acoount")
            username=input("Student username:")
            query_vals=(username,"student")
            command_handler.execute("DELETE FROM users WHERE username=%s AND privilage=%s",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("user not found")
            else:
                print(username + "has been deleted")

        elif user_option=="4":
            print("")
            print("Delete existing teacher acoount")
            username=input("teacher username:")
            query_vals=(username,"teacher")
            command_handler.execute("DELETE FROM users WHERE username=%s AND privilage=%s",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("user not found")
            else:
                print(username + "has been deleted")

        elif user_option=="5":
            break
        else:
            print("no valid option selected")

def auth_admin():
    print("")
    print("admin login")
    print("")
    username=input("username:")
    password=input("password:")
    if username=="admin":
        if password=="password":
            admin_session()
        else:
            print("incorrect password")
    else:
        print("incorrect usename")

class College:
    def main(self):
        today=date.today()
        time_now=datetime.now()
        while 1:
            print("welcome to the college system")
            print("")
            print("Date is:",today)
            print("Time:",time_now)
            print("")
            print("1.Login as student")
            print("2.Login as teacher")
            print("3.login as admin")

            user_option=input("option:")
            if user_option=="1":
                print("student login")
            elif user_option=="2":
                print("teacher login")
            elif user_option=="3":
                auth_admin()
            else:
                print("no valid option selected")

c=College()
c.main()

