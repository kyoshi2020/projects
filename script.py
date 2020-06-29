#!/bin/python3
#intro to python while learning ethical hacking. more of a review for me, I had already went through Automate the Boring Stuff previously.
#variables and methods
quote = "Choice is the act of hesitation before making a decision"
print(quote.upper()) # uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case

print(len(quote))


name = "Boris" #sting
age = 35 #integeter / int - no decimal point int(30)
gpa = 3.74 #float - has a decimal point float(3.7)

print(int(age))
print(int(30.9))

print("My name is " + name + " and I am " + str(age) + " years old.") # need to change age variable from int to str. str(age) so you can concatenate the whole thing

age +=1
print(age)

birthday = 1
age +=birthday
print(age)

print('\n')
#Functions
print("Here is an example function:")

def who_am_i(): #this is a function.
	name = "Boris"
	age = 35
	print("My name is " + name + " and I am " + str(age) + " years old.")
	
who_am_i()

#adding parameters
def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

#multiple parameters
def add(x, y):
	print(x + y)
	
add(7, 7)

def multiply(x, y):
	return x * y # store it for later. doesn't always have to print
	
print(multiply(7,7))

def square_root(x):
	print(x ** .5)
	
square_root(64)

def nl(): # save time by calling NL as a function for a new line instead of '\n' every time
	print('\n')
	
nl()

#Boolean expressions - (True or False)
print("Boolean Expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 !=9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

nl()
#Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 < 7) # False - both need to be true to be true.
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 < 7) #true because 1 statement has to be true for OR.

test_not = not True #False. not False = True

nl()
#Conditional statements
def drink(money):
	if money >=2:
		return "You've got yourself a drink!"
	else:
		return "NO drink for you!"

print(drink(3))
print(drink(1))

def alcohol(age, money): # you made a mistake here putting an extra letter in alcohol which made your function not work because it didn't have alcohol defined
	if (age >=21) and (money >= 5): #you had a syntax error here because you forgot the colon at the end.
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "You're too poor and too young."
		
print(alcohol(21, 5))
print(alcohol(21, 3))
print(alcohol(20, 5))
print(alcohol(20, 3))

nl()
#Lists - Have brackets [] inside those brackets are ITEMS
movies = ["The Matrix", "Fight Club", "V for Vendetta", "Inception"]

print(movies[1]) #returns the 2nd item in list. if we wanted first, we use 0
print(movies[0]) # returns first item in the list.
print(movies[1:3]) #start at index 1 - fight club - doesn't include 3 inception. this should only show fight club and v for vendetta
print(movies[1:]) # prints all the movies in the list from fight club to the end
print(movies[:1])# grabs everything before index 1. which is the Matrix
print(movies[:2]) # grabs the first 2.
print(movies[-1]) #grabs last  item off the list

print(len(movies)) # length of items in list
movies.append("Star Wars") #adds whatever you want to end of list
print(movies)

movies.pop() # deletes last item in list
print(movies)

movies.pop(0) #removes very first item in list. Matrix
print(movies)

nl()
# tuples - do not change. immutable. ()
grades = ("a", "b", "c", "d", "f") # example of tuple
print(grades[1])

nl()
#Looping

# For loops - start to finish of an interate
vegetables = ["cucumber", "spinach", "cabbage"] #list
for x in vegetables: # for every time in vegetables (x) print out that item
	print(x)
	
#  While loops - execute as long as true

i = 1 # starting variable. can be whatever letter/number you want

while i < 10: # while i is less than 10, do the thing below.
	print(i) # print i, then see below
	i += 1 # after printing i, add 1 to it. then goes back to the top to check if i is greater than 10 or not.
