from os import system
import students

def student_menu():
    system("clear")
    print("\nWelcome to Student Menu")
    while(True):

        print("\n0.exit\n1.Register \n2.Sign In\nnEnter Choice: ")
        ch=int(input())
        if ch==1:
          students.register()
        elif ch==2:
          print("Enter User Name: ")
          uname=input()
          print("Enter password: ")
          passwd=input()
          while(True):

            if(students.validate(uname,passwd)):
                    print("\n0.Log Out\n1.Course List\n2.Center List\n3.Give Preference\n4.check allocated center\n5.update payment detail")
                    print("\nEnter choice: ")
                    choice=int(input())
                    if choice==1:
                         students.courseList()
                    elif choice==2:
                        students.centerList()
                    elif choice==3:
                        students.setPreference()
                    elif choice==4:
                        students.checkAllocatedCenter()
                    elif choice==5:
                        students.updatePaymentDetail()
                    elif choice==0:
                        break;
                    else:
                        print("Enter Correct choice")
                    
        elif ch==0:
            break;
        else:
            print("Invalid Input")
    

def admin_menu():
    system("clear")
    print("Welcome to Admin Menu")

def center_menu():
    system("clear")
    print("Welcome to center Cordinator Menu")
