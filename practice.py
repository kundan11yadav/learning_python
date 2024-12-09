# Practice sets from code with harry
# Q1 spam comment detector
from itertools import count

from adodbapi.examples.db_print import kw_args

comment = ["Nice Video","Do this and make a lot of money" ,"buy now","click this"]
for el in range(len(comment)):
    if comment[el] =="make a lot of money" or comment[el] == "buy now" or comment[el] == "click this":
        print("Spam Detected")
    else:
        print("No spam")

# Q3 Leap year Checker

yr = int(input("Enter the year:"))

if (yr%400 == 0)or (yr % 4 == 0 and yr % 100 != 0):
    print(yr,"is leap year")
else:
    print(yr,"is not leap year")

# Loops:Chai aur code problems
# Q1, count positive numbers in a list
number = [1,-2,3,-4,5,-6,7-8]
n = 0
for i in range(len(number)):
    if number[i] > 0:
        n +=1

print(n)

# Print multiplication table , skip 5
for i in range(1,11):
    if i == 5:
        continue
    else:
        print(8 ,"x",i ,"=", 8 * i  )


# FUNTIONS------CHAIAURCODE--------------------

# Q2 multiply string and int
def mul(a , b ):
    return a * b
print(mul(4,6))
print(mul("k",5))

# Q3 multiple return values area and perimeter

import  math

def circle(r):
    area =   math.pi * r ** 2
    perimeter = 2 * math.pi * r
    return  area  , perimeter

a,p = circle(7)
print("Area:",a ,"Perimeter:",p)


# Q5, default parameter value,
# greet user and no value provided greet with default value

def greet(name = "User"):
    print("Good Morning!,", name)

greet("Raju")
greet()

# Q6 lamda functions and anonymous functions
# create lambda function for cube of a number

cube = lambda  a: a ** 3
print(cube(3))

# Q7, functions with args
# function that takes different no of arguments and sums it
def add_all(*args):
    print(args)
    print(type(args))
    return sum(args)

print(add_all(2,3,4))
print(add_all(1,2))

# Q8 , Function with **kwargs(keyword arguments)

def handle_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

handle_kwargs(name="Binod" , adress= "Tengar")


# Q9, generator function that yeilds even num upto a limit

def even_generator(limit = 10 ):

   for i in  range(2,limit + 1 , 2 ):
       yield  i

for num in even_generator(10):
    print(num)

def first(n):
    def second(x):
        return x ** n
    return second
a = first(2)
# b = second(3)

# print(a(2) ,b(3) )