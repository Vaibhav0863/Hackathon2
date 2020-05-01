from data import *
student_data = pull('admission-test-cases/set1/05_students_after_round2.csv')

student_data = sorted(student_data,key = lambda row:int(row['form_no']))
cnt = 0
for row in student_data:
	if row['allocated_preference'] != '0':
		print(f'{row["form_no"]}=={row["name"]}=={row["allocated_preference"]}=={row["allocated_course_name"]}=={row["allocated_center_id"]}=={row["payment"]}')
		cnt+=1
print(cnt)