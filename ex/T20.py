# -*- coding: euc-kr -*-

class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def bark(self):
		print(self.name, 'is barking')
		
def test1():		
	x = Dog('KuKu', 8)
	y = Dog('Mari', 7)
	x.bark()
	y.bark()
	print(str(x.name) + ' is ' + str(x.age) + ' years old.')
	print( '%s is %d years old' %(y.name, y.age) )
	print(y.name, 'is', y.age, 'years old.')

    
test1()

class Circle:
	def __init__(self, redius):
		self.redius = redius
		
	def area(self):
		a = 3.14 * pow(self.redius, 2)
		return a
	
	def perimeter(self):
		b = 2 * 3.14 * self.redius
		return b
	
def test2():
	x1 = Circle(2)
	print(x1.area())
	print(x1.perimeter())
	
test2()