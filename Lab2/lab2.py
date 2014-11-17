class Animal:
	def __init__(self,name,age):
		 self.name = name
		 self.age = age

	def lasers(self):
		print self.name + " can shoot super cool death lasers out og his eyes, aaaand he is " + self.age + " years old"

	def dubstep(self):
		print self.name + " has been makin' sick wubs' for the whole " + self.age + " years he's been alive for"

class griffon(Animal):
	def __init__(self, name, age, wingspan, beaklength):
		Animal.__init__(self, name, age)
		self.wingspan = wingspan
		self.beaklength = beaklength

	def screech():
		print "KAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

class mudkip(Animal):
	def __init__(self, name, age, hp, move):
		Animal.__init__(self, name, age)
		self.hp = hp
		self.move = move

	def attack():
		print self.name " used " + self.move + "!!!"

swampy = mudkip("swampy", 14, 51, "Water gun")
peter = griffon("Peter", 42, 7.5, 0.3)