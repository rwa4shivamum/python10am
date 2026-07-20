# ????*
# ???***
# ??*****
# ?*******
# *********
# n=5
# for i in range(n,0,-1):
#     for j in range(1,i):
#         print(" ", end=" ")
#     for k in range(0,n-i+1):
#         print("*", end=" ")
#     for z in range(0,n-i):
#         print("*", end=" ")
#     print("")

# num = 12
# num1 = 12.1
# name = "shis"
# isAdult = True

#collection of datatype 12,14,15,16,
# lst = [12,13,14] #list dataType
# tupl = (1,13,14) #tuple
# set1 = {1,2,3} #tuple
# Dictionary = {"name":"Shivma"} #dictionary
# strng = "shivam"
# city = 'Ahmedabad'
# #  0 1 2 3 4 5
# # "s h i v a m"
# # -6-5-4-3-2-1
# print(strng[4])#positive indexing
# print(strng[-2])#Negative Indexing

# #string[start : end : step]

# print(strng[0:5:3]) #slicing
# #A string is a sequence of characters enclosed in quotes.
# text = "Python Programming"

# print(text[0:6])    # Python
# print(text[7:18])   # Programming
# print(text[:6])     # Python
# print(text[7:])     # Programming
# print(text[::2])    # Pto rgamn

#string formatting
# name = "shivam"
# print("Hello " + name) #string concatination

# name = "kavy"
# age = 17

# # print("My name is {} and I am {} years old".format(name, age))

# print(f"my name is {name} and my age is {age}")


#string function help to do something with string

name = "akayahfsdbfjhsdgbjhdbjgvhbdasfgjhbjhsdgbfvjsdbv"
name1 = "ALAY"
print(name.upper())
print(name1.lower())
print(name.capitalize())
print(len(name))
print(name1.replace("L", "K"))

str = "kjsdfhbsjhdfsjkdf"
print(str[0])
print(str[-1])
str1 = "hello"
str2 = "world"

print(str1 + str2 + "Shivam")#stribng concatination
#4.slicing
print(str1[1:3])
#4.length of stinrg
print(len(str1))
str  = "   HEllokj world "
# print(str.lower())
# print(str.upper())
# print(str.title())
# print(str1.capitalize())
# print(str.strip())
# print(str1.split(''))['h','e','l','l','o']
print(str.find("World"))
print(str.replace("world", "Python"))

name = "Shivam"
age = 21
print(f"I am {name} and my age {age}")

#c++ string name = "shivam"

# lstOfDatatpyes = [1,"shivam",True,2.5]
# print(lstOfDatatpyes)
# del lstOfDatatpyes
# print(lstOfDatatpyes)


my_list = ['apple', 'banana', 'cherry', 'banana']
my_list.remove('cherry')
print(my_list)

mylist = [1,2,3]
mylist.append(4)
mylist.extend([6,7])
print(mylist)
# print(my_list.index("cherry"))
