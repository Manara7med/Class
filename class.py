#Event-driven programming
#In computer programming, event-driven programming is a programming paradigm in which the flow of the program 
#is determined by events such as user actions (mouse clicks, key presses), sensor outputs,
#or message passing from other programs or threads.

#Example
#The following example of event loop helps in printing hello world by using the get_event_loop() method.
#This example is taken from the Python official docs.
#import asyncio
#def hello_world(loop):
 #  print('Hello World')
  # loop.stop()
#loop = asyncio.get_event_loop()
#loop.call_soon(hello_world, loop)
#loop.run_forever()
#loop.close()

###########################################################################################


def circle():

   print("You choose Circle...")

   radius=int(input("enter the radius : "))

   print("Area of the circle with the radius of ",radius," units is", 3.14*1(radius**2),"square units.")

def square():

   print("You choose Square...")

   side=int(input("enter the size of a side of a square : "))

   print("Area of the square with the a side of ",side," units is",side**2,"square units.")


def rectangle():

   print("You choose Rectangle...")

   length=int(input("enter the length of the rectangle : "))

   breadth=int(input("enter the breadth of the rectangle : "))

   print("Area of the rectangle with length and breadth ",length, " ",breadth," units is",length*breadth,"square units.")

print("Menu-\n"

       "1. Circle\n"

       "2. Square\n"

       "3. Rectangle\n")


x=int(input("Enter the corresponding number of a shape given in the menu, whose area you wants to calculate : "))

if x==1:

   circle()

elif x==2:

   square()

elif x==3:

   rectangle()

else:

   print("Wrong Input!")
   
print("####################################################")   

# Python program to demonstrate
# use of class instance ,class method and static method.
from datetime import date
class Person:
    # instance class
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
   
   


