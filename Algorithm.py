from data import *


def getCourses():
	course_data = pull("data-files/courses.csv")

	courses = dict()
	sections = ["A","B","C"]
	for i in sections:
		temp = []

		for row in course_data:
			if row["section"] == i:
				temp.append(row['name'])
		courses[i] = temp

	return courses

def getPerefList():
	preference_data = pull('data-files/preferences.csv')
	student_data = pull('data-files/students.csv')

	preference_dict = dict()

	for row in student_data:
		temp = []

		for pref_row in preference_data:
			if row["form_no"] == pref_row["form_no"]:
				temp.append([pref_row['course'],pref_row['center_id'],pref_row['preference_no']])
		if len(temp)!=0:
			preference_dict[row['form_no']] = temp

	return preference_dict

# THIS IS USED FOR INCREMENTING COUNT OF ALLOCATED STUDENT
def incrementor(capacity_data,center_id,course,preference_no,student_row):
	for capacity_row in capacity_data:
		if capacity_row['center_id'] == center_id and capacity_row['course'] == course:
			if int(capacity_row['count'])<int(capacity_row["capacity"]):
				capacity_row['count'] = str(int(capacity_row['count']) +1)
				student_row['allocated_course_name'] = course
				student_row['allocated_center_id'] = center_id
				student_row['allocated_preference'] = preference_no

# THIS IS FOR DECREMENTING COUNT OF ALLOCATED STUDENT
def decrementer(capacity,student):
	for capacity_row in capacity:
		if student["allocated_course_name"] == capacity_row['course'] and student['allocated_center_id'] == capacity_row['center_id']:
			if int(capacity_row['count']) > 0:
				capacity_row['count'] = str(int(capacity_row["count"])-1)
				# student_row['A'] = '-1'
				# student_row['A'] = '-1'
				# student_row['A'] = '-1'
				# student['allocated_course_name'] = 'NA'
				# student['allocated_center_id'] = 'NA'
				student['allocated_preference'] = '-1'
				student['payment'] = '-1'


# THIS IS FOR ALLOCATION ROUND 1

def round1(student_data,capacity_data,preference_dict,course_dict):
	# student_data = pull('data-files/students.csv')
	sections = ['A','B','C']

	for i in range(1,11):
		for rank in sections:
			student_data = sorted(student_data, key = lambda row : int(row[rank]))

			for row in student_data:
				if int(row['form_no']) > 0 and row['allocated_preference'] == '0':
					preference_data = preference_dict.get(row['form_no'],-1)
					courses = course_dict.get(rank)

					if preference_data != -1:
						for preference in preference_data:
							if preference[0] in courses and int(preference[2]) == i:
								course_name,center_id,preference_no = preference
								incrementor(capacity_data,center_id,course_name,preference_no,row)
								break			
		
			

	student_data = sorted(student_data, key = lambda row : int(row['form_no']))

	# pushF('student_round1.csv',student_data)
	# pushF('capacity_round1.csv',capacity_data)
	return [student_data,capacity_data]


# THIS IS FOR ALLOCATION ROUND 2

def round2(student_data,capacity_data,preference_dict,course_dict):
	

	for row in student_data:
		if row['allocated_preference'] != '0' and row['allocated_course_name'] != 'NA' and row['payment'] == '0':
			decrementer(capacity_data,row)



	for row in student_data:
		if row['allocated_preference'] != '0':
			row['allocated_course_name'] = 'NA'
			row['allocated_center_id'] = 'NA'
			row['allocated_preference'] = '0'


	for row in capacity_data:
		row['count'] = 0

	sections = ['A','B','C']

	for i in range(1,11):
		for rank in sections:
			student_data = sorted(student_data, key = lambda row : int(row[rank]))

			for row in student_data:
				if int(row['form_no']) > 0 and row['allocated_preference'] == '0' and row['payment'] != '-1':
					preference_data = preference_dict.get(row['form_no'],-1)
					courses = course_dict.get(rank)

					if preference_data != -1:
						for preference in preference_data:
							if preference[0] in courses and int(preference[2]) == i:
								course_name,center_id,preference_no = preference
								incrementor(capacity_data,center_id,course_name,preference_no,row)
								break	

	student_data = sorted(student_data, key = lambda row : int(row['form_no']))

	# pushF('student_round2.csv',student_data)
	# pushF('capacity_round2.csv',capacity_data)
	return [student_data,capacity_data]