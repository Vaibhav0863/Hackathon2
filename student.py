import data


class Student:
	def __init__(self,name="VAIABHAV"):
		self.name = name

	def display(self):
		print(self.name)


def getChoice():
	print("0. EXIT\n1. REGISTER STUDENT\n2. SIGN IN\n3. LIST COURSES\n4. LIST CENTERS\n5. GIVEN PREFERENCES\n6. SEE ALLOCATED CENTER/COURSES\n7. UPDATE PAYMENT DETAILS")

	ch = int(input("ENTER YOUR CHOICE : "))
	return ch

def student_menu(student):

	ch = getChoice()
	while(ch):
		if ch == 1:
			print("Register Student")
		elif ch == 2:
			print("SIGN IN")
		elif ch == 3:
			print("LIST COURSES")
		elif ch == 4:
			print("LIST CENTERS")
		elif ch == 5:
			print("GIVEN PREFERENCES")
		elif ch == 6:
			print("SEE ALLOCATED CENTERS AND COURSES")
		elif ch == 7:
			print("UPDATE PAYMENT DETAILS")
		else:
			print("INVALID INPUT")
		ch = getChoice()

