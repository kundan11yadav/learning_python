# cwh 100 days of python , more concepts
# 1,Error Handling 
# try:
#     n = int(input("Enter a number:"))

#     print("inside try ")
#     for i  in range(1,11):
#         print(f"{n} X {i} = {n * i}")

# except ValueError as v:
#     print(v , "I am valueError")

# except Exception as e:
#     print(e ,"I am in exception")
    
# 2. Docstring 
# used for telling about a function just below function definition 

# def add(a,b):
#     ''' This function adds two numbers
#     '''
#     return a + b 
# print(add(3,4))
# print(add.__doc__)

# 3. Finally 
# def func1():
#     try:
#         l = [2,3,4,5,6]
#         i = int(input("Enter a index:"))
#         print(l[i])
#         return 0 

#     except:
#         print("Some error occurred.")
#         return 1 
#     # even if function is returned, it always gets executed
#     finally:
#         print("I am always executed.")

# a = func1()
# print(a)

# 4. Custom error 

# n= int(input("Enter a number betn 2 and 8:"))

# if n<2 or n>8:
#     # raise ValueError("The number should be from 2 to 8")

# else:
#     print("Your lucky number is", n+1)

# class CustomError(Exception):
#     print("Server is off..")

# try:
#     a = input("Do you want to fetch or push,f or p:")
#     if a =='p':
#         print("Data pushed")

# except:
#     if a == 'f':
#         print(CustomError)    
        
####################################################################
# 5 SECRET CODE 

# import random
# import string

# Input from user
# word = input("Enter a message:")
# copy_word = list(word)
# n = len(word)

# def encode():
#     def random_str():
#         return ''.join(random.choices(string.ascii_letters, k=n))

#     random_prepend = random_str()
#     random_append = random_str()

#     if n >= 3:
#         # Rotate first letter to the end
#         first_letter = copy_word.pop(0)
#         copy_word.append(first_letter)
        
#         # Add random prepend and append
#         copy_word.insert(0, random_prepend)
#         copy_word.append(random_append)

#         # Return encoded string
#         final_word = "".join(copy_word)
#         return final_word
#     else:
#         # Reverse the word for short strings
#         rev_word = word[::-1]
#         print("Encoded word for short input:", rev_word)
#         return rev_word

# # Encoding
# encoded_word = encode()
# print("Encoded Word:", encoded_word)

# def decode():
#     if n >= 3:
#         # Remove first n and last n characters
#         copy_of_encoded = list(encoded_word)
#         decoded_word = copy_of_encoded[n:-n]  

#         # Move last letter back to the front
#         last_letter = decoded_word.pop(-1)
#         decoded_word.insert(0, last_letter)

#         # Return decoded string
#         final_decoded_word = "".join(decoded_word)
#         return final_decoded_word
#     else:
#         # Reverse decoding for short inputs
#         rev_word = encoded_word[::-1]
#         return rev_word

# # Decoding
# decoded_word = decode()
# print("Decoded Word:", decoded_word)

# ######################################################## 

# 6.Enumerate function 
# list = [2,3,4,5,6,7]

# for i,el in enumerate(list):
#     print(i , ":", el)
#     if i == 3:
#         print("I am third..")

# 7. if__name__ = "__main__"
# We add this if we import this file in another file then 
# to avoid running all the functions again

import functions as f

f.check(8)



    











































