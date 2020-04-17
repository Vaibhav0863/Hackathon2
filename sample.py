from data import *

def getCourses(sec):
	course_data = pull("data-files/courses.csv")

	courses = {}

	sections = ["A","B","C"]
	for i in sections:
		temp = []

		for row in course_data:
			if row["section"] == i:
				temp.append(row['name'])
		courses[i] = temp

	return courses.get(sec)

def getPerefList(id):
	preference_data = pull('data-files/preferences.csv')
	student_data = pull('data-files/students.csv')

	preference_dict = {}

	for row in student_data:
		temp = []

		for pref_row in preference_data:
			if row["form_no"] == pref_row["form_no"]:
				temp.append([pref_row['course'],pref_row['center_id'],pref_row['preference_no']])
		if len(temp)!=0:
			preference_dict[row['form_no']] = temp

	return preference_dict.get(id,-1)

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
				student['allocated_course_name'] = 'NA'
				student['allocated_center_id'] = 'NA'
				student['allocated_preference'] = '0'


# THIS IS FOR ALLOCATION ROUND 1

def round1():
	student_data = pull('data-files/students.csv')

	capacity_data = pull("data-files/capacities.csv")

	rnd = 0 # THIS IS FOR COUNCELLING ROUND

	sections = ['A','B','C']

	for rank in sections:
		# FIRST SORT STUDENT DATA BY SECTION
		student_data = sorted(student_data,key = lambda row : int(row[rank]))
		for row in student_data:
			if int(row[rank]) > 0 and int(row['allocated_preference']) == 0:
				preferances = getPerefList(row['form_no'])
				courses = getCourses(rank)
				

				if preferances != -1:
					if preferances[0][rnd] in courses:
						course_name,center_id,preference_no = preferances[rnd]
						incrementor(capacity_data,center_id,course_name,preference_no,row)
			

	student_data = sorted(student_data, key = lambda row : int(row['form_no']))

	pushF('student_round1.csv',student_data)
	pushF('capacity_round1.csv',capacity_data)


# THIS IS FOR ALLOCATION ROUND 2

def round2():
	student_data = pull('student_round1.csv')

	capacity_data = pull("capacity_round1.csv")

	rnd = 0 # THIS IS FOR COUNCELLING ROUND

	# for row in student_data:
	# 	if row['allocated_course_name'] != 'NA' and int(row['payment']) == 0:
	# 		decrementer(capacity_data,row)

	# pushF('student_round2.csv',student_data)

	sections = ['A','B','C']

	for rank in sections:
		# FIRST SORT STUDENT DATA BY SECTION
		student_data = sorted(student_data,key = lambda row : int(row[rank]))
		for row in student_data:
			preferances = getPerefList(row['form_no'])
			courses = getCourses(rank)
			# Student get preferece and also make payment
			if int(row['allocated_preference']) != 0 and int(row['payment']) != 0:
				print("YES")
			# student get preference but does not make payment
			elif row['allocated_preference'] != '0' and int(row['payment']) == 0:
				if preferances[0][rnd] in courses:
					decrementer(capacity_data,row)
			else:
				if int(row[rank]) > 0 and int(row['allocated_preference']) == 0:

					if preferances != -1 :
						if preferances[0][rnd] in courses:
							course_name,center_id,preference_no = preferances[rnd]
							incrementor(capacity_data,center_id,course_name,preference_no,row)

	student_data = sorted(student_data, key = lambda row : int(row['form_no']))

	pushF('student_round2.csv',student_data)
	pushF('capacity_round2.csv',capacity_data)

round1()
round2()