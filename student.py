from data import *

def menu():
	print("\n0. SIGN OUT\n1. LIST COURSES\n2. LIST CENTERS\n3. GIVE PREFERENCES\n4. SEE ALLOCATED CENTER COURSES\n5. UPDATE PAYMENT DETAILS")
	op = int(input("Enter your choice : "))
	return op


def getChoice():
	print("\n0. EXIT\n1. REGISTER STUDENT\n2. SIGN IN")

	ch = int(input("ENTER YOUR CHOICE : "))
	return ch


# Validating Student

def isValid(student_data):
	flag = 0
	data = {}
	form_no = int(input("Enter Form Number : "))
	name = input("Enter Name : ")
	for row in range(1,len(student_data)):
		if student_data[row]['form_no'] == str(form_no):
			flag = 1
			data = student_data[row]
			break

	if flag:
		if data['name'] == name:
			return data
		else:
			raise Exception("Invalid Name")
	else:
		raise Exception("Invalid Form Number")

def student_menu():
	print("\n\t\tSTUDENT SYSTEM\t\t\n")
	student_data = pull("data-files/students.csv")
	ch = getChoice()
	while(ch):
		if ch == 1:
			print("Register Student")
		elif ch == 2:
			# Validating Student
			try:
				data = isValid(student_data)
				if len(data)!=0:
					# print(data)
					op = menu()
					while(op):
						if op == 1:
							# THIS OF GETTING LIST OF COURSES
							course_data = pull("data-files/courses.csv")

							print("================================================")
							print("\t\tAVAILABLE COURSES\t\t\n")
							for row in range(1,len(course_data)):
								print(f'Course Name : {course_data[row]["name"]}\nFees : {course_data[row]["fees"]}\nSection Rank Required : {course_data[row]["section"]}\n\n')
							print("================================================")
						elif op == 2:
							# THIS IS FOR GETTING LIST OF CENTER
							center_data = pull('data-files/centers.csv')
							center_data.pop(0)
							print("================================================")
							print("\t\tAVAILABLE CENTERS\t\t\n")

							for row in center_data:
								print(f'Center Name : {row["center_name"]}\nCenter Co-ordinator : {row["coordinator"]}\nAddress : {row["address"]}\n\n')
							print("================================================")
						elif op == 3:
							print("GIVE PREFERENCES")
						elif op == 4:
							print("SEE ALLOCATED COURSES/CENTERS")
						elif op == 5:
							print("UPDATE PAYMENT DETAILS")
							print(data)
						else:
							print("Invalid input");
						op = menu()

			except Exception as ex:
				print(ex)
		else:
			print("INVALID INPUT")
		ch = getChoice()

