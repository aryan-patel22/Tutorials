#python beginner tutorial for Booleans & Operators
#https://www.programiz.com/python-programming/online-compiler/
#Use for online compiler ^

#Boolean evaluates expressions tells you if statement is True or False
print('-------------------------------------------------------------------------')

print(10 > 9)
print(10 == 9)
print(10 < 9)

#using if conditional statement
print('-----------------------------------')
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#bool() function evaulates any value and returns True or False
#Eval str & num
print('-----------------------------------')

print(bool("Hello"))
print(bool(15))

#Eval two vars
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

"""
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones
"""

#Following will return True
print('-----------------------------------')

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

"""
Not many values eval to False except empty Vals such as
(),[],{},"", the number 0. and the value None
Value False evals to False
"""

#following will return False
print('-----------------------------------')
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#One object evals to False and thats if you have
#Object made from a class with __len__function that
#returns 0 or false
print('-----------------------------------')

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Can create function that returns Boolean Value
print('-----------------------------------')
def myFunction() :
  return True

print(myFunction())

#or

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Py has built-in fuctions that return boolean val like 
#ininstance() function - deteremines if obj is a certain data type
print('-----------------------------------')

x = 200
print(isinstance(x, int))

#ininstance() function - deteremines if obj is a certain data type
print('-----------------------------------')


#Operators used to perform ops on vars and vals
"""
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""
"""
Artithmetic Ops
used with numeric values to perform common mathematical operations

+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""

"""
Assigment Ops
used to assign values to variables

Op    Ex        Same As
=	    x = 5	    x = 5	
+=	  x += 3	  x = x + 3	
-=	  x -= 3	  x = x - 3	
*=	  x *= 3	  x = x * 3	
/=	  x /= 3	  x = x / 3	
%=	  x %= 3	  x = x % 3	
//=	  x //= 3	  x = x // 3	
**=	  x **= 3	  x = x ** 3	
&=	  x &= 3	  x = x & 3	
|=	  x |= 3	  x = x | 3	
^=	  x ^= 3	  x = x ^ 3	
>>=	  x >>= 3	  x = x >> 3	
<<=	  x <<= 3	  x = x << 3
"""

"""
Comparison Operators
Comparison operators are used to compare two values

==	  Equal                    	x == y	
!=	  Not equal   	            x != y	
>	    Greater than            	x > y	
<	    Less than	                 x < y	
>=	  Greater than or equal to	x >= y	
<=	  Less than or equal to	    x <= y
"""
"""
Python Logical Operators
Logical operators are used to combine conditional statements:

and 	Returns True if both statements are true	              x < 5 and  x < 10	
or	  Returns True if one of the statements is true	          x < 5 or x < 4	
not	  Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	
"""

"""
Python Identity Operators
Identity operators are used to compare the objects
not if they are equal, but if they are actually the
same object, with the same memory location:

is 	    Returns True if both variables are the same object	    x is y	
is not	Returns True if both variables are not the same object	x is not y	
"""
"""
Python Membership Operators
Membership operators are used to test if a sequence is presented 
in an object:


in     	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y	
"""

"""
Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:


& 	AND	Sets each bit to 1 if both bits are 1
|	  OR	Sets each bit to 1 if one of two bits is 1
^	  XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	  Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""

