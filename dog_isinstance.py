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

# is jim an instance of dog()?
print isinstance(jim,Dog)

#is julie an instance of dog()?
julie = Dog("julie",100)
print isinstance(julie,Dog)

# is johnny walker an instance of bulldog()?
johnnywalker = RusselTerrier("johnny walker",4)
print isinstance(johnnywalker,Bulldog)

# is julie an instance of jim?
print isinstance(julie,jim)
