class MyClass:
	_Id = 0
	def __init__(self,surname,city,profession):
                MyClass._Id += 1
                self._cId = MyClass._Id
                self.surname = surname
                self.city = city
                self.profession = profession
	def meth_1(self):
                print("ID:", self._cId)
                print("Surname: ",self.surname)
                print("City: ", self.city,)
                print("Profession", self.profession)
                print('------------------')

	def meth_2(self):
		self.surname = "Yessenbayev"
		self.city = "Astana"
		self.profession = "teacher"

 
