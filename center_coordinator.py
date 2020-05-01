from data import *

def isValid(center_data):
	center_id = input("Enter Center Id : ")
	password = input("Enter Password : ")
	flag = 0
	data = {}
	for row in center_data:
		if row['center_id'] == center_id:
			flag = 1
			data = row
			break

	if flag:
		if data['password'] == password:
			return center_data.index(data)
		else:
			raise Exception("Invalid Password!")
	else:
		raise Exception("Invalid Center Id!")


# MAIN MENU OPTION
def get_center_menu_option():
	print("\n=============================================")
	print("CENTER CO-ORDINATOR SYSTEM\n".center(40,' '))

	print("0.EXIT\n1.SIGN IN\n")
	ch = int(input("Enter Your Choice : "))

	return ch

def getMenuOption():
	print("\n=============================================")
	
	print("\n0. SIGN OUT\n1. LIST COURSES\n2. LIST OF STUDENTS\n3. UPDATE REPORTED STUDENTS\n4. LIST OF ADMITTED STUDENTS\n")
	op = int(input("Enter your option : "))

	return op
	

def center_menu():

	ch = get_center_menu_option()

	student_data = pull("data-files/students.csv")
	center_data = pull("data-files/centers.csv")
	course_data = pull("data-files/courses.csv")

	while(ch):
		if ch == 1:
			try:
				index = isValid(center_data)

				if(index>=0):
					op = getMenuOption()
					while op:
						if op == 1:
							# GETTING LIST OF COURSES
							print("\n=================================================")
							print("LIST OF COURSES\n".center(45,' '))
							for row in course_data:
								print(f'Course Name : {row["name"]}\nFees : {row["fees"]}\n\n')
							print("\n=================================================")
							
						elif op == 2:
							# Getting list of allocated student
							student_data = sorted(student_data,key = lambda row : row['name'])
							cnt = 0
							print("\n=================================================")
							for row in student_data:
								if row['allocated_center_id'] == center_data[index]['center_id']:
									cnt+=1
									print(f'Name : {row["name"]}\nCourse Name : {row["allocated_course_name"]}\n\n')

							if cnt==0:
								print("No Record Found!")
							print("\n=================================================")
						elif op == 3:
							# Update status of reported student
							student_data = sorted(student_data,key = lambda row : row['name'])
							cnt = 0
							print("\n=================================================")
							for row in student_data:
								if row['allocated_center_id'] == center_data[index]['center_id'] and row['payment'] == "11800":
									row['reported_to_center'] = '1'
									cnt+=1

							if cnt == 0:
								print("No Record Found!")
							else:
								print("Record Updated!")
							print("\n=================================================")

						elif op == 4:
							# List of admitted student
							cnt = 0
							print("\n=================================================")
							for row in student_data:
								if row['prn'] != 'NA':
									cnt+=1
									print(f'Name : {row["name"]}\nCourse Name : {row["allocated_course_name"]}\n\n')
							
							if cnt == 0:
								print("No Record Found!")
							print("\n=================================================")
						else:
							print("Invalid option!")
						op = getMenuOption()
							


			except Exception as ex:
				print(ex)

		else:
			print("invalid Choice!")
		ch = get_center_menu_option()
