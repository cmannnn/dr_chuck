class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Gareth', 'Bale', 200000)
emp_2 = Employee('Test', 'User', 50000)

print(emp_1.fullname())
print(Employee.fullname(emp_1))