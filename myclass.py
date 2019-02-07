class MyClass:
	
	def __init__(self,surname,city,profession):
		self.surname = surname
		self.city = city
		self.profession = profession
	def meth_1(self):
		print(self.surname)
		print(self.city)
		print(self.profession)

	def meth_2(self):
		self.surname = "Yessenbayev"
		self.city = "Astana"
		self.profession = "teacher"

