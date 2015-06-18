class Dog(object):
	species = 'mammal'
	def __init__(self, name,age):
		
		self.name = name
		self.age = age		
		
philo = Dog("Philo",5)
mikey = Dog("Mikey",6)
jackey = Dog("Jackey",7)

def get_biggest_number(*args):
	if (philo.age > mikey.age) and (mikey.age > jackey.age):
		return biggest = philo.age
		
	elif (mikey.age > philo.age) and (philo.age > jackey.age):
		return biggest = mikey.age

	else:
		return biggest = jackey.age
	


		

print "The oldest gog is {} year old".format(biggest)

