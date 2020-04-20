from data import *
from Algorithm import *
from datetime import datetime

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
	student_data = pull("data-files/students.csv")
	capacity_data = pull("data-files/capacities.csv")

	preference_dict = getPerefList() # return key and value pair of form no. and list of their preferences
	course_dict = getCourses()

	ch = getChoice()

	while(ch):
		if ch == 1:
			try:
				if isValid():
					op = getMenuChoice()
					while op:
						if op == 1:
							# Getting list of Courses provided by CDAC 
							course_data = pull("data-files/courses.csv")

							print("================================================")
							print("\t\tAVAILABLE COURSES\t\t\n")
							print("================================================")
							for row in course_data:
								print(f'Course Name : {row["name"]}\nFees : {row["fees"]}\nSection Rank Required : {row["section"]}\n\n')
							print("================================================")
						
						elif op == 2:
							# Getting list of CDAC traning centers
							center_data = pull('data-files/centers.csv')

							print("================================================")
							print("\t\tAVAILABLE CENTERS\t\t\n")
							for row in center_data:
								print(f'Center Name : {row["center_name"]}\nCenter Co-ordinator : {row["coordinator"]}\nAddress : {row["address"]}\n\n')
							print("================================================")
						
						elif op == 3:
							print("=============================================")
							print("\t\tStudent List\t\t\n\n")
							for row in student_data:
								print(f'Form Number : {row["form_no"]}\nStudent Name : {row["name"]}\n\n')
							print("=============================================")

						elif op == 4:
							# UPDATING RANK OF STUDENT 
							form_no = int(input("Enter The Form Number of Student : "))
							sections = ['A','B','C']
							for section in sections:
								rank = input(f'Enter The Rank of Section {section} : ')
								if len(rank) != 0:
									if int(rank)>0:
										student_data[form_no-1][section] = rank
									else:
										print("Invalid Rank!")

							print("===============================================")
							print("RANK OF STUDENT UPDATED!")
							print("===============================================")
						elif op == 5:
							# Center Allocation Round 1
							student_data,capacity_data=round1(student_data,capacity_data,preference_dict,course_dict)

						elif op == 6:
							# Center Allocation Round 2
							student_data,capacity_data=round2(student_data,capacity_data,preference_dict,course_dict)

						elif op == 7:
							# Getting List of Allocated students
							print("===========================================")
							print("LIST OF ALLOCATED STUDENTS\n".center(40,' '))
							cnt = 0
							for row in student_data:
								if row['allocated_course_name'] != 'NA':
									print(f'{row["form_no"]}=={row["name"]}=={row["allocated_course_name"]}=={row["allocated_center_id"]}')
									cnt+=1
							if cnt == 0:
								print("No Record Found!")
							
							print("===========================================")
									
						elif op == 8:
							# GETTING LIST OF PAID STUDENT
							print("===========================================")
							print("LIST OF PAID STUDENTS\n".center(40,' '))
							cnt = 0
							for student_row in student_data:
								if student_row['payment'] != '0':
									print(f'FORM NUMBER : {student_row["form_no"]}\nNAME : {student_row["name"]}\n\n')
									cnt+=1
							if cnt == 0:
								print("No Record Found!")
							print("===========================================")
						elif op == 9:
							# GETTING LIST OF REPORTED STUDENTS
							print("===========================================")
							print("LIST OF REPORTED STUDENTS\n".center(40,' '))
							cnt = 0
							for row in student_data:
								if row['reported_to_center'] != '0':
									print(f'FORM NUMBER : {row["form_no"]}\nNAME : {row["name"]}\nCOURSE : {row["allocated_course_name"]}\nCENTER : {row["allocated_center_id"]}\n\n')
									cnt+=1
							if cnt == 0:
								print("No Record Found!")
							
							print("===========================================")
						elif op == 10:
							# UPDATING PRN OF STUDENT WHO REPORTED TO CENTER
							year = datetime.now().year
							year = year*1000
							prn = "PRN"
							flag = 1
							for student_row in student_data:
								if student_row['reported_to_center'] != '0':
									year += int(student_row['form_no'])
									prn += str(year)
									student_row['prn'] = prn
									flag = 0
							if flag:
								print("===========================================")
								print("No Record Found!")
								print("===========================================")
							else:
								print("===========================================")
								print("Updated PRN Number of Students!")
								print("===========================================")
							



						elif op == 11:
							# GETTING LIST OF ADMITTED STUDENT
							print("===========================================")
							print("LIST OF REPORTED STUDENTS\n".center(40,' '))
							cnt = 0
							for row in student_data:
								if row['prn'] != 'NA':
									print(f'FORM NUMBER : {row["form_no"]}\nNAME : {row["name"]}\nCOURSE : {row["allocated_course_name"]}\nCENTER : {row["allocated_center_id"]}\n\n')
									cnt+=1
							if cnt == 0:
								print("No Record Found!")
							
							print("===========================================")
						else:
							print("Invalid Input...")
						op = getMenuChoice()
			except Exception as ex:
				print(ex)
		else:
			print("Invalid Input")

		ch = getChoice()
	pushF("data-files/students.csv",student_data)
	pushF("data-files/capacities.csv",capacity_data)