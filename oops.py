# APNA College _-- OOPs part 1
class Student:
    name = "Binod"
s1 = Student()
print(s1.name)
print(type(s1))

class Car:
    def __init__(self,extra): #Constructor runs everytime with each object
        self.another = extra
        print("adding new car..")
    color = "blue"
    brand =  "TATA"
car1 = Car("Tesla")
print(car1.another)
print(car1.color)
print(car1.brand)

class Stud:
    # default constructor
    def __init__(self):
        pass
    # parameterized constructor
    def __init__(self, name, marks):
        print("adding new student , I am constructor")
        self.name = name
        self.marks = marks

s1 = Stud("Raju",67)
print(s1.marks , s1.name)

s2 = Stud("Binod" , 89)
print(s2.marks , s2.name)

#Create a class and object
class Student:
    college = "KMC" #It is class attribute
    dressCode = "Coat"

    def __init__(self,fname ,adrress , percentage): #Constructor
        print("adding new student...")
        self.name = fname #It is object attribute
        self.adr = adrress
        self.percentage = percentage

    def design(self): # It is method
        print("I am in designing  team" ,self.name)

    def market(self):
        print("I am in marketing team" , self.name)


s1 = Student("Raju", "JNK" , 89)
print(s1.name,s1.adr,s1.percentage,s1.college,s1.dressCode)
s1.design()
s2 = Student("Golu" , "KTM" , 78)
s2.market()
print(s2.name,s2.adr,s2.percentage,s2.college,s2.dressCode)


# Create a Student that takes name and marks
# Also a method to print average

class Student:
    def __init__(self, name, sub1, sub2, sub3):
        print("Adding student...")
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    @staticmethod #Decorators to change behaviour and make into class function , no
                    # no need of self
    def sayHello():
        print("Hello")

    def average(self):
        return (self.sub1 + self.sub2 + self.sub3) / 3

s1 = Student("Raju", 56, 67, 76)
avg = s1.average()
print(f"Average marks for {s1.name}: {avg}")
s1.sayHello()

class Calculator:
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 =  num2

    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2

value = Calculator(4 , 5)
print(value.add())
print(value.subtract())
print(value.multiply())
print(value.divide())

# Static Methods

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Class Started")

car1 = Car()
car1.start()

# Create Account class with attributes balance and account no
# Also methods for debit credit and printing the balance
class Account:
    def __init__(self ,acc_no , balance):
        self.acc_no = acc_no
        self.balance = balance

    def debit(self,amount):
        self.balance += amount
        print("Rs.",amount ,"was debited.")

    def credit(self ,amount):
        self.balance -= amount
        print("Rs.", amount , "was credited.")

    def printBalance(self):
        print(self.balance)

acc1 = Account(2002 , 5000)
print("AC_NO:",acc1.acc_no , "CurrentBalance:",acc1.balance)
acc1.credit(3000)
print("AC_NO:",acc1.acc_no , "CurrentBalance:",acc1.balance)
acc1.debit()

# APNA College --- OOPs part 2
# Inheritance
class Car:
    def __init__(self):
        pass
    @staticmethod
    def start():
        print("Car is starting..")
    @staticmethod
    def stop():
        print("Car is stopping..")

class ToyataCar(Car):

    def __init__(self ,name):
        self.name = name

car1 = ToyataCar("Mahindra")
car2 = ToyataCar("TATA")

print(car1.start())
print(car2.stop())

#Multiple Inheritance

class A:
    a = "I am in A ,"
class B:
    b = "I am in B , "
class C(A,B):
    c = "I am in C , "
c1 = C
print(c1.a , c1.b , c1.c )





























