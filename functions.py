def calc_sum(a , b ):
    return a + b
value = calc_sum(3.5,6)
print(value)
from math import factorial

#function to find average of 3 numbers
def avg(a,b,c=8):   #  8 is default parameter
    print("The average is:", (a+b+c)/3)

avg(20,6)

#Q1 length of list
cites = ["jnk", "ktm" , "pok","hkkk"]

def mk(variab):
    print(len(variab))
mk(cites)

#Factorial of a number

def fact(n):
    f = 1
    for i in range (1, n+1):
        f *= i
    print(f)
fact(5)

# Convert USD in NPR
def converter():
    usd = int(input("Enter USD::"))
    npr = usd * 120
    print("The NPR is ::",npr)

converter()
# Four types of functions
# 1.  no argument no return
def square():
    n = int(input("Enter a number:"))
    sq = n * n
    print("The square is", sq)
square()

#2. with argument no return
def square(n):
    sq = n * n
    print("The square is:", sq)

a = int(input("Enter a number:"))
square(a)

#3. no argument with return
def square():
    a = int(input("Enter a number:"))
    sq = a * a
    return  sq

print("The square is" , square())

#4. with argument and return
def square(n):
    sq = n * n
    return  sq

a = int(input("Enter a number:"))
b = square(a)
print("The square is:", b)

# Q1 Odd or even
num = int(input("Enter a number:"))

def check(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
check(num)

#-----------------------Recursion--------------
# Q1 print 5 to 1
def show(n):  #Base Case
    if n == 0:
        return
    print(n)
    show(n-1)

show(5)

#Q2. find factorial
a = int(input("Enter a number:"))
def calc_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calc_factorial(n-1)
print(calc_factorial(a))

# Q3. sum upto n natural numbers
lim = int(input("Enter the number upto:"))
def calc(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return n + calc(n-1)

val = calc(lim)
print("The sum is:",val )

#Q4. Recursion to print all elements in list
name = ["Raju", "Hari" , "Shyam"]

def pr_list(idx):
    if idx == (len(name)+ 1):
        return
    print(name[idx])

pr_list(2)
