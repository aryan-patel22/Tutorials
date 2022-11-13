#python beginner tutorial for data types
#https://www.programiz.com/python-programming/online-compiler/
#Use for online compiler ^

"""
data types built-in by default, in these categories:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

Data type is set when you assign val to var
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview

If you want to specify data type can use following constructor functions:
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview
"""

#Can get data type of any obj with type function:
print('-------------------------------------------------------------------------')

x = 5

print(type(x))

"""
Ints:
Int, or integer, is a whole number, positive or negative
without decimals, of unlimited length.
"""
print('-----------------------------------')

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

"""
Floats:
Float, or "floating point number" is a number that is
positive or negative, containing one or more decimals
Can also be scientific num with "e" to indicate pow of 10
"""
print('-----------------------------------')

x = 1.10
y = 1.0
z = -35.59
a = -87.7e100

print(type(x))
print(type(y))
print(type(z))
print(type(a))

"""
Complex
Complex numbers are written with a "j" as the imaginary part:
"""
print('-----------------------------------')

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Can convert from one type to another with resepctive methods
#cannot convert complex numbers into another number type
print('-----------------------------------')
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""
Casting Strings
Can cast with str() that constructs a str from wide variety of data types
including str, integer and float literals
"""
print('-----------------------------------')

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#Py does not have random function but built-module called random
print('-----------------------------------')

import random

print(random.randrange(1,10))