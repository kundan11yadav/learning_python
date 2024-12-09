# 1, Reading a file
f = open("raju.txt","r")

a = f.readline()
b = f.readline()
c = f.readline()

print(a, end="")
print(b, end="")
print(c, end="")
f.close()
from math import factorial

# 2. Writing into a file(it flushes entire file first)

f = open("raju.txt", "w")
f.write("I am Just a chill Guy")
f.close()

# 3. Append into a file

f = open("raju.txt" , "a")
f.write("\n and I like Netflix")
f.close()

# Deleting a file using OS module
import  os
os.remove("raju.txt")

# PQ, 1 create a new txt file using python and add sth

f = open("new.txt" , "w")
f.write("Mount Everest is the tallest mountain in world. \n Tenzing Norway Sherpa was first person to climb it.")

f.close()

























