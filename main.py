from student import student_menu
from admin import admin_menu

def getChoice():
	print("==========================================================")
	print("\n\t\tADMISSION SYSTEM\t\t\n")
	print("0. EXIT\n1. STUDENT\n2. ADMIN\n3. CENTER COORDINATOR\n")

	print("==========================================================")

	op = int(input("Enter Your Choice : "))

	return op

def main():
	op = getChoice()

	while(op):
		if op == 1:
			# THIS IS FOR STUDENT
			student_menu()
		elif op == 2:
			# This is for admin
			admin_menu()
		elif op == 3:
			print("CENTER COORDINATOR")
		else:
			print("Invalid Choice")

		op = getChoice()




if __name__ == "__main__":
	main()