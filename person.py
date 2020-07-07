class Person:

	def __init__(self, name, job = None, pay = 0):
		self.name = name
		self.job = job
		self.pay = pay


	def raisepay (self, percent):
		self.pay = int(self.pay + (1 + percent))

	def lastname (self):
		return self.name.split()[-1]


class Manager(Person):

	def __init__(self, name, pay):
		Person.__init__(self, name, 'mngr', pay)

	def raisepay(self, percent, bonus = 10):
		Person.raisepay(self, percent + bonus)


if __name__ == '__main__':


	bob = Person('Bob Johns')
	sue = Person("Sue Johns", 'dev', 100)
	sue.raisepay(2)							
	print(sue.__dict__)
	print(bob.lastname())

		######

	tom = Manager("Tom Howkins", 100)
	tom.raisepay(1)
	print(tom.__dict__)