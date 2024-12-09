#from list , tuple, dictionary,and sets

# -------------------Lists------------------------------------

#same as array but array is collection of similar data types
#but in list different data types can be stored

marks = [23,34,45,56,78,89]

print(type(marks) , marks[3])
print(len(marks))

m2 = ["a" , 5, [2,3,4] , False]
print(m2)
print(type(m2[3]))
print(type(m2[2]))
print(type(m2[1]))

# lists are mutable i.e values of index can be changed but not that of string
customer = ["raju" , 29 ,700]
print(customer[0])

customer[0] = "shyam" 
print(customer[0])

# slicing of list 
print(marks[1:3])
print(marks[1:])
print(marks[:1])
print(marks[-4:-3])

# methods of list 

pin = [2,7,6,5,1,9]
pin.append(12)
pin.append(15)
pin.sort()
print(pin)

# list methods return none type and changes original list 
# string methods return updated string but original string is not changed

print(type(pin.sort()))
pin.sort(reverse=True)
print(pin)
pin.sort()
print(pin)
pin.reverse()
print(pin)

list = ["banana" , "mango" , "cherry"]
print(list)
list.sort()
print(list)
list.sort(reverse= True)
print(list)

list.insert(2, "Papaya")
print(list)
list.sort()
print(list)

list.pop(1)
print(list)
pin.remove(7)
print(pin)

pin2 = pin.copy()
print(pin2)
print(type(pin2.copy()))

# Q1 ask name of movies and store in list 
movie1= input("Enter name of three movies:")
movie2=input(":")
movie3=input(":")

list = [movie1,movie2,movie3]
print(list)

# Q2 check if list contains palindrome of elements
list1 = [2,3,4,8,2]

temp1 = list1.copy()
temp1.reverse()
print(list1)
print(temp1)
if temp1 == list1:
    print("Is palindrome")
else:
    print("Not palindrome")

# ----------------------Tuples--------------------------
tup = (2,3,4,5,6)
print(tup)
print(type(tup))

print(tup[1:4])

print(tup.count(2))
print(tup.index(4))

# Q3 count the number of students with grade A 

tup = ("C", "D" , "A" ,"B","B","A")
a = tup.count("A")
print(a)

# ---------------------------Dictionary---------------------
# key value pairs , mutable ,unordered ,  non duplicate keys
info = {
    "name" : "Raju",
    "age" : 19,
    'adr' : "Ktm",
    "is_adult" : True
}
print(info)
print(type(info))
info["name"] = "Shyam"
print(info["name"])
info["surname"] = "Yadav"
print(info)

null = {}
print(type(null))

# Nested Dictionary 
student = {
    "name" : "Binod",
    "subjects": {
        "physics" : 56,
        "chemistry" : 65,
        "maths" : 71
    }
}
print(student["name"])
print(student["subjects"]["physics"])

# Methods of dictionary
data  =   {
    "name" : "Rakesh",
    "age" : 19,
    "isPresent" : False,
    "adr" : "Ramgopalpur"
}

copied = data.copy()

print(len(data.keys()))
print(list(data.keys()))

print(data.values())
print(list(data.values()))
print(data.items())
print(data.get("age2"))
print((data["age2"]))
data.update({"marks" : 78 })
print(data)


# --------------------------Sets-----------------------------------
# collection of unordered items , unique and elements are immutable
# But set itself is mutable

num = {1,2,3,4,2,3,"Raju",False}
print(num)
print(type(num))

dj = set() #null set syntax
print(type(dj))

num.add(5)
num.add((8,9,6))
print(num)
num.remove(3)
print(num)
num.pop()
print(num)
num.clear()
print(num)

# Union and Intersection
A = {1,2,3}
B = {3,4,5}
print(A.union(B))
print(B.intersection(A))

# Q1 prepare a dictionary
d = {
    "table" : "a piece of furniture", 
    "apple" : "a type of fruit , usually red",
    "cat" : "a small animal",
    "meadow" : "grassland"
}
user = input("Enter The word:")
if user in d :
    print(d[user])

else:
    print("Invalid Input!!!")
    print("Mission Failed")
    