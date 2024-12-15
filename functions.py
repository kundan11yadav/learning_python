from math import factorial

def calc_sum(a , b ):
        return a + b
    
def avg(a,b,c=8):   #  8 is default parameter
        print("The average is:", (a+b+c)/3)

def fact(n):
        f = 1
        for i in range (1, n+1):
            f *= i
        print(f)  
        
def converter():
        usd = int(input("Enter USD::"))
        npr = usd * 120
        print("The NPR is ::",npr)
        
def square():
        a = int(input("Enter a number:"))
        sq = a * a
        return  sq

def check(n):
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")   

def main():
    value = calc_sum(3.5,6)
    print(value)
    avg(20,6)
    fact(5)
    converter()
    check(7) 



if __name__ == '__main__':
    main()



#-----------------------Recursion--------------
# Q1 print 5 to 1
# def show(n):  #Base Case
#     if n == 0:
#         return
#     print(n)
#     show(n-1)

# show(5)

# #Q2. find factorial
# a = int(input("Enter a number:"))
# def calc_factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * calc_factorial(n-1)
# print(calc_factorial(a))

# # Q3. sum upto n natural numbers
# lim = int(input("Enter the number upto:"))
# def calc(n):
#     if n == 0:
#         return 0
#     elif n ==1:
#         return 1
#     else:
#         return n + calc(n-1)

# val = calc(lim)
# print("The sum is:",val )

# #Q4. Recursion to print all elements in list
# name = ["Raju", "Hari" , "Shyam"]

# def pr_list(idx):
#     if idx == (len(name)+ 1):
#         return
#     print(name[idx])

# pr_list(2)
