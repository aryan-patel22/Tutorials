#python beginner tutorial for Strings
#https://www.programiz.com/python-programming/online-compiler/
#Use for online compiler ^

#Side note for at the end that I'm just adding at top
#Py has a set of built-in methods for strs and they return new vals
#they do not change the orginal string

#Can assign Multiline String to Vars by using 3 double or single quotes
print('-------------------------------------------------------------------------')

#a = '''Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.'''

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

#escape characters is backslash '\' followed by character you want
#escape characters used in Python
#\'	Single Quote	
#\\	Backslash	
#\n	New Line	
#\r	Carriage Return	
#\t	Tab	
#\b	Backspace	
#\f	Form Feed	
#\ooo	Octal value	
#\xhh	Hex value

#how to use double quotes inside str that surrounded by double quotes
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#String in py is array of btyes representing unicode characters
#py has no charater data type so single character is simply
#a string with length of 1
# Square brackets{} used to access elements of string
print('-----------------------------------')

a = "Hello, World!"
#Gets charater at pos 1 cause first character has pos 0
print(a[1])

#Strings are arrays so loop through characters with for loop
print('-----------------------------------')

for x in "banana":
  print(x)

#to get length od string use len() funct
print('-----------------------------------')

a = "Hello, World!"
#remeber counts spaces and punctions inside string
print(len(a))

#To check if certain phrase or character is present use the keyword 'in'
print('-----------------------------------')

txt = "The best things in life are free!"
print("free" in txt)

#use in if statement

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

print('-----------------------------------')

#to check if not present in string use 'not in'
txt = "The best things in life are free!"
print("expensive" not in txt)

#use in if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#To return range of chars(slice syntax)
#specify start index and the end of index, sep by colon, to return a 
#part of the string 
print('-----------------------------------')

#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

#Leaveing out start index, range start at first character

#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

#Leaveing out end index, range will go to the end

#Get chars from pos 2 and all the way to the end
b = "Hello, World!"
print(b[2:])

#Use negative indexes to start slice from end of string(Negative Indexing)

'''
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
'''

b = "Hello, World!"
print(b[-5:-2])

#Built-In methods that you can use on strings
print('-----------------------------------')

#upper() medthods returns string upper case
a = "Hello, World!"
print(a.upper())

#lower() medthods returns string lower case
a = "Hello, World!"
print(a.lower())

#Strip() method removes any whitespace
#(space before and/or after the actual text)
#from beginning or the end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#replace() method replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))

#split() method returns list where the text between specified separator
#becomes the list items

#split() method spilts the string into substrings 
#if finds instances of the separator
print('-----------------------------------')

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#To concatenate, or combine, two strings you can use the + operator

a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Use format() method to insert numbers into strings
#format() method takes passed arguments, formats them, and places
#them in the string where the placeholders {} are
print('-----------------------------------')

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Takes unlimited num of args, and are places into respective placeholders

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Use index numbers{0} to be sure the args are placed in the correct
#placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))