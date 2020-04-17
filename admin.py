from data import *

# Getting Choice from use
def getChoice():
	print("\n0. EXIT\n1. SIGN IN\n")
	ch = int(input("Enter Your Choice : "))

	return ch

# Getting Menu Choice from user
def getMenuChoice():
	print('''
0. Sign Out
1. List Courses & eligibilities
2. List centers & capacities
3. List students
4. Update student ranks
5. Allocate centers (Round 1)
6. Allocate centers (Round 2)
7. List allocated students
8. List paid students
9. List reported (at center) students
10. Generate PRN
11. List admitted students (with PRN) for given center
		''')

	op = int(input("Enter Your Choice : "))
	return op
# Validating User
def isValid():
	username = input("Enter Username : ")
	password = input("Enter Password : ")

	if username == "admin":
		if password == "admin":
			return True
		else:
			raise Exception("Password is incorrect!")
	else:
		raise Exception("Username is incorrect!")

def admin_menu():
	print("\n\t\tADMIN SYSTEM\t\t\n")
	ch = getChoice()

	while(ch):
		if ch == 1:
			try:
				if isValid():
					op = getMenuChoice()
					course_data = pull("data-files/courses.csv")
					center_data = pull("data-files/centers.csv")
					student_data = pull("data-files/students.csv")
					while op:
						if op == 1:
							print("================================================")
							print("\t\tAVAILABLE COURSES\t\t\n")
							for row in range(1,len(course_data)):
								print(f'Course Name : {course_data[row]["name"]}\nFees : {course_data[row]["fees"]}\nSection Rank Required : {course_data[row]["section"]}\n\n')
							print("================================================")
						elif op == 2:
							center_data.pop(0)
							print("================================================")
							print("\t\tAVAILABLE CENTERS\t\t\n")

							for row in center_data:
								print(f'Center Name : {row["center_name"]}\nCenter Co-ordinator : {row["coordinator"]}\nAddress : {row["address"]}\n\n')
							print("================================================")
						elif op == 3:
							print("List Student")
						elif op == 4:
							print("Update Student Rank")
						elif op == 5:
							print("Allocation of center (Round 1)")
						elif op == 6:
							print("Allocation of center (Round 2)")
						elif op == 7:
							print("List Allocated Student")
						elif op == 8:
							print("List of Paid Student")
						elif op == 9:
							print("List reported (at center) students")
						elif op == 10:
							print("Generate PRN")
						elif op == 11:
							print("List admitted students (with PRN) for given center")
						else:
							print("Invalid Input...")
						op = getMenuChoice()
			except Exception as ex:
				print(ex)
		else:
			print("Invalid Input")

		ch = getChoice()