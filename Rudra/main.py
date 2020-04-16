import sys
import Menu.menu as m


while(1):

    print("************** MAIN MENU***********\n")
    print("\n0.Exit\n1.Student\n2.Admin\n3.Center Coordinator\nEnter Choice: ")
    ch=int(input())
    if ch==1:
        m.student_menu()
    elif ch==2:
        m.admin_menu()
    elif ch==3:
        m.center_menu()
    elif ch==0:
        sys.exit()
    else:
        print("Enter Valid choice\n\n")
