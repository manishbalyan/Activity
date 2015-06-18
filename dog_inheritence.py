# parent class
class Dog(object):
	# class attribute
	species = 'mammal'

	# instance attributes
	def __init__(self,name,age):
		self.name = name
		self.age = age

		#instance method
	def description(self):
		return "{} is {} years old".format(self.name,self.age)

		#instance method
	def speak(self,sound):
		return "{} says {}".format(self.name,sound)

# child class(inherits from dog class)
class RusselTerrier(Dog):
	def run(self,speed):
		return "{} runs {} ".format(self.name,speed)

# child class(inherits from dog class)
class Bulldog(Dog):
	def run(self,speed):
		return "{} runs {}".format(self.name,speed)

# child class inherits attributes and behaviour from parents class
jim = Bulldog("Jim",12)
print jim.description()

# child class have specific attributes and behaviour as well
print jim.run("slowly")

										
		
	
