from data import *
from Algorithm import *
from studentRegistration import studentRegistration,getEligibility

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
	data = 0
	form_no = int(input("Enter Form Number : "))
	name = input("Enter Name : ")
	for row in student_data:
		if row['form_no'] == str(form_no):
			flag = 1
			data = row
			break

	if flag:
		if data['name'] == name:
			return student_data.index(data)
		else:
			raise Exception("Invalid Name")
	else:
		raise Exception("Invalid Form Number")

def student_menu():
	print("\n\t\tSTUDENT SYSTEM\t\t\n")
	student_data = pull("data-files/students.csv")
	# capacity_data = pull("data-files/capacities.csv")
	eligibility_data = getEligibility()
	form_number = len(student_data)
	form_number +=1
	ch = getChoice()
	while(ch):
		if ch == 1:
			new_student_data = dict()
			newStudent = studentRegistration(form_number,eligibility_data)
			try:
				newStudent.accept()
				new_student_data = newStudent.getRecord()
			except Exception as ex:
				print(ex)
			
			if len(new_student_data)!=0:
				student_data.append(new_student_data)
				form_number+=1
			
		elif ch == 2:
			# Validating Student
			try:
				index = isValid(student_data)
				if index>=0:
					# print(data)
					op = menu()
					while(op):
						if op == 1:
							# THIS OF GETTING LIST OF COURSES
							course_data = pull("data-files/courses.csv")
							courses = eligibility_data.get(student_data[index]['degree'])
							courses = courses[1]
							
							print("================================================")
							print("\t\tAVAILABLE COURSES ACCORDING TO YOUR DEGREE\t\t\n")
							for row in course_data:
								if row['name'] in courses:
									print(f'Course Name : {row["name"]}\nFees : {row["fees"]}\nSection Rank Required : {row["section"]}\n\n')
							print("================================================")


						elif op == 2:
							# THIS IS FOR GETTING LIST OF CENTER
							center_data = pull('data-files/centers.csv')
							print("================================================")
							print("\t\tAVAILABLE CENTERS\t\t\n")
							for row in center_data:
								print(f'Center Name : {row["center_name"]}\nCenter Co-ordinator : {row["coordinator"]}\nAddress : {row["address"]}\n\n')
							print("================================================")


						elif op == 3:
							print("GIVE PREFERENCES")
						elif op == 4:
							# For giving acknowledgement to student about their allocation
							data = student_data[index]

							if int(data['allocated_preference']) <= 0:
								print(f'Sorry {data["name"]}! There is no center allocated to you.')
							else:
								print(f'Hello {data["name"]}, your allocated center is {data["allocated_center_id"]} for {data["allocated_course_name"]}.')
								

						elif op == 5:
							if int(student_data[index]['allocated_preference']) <= 0:
								print(f'Sorry {student_data[index]["name"]}! There is no center allocated to you.')
							else:
								print(f'Hello {student_data[index]["name"]}, your allocated center is {student_data[index]["allocated_center_id"]} for {student_data[index]["allocated_course_name"]}.')
								ip = input("Do you want to make payment?(y/n) : ")
								if ip == 'y':
									student_data[index]['payment'] = '11800'
									print("Payment Successful!!!")
						else:
							print("Invalid input");
						op = menu()

			except Exception as ex:
				print(ex)
		else:
			print("INVALID INPUT")
		ch = getChoice()
	pushF("data-files/students.csv",student_data)

