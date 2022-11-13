#python beginner tutorial for variables
#https://www.programiz.com/python-programming/online-compiler/
#Use for online compiler ^

#This is a comment in Python!

print('-------------------------------------------------------------------------')
#how to print statements
#String variable can be declared by either " " or ' ' 

print("Hello, World!")

#python has no command for declaring variables
#created the moment you first assign a value
print('-----------------------------------')

x = 5
y = 2
z = "John"

print(x)
print(y)
print(z)

#other languages use indents for readability only
#Python uses indentation to indicate a block of code

if x > y:
    print("X is indeed greater than y")
    

#This will throw an error but its commented out to keep program running
#if x > y:
#print("X is indeed greater than y")

#also have to use same number of spaces or it throws an error
#if x > y:
#    print("X is indeed greater than y")
#       print(z)

#Variables don't have to be declared with particular type and
#can change type after they been set
print('-----------------------------------')

x = 10
print(x)

x = "Tommy"
print(x)

#if u want specify data type can be done with casting
#you can get data type of variable with type() function
print('-----------------------------------')

x = str(3)      # x will be '3'
y = int(3)      # y will be 3
z = float(3)    # z will be 3.0

print(x)
print(type(x))

print(y)
print(type(y))

print(z)
print(type(z))

#Can assign vales to mutiple varibles in one line
#make sure # of vars matches # of vals or its an error
print('-----------------------------------')

x, y, z, = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#Can assign same value to mutiple vars in one line
print('-----------------------------------')

x = y = z = "Orange"

print(x)
print(y)
print(z)

#if collections of vals in list,tuple,etc
#Py allows you to extract vals to varibles 
#This is called "unpacking"
print('-----------------------------------')

#This is a list btw in Python 
fruits = ["apple", "banana", "cheery"]
x, y, z = fruits

print(x)
print(y)
print(z)

#you can output mutiple values seperated by a coma
print('-----------------------------------')

x = "Py"
y = "is"
z = 8

print(x, y, z)

#can use + op to outpout multiple vars
print('-----------------------------------')

x = "Py"
y = "is"
z = " awesome"

print(x + y + z)

#For nums + op works mathematicaly
print('-----------------------------------')

x = 5
y = 10
print(x + y)

#With print() function when try combine str & num with + op its error

#x = 5
#y = "John"

#print(x + y)

#Best way to outpost multiple vars with print() is seperate with commas
#Which even supports different data types
print('-----------------------------------')

x = 5
y = "John"

print(x, y)

#Can create Var with same name inside function
# will be local and only used in function
#global varf with same name will remain as was global & orginal val
print('-----------------------------------')

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Can create global var inside function with global keyword
print('-----------------------------------')

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change val of global func, refer to var with global keyword
print('-----------------------------------')
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
