class Dog(object):
	# class attributes
	species = 'mammal'
	# initalizer/ instance attributes
	def __init__(self, name,age):
		
		self.name = name
		self.age = age		
	# instant method
	def description(self):
		return "{} is {} years old".format(self.name,self.age)
	def speak(self,sound):
		return "{} says {} ".format(self.name,sound)
# instantiate dog object		
mikey = Dog("Mikey",6)			

# call instant method
print mikey.description()
print mikey.speak("Gruff Gruff")