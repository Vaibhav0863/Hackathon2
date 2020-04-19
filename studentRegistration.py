from data import *
class studentRegistration:
	def __init__(self,form_no,eligibility_dict):
		self._form_no = form_no
		self._name = 'NA'
		self._A = '-1'
		self._B = '-1'
		self._C = '-1'
		self._degree = 'NA'
		self._percentage = '0'
		self._allocated_preference = '0'
		self._allocated_course_name = 'NA'
		self._allocated_center_id = 'NA'
		self._payment = '0'
		self._reported_to_center = '0'
		self._prn = 'NA'
		self._elib_dict = eligibility_dict
	
	# GETTING AND SETTER

	# SETTING NAME
	def setName(self,name):
		if len(name) == 0:
			raise Exception("Invalid Name!")
		else:
			self._name = name

	# SETTING DEGREE
	def setDegree(self,degree):
		temp = self._elib_dict.get(degree,-1)
		if temp == -1:
			raise Exception("Sorry! your are not eligible.")
		else:
			self._degree = degree

	# SETTING PERCENTAGE
	def setPercentage(self,percentage):
		if int(self._elib_dict[self._degree][0]) >= int(percentage):
			raise Exception("Sorry! Your percentage is too low.")
		else:
			self._percentage = percentage


	# GETTING NAME
	def getName(self):
		return self._name	

	# GETTING DEGREE
	def getDegree(self):
		return self._degree	
	
	# GETTING PERCENTAGE
	def getPercentage(self):
		return self._percentage

	def accept(self):
		try:
			name = input("Enter Name : ")
			self.setName(name)

			degree = input("Enter Your Degree : ")
			self.setDegree(degree)

			percentage = input("Enter Your Percentage : ")
			self.setPercentage(percentage)

		except Exception as ex:
			raise Exception(ex)

	def getRecord(self):
		form_no = self._form_no
		name = self.getName()
		degree = self.getDegree()
		percentage = self.getPercentage()
		
		return {'form_no' : str(form_no),
				'name': name,
				'A':'-1',
				'B':'-1',
				'C':'-1',
				'degree':degree,
				'precentage':percentage,
				'allocated_preference' : self._allocated_preference,
				'allocated_course_name' : self._allocated_course_name,
				'allocated_center_id' : self._allocated_center_id,
				'payment' : self._payment,
				'reported_to_center' : self._reported_to_center,
				'prn' : self._prn}



# THIS IS FOR GETTING KEY AND VALUE OF DEGREE AND MINIMUM PERCENTAGE
def getEligibility():
	elib_data = pull("data-files/eligibilities.csv")
	data = dict()
	for row in elib_data:
		degree = row['degree']
		min_percentage = 0
		courses = []
		for row1 in elib_data:
			if row1['degree'] == degree:
				min_percentage = row1['min_percentage']
				courses.append(row1['course'])
		data[degree] = [min_percentage,courses]

	return data