from data import *
from Algorithm import getPerefList,getCourses
from studentRegistration import studentRegistration,getEligibility

# This function return preferences given by student [course,center_id]
def getPreferenceList(student_data):
	preference_data = pull('data-files/preferences.csv')

	preference_dict = dict()

	for row in student_data:
		temp = []

		for pref_row in preference_data:
			if row["form_no"] == pref_row["form_no"]:
				temp.append([pref_row['course'],pref_row['center_id']])
		if len(temp)!=0:
			preference_dict[row['form_no']] = temp

	return preference_dict

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
	# THIS IS USED TO GET STUDENT RECORD
	student_data = pull("data-files/students.csv")
	# THIS IS USED FOR APPENDING PREFERENCES GIVEN BY STUDENT
	preference_data = pull("data-files/preferences.csv")
	# THIS IS FOR GETTING LIST OF CENTER
	center_data = pull('data-files/centers.csv')
	# THIS IS FOR GETTING COURSES DATA
	course_data = pull("data-files/courses.csv")


	preference_list = getPerefList()
	course_list = getCourses()
	eligibility_data = getEligibility()
	form_number = len(student_data)
	form_number +=1
	ch = getChoice()
	while(ch):
		if ch == 1:
			print(' \n'.center(55,'='))
			print("Student Registration\n".center(45,' '))
			new_student_data = dict()
			newStudent = studentRegistration(form_number,eligibility_data)
			try:
				newStudent.accept()
				new_student_data = newStudent.getRecord()
			except Exception as ex:
				print(ex)
			
			if len(new_student_data)!=0:
				student_data.append(new_student_data)
				print("New Student Registered Successfully!")
				form_number+=1
			print('\n '.center(55,'='))
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
							
							courses = eligibility_data.get(student_data[index]['degree'])
							courses = courses[1]
							
							print("================================================")
							print("\t\tAVAILABLE COURSES ACCORDING TO YOUR DEGREE\t\t\n")
							for row in course_data:
								if row['name'] in courses:
									print(f'Course Name : {row["name"]}\nFees : {row["fees"]}\nSection Rank Required : {row["section"]}\n\n')
							print("================================================")


						elif op == 2:
							
							print("================================================")
							print("\t\tAVAILABLE CENTERS\t\t\n")
							for row in center_data:
								print(f'Center Name : {row["center_name"]}\nCenter Co-ordinator : {row["coordinator"]}\nAddress : {row["address"]}\n\n')
							print("================================================")


						elif op == 3:
							flag = 1
							pref_list = preference_list.get(student_data[index]['form_no'],[])
							cnt = len(pref_list)
							eligible_courses = eligibility_data.get(student_data[index]['degree'])
							eligible_courses = eligible_courses[1]
							cnt+=1
							available_preferences = []
							sections = ['A','B','C']

							for rank in sections:
								courses = course_list.get(rank,-1)
								if courses!=-1 and int(student_data[index][rank]) > 0 :
									flag = 0
									for center_row in center_data:
										for course in courses:
											if course in eligible_courses:
												if [course,center_row['center_id']] not in pref_list:
													available_preferences.append([course,center_row['center_id']])
						
							if flag != 1:
								print("====================================================")
								print("\t\tGIVE YOUR PREFERENCE\t\t\n")
								while True:
									if cnt>10:
										print("10 preferences are already given")
										break
									print("0. EXIT")
									idx = 1
									for row in available_preferences:
										print(f'{idx}. {row[0]} {row[1	]}')
										idx+=1
									
									pref_no = int(input("Enter Your Preference Number : "))
									if pref_no == 0:
										break
									elif pref_no>=1 and pref_no <= idx:
										data = available_preferences.pop(pref_no - 1)
										print({'form_no' : student_data[index]['form_no'],'preference_no' : str(cnt),'course'  : data[0],'center_id' : data[1]})
										preference_data.append({'form_no' : student_data[index]['form_no'],'preference_no' : str(cnt),'course'  : data[0],'center_id' : data[1]})
										cnt+=1
										print("Your Preference Saved...")
									else:
										print("Please Enter valid preference number...!")
									
									
									ch = input("Do you want to continue...(y/n)")
									if ch == 'n':
										break
							else:
								print("==========================================================")
								print("Their is no valid rank for giving preferences!")
								print('==========================================================')
							
							preference_data = sorted(preference_data,key = lambda row : int(row['form_no']))


								
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
								if student_data[index]['payment'] == '0':
									print("Your first installment of 11800rs is still pending!")
									ip = input("Do you want to make payment?(y/n) : ")
									if ip == 'y':
										student_data[index]['payment'] = '11800'
										print("Payment Successful!!!")


								elif student_data[index]['payment'] == '11800':
									fee = 0
									for row in course_data:
										if row['name'] == student_data[index]['allocated_course_name']:
											fee = row['fees']
									print(f'Your Second installment of {fee}rs is still pending!')
									ip = input("Do you want to make payment?(y/n) : ")
									if ip == 'y':
										student_data[index]['payment'] = str(int(student_data[index]['payment'])+int(fee)) 
										print("Payment Successful!!!")
								else:
									print("Your payment was already done!")
						else:
							print("Invalid input");
						op = menu()

			except Exception as ex:
				print(ex)
		else:
			print("INVALID INPUT")
		ch = getChoice()
	pushF("data-files/students.csv",student_data)
	pushF("data-files/preferences.csv",preference_data)

