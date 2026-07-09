#defn:python is high level and interpreted programming langauge
# num = input("Enter a num1:")#type of input is string
# num2 = input("Enter a num2:")
# print(int(num) + int(num2))
# print(type(num))
# name = "shicma"
# age = 22
# salary = 891273.97
# isAdult = True
# num = 2
# num1 = 4.5
# num3 = num + num1
# print(type(num3))#what is it implicit or Explicit ?

# print(id(num))#140714279773128
# print(id(num1))#1637006088688
# a = 10
# b = 10

# print(id(a) == id(b))

#operator operands
# print(10 + 10)

#Arithmatic opearator
# +,-,/,%,**,*,//

#assignment operator
name = "shivam"
# =,==, -=, +=, *=, /= (?, more has been seen by kavy)

# num = 5
# num = 2

# print(5 != 6)


#comparison operator
# >=, >, <, <= , 

#logical opeartor
# and, or, not

# print(True and True)#True
# print(True and False)#True
# print(True or False)#False
# print(True or True)#True
# print(not True)#false
# print(not False)#true

# isAdult = True
# isAdult = not isAdult
# isAdult = not isAdult
# isAdult = not isAdult
# isAdult = not isAdult
# isAdult = not isAdult
# print(isAdult)#false

#identity operator
#is , is not

# num = 10
# num2 = 10
# # print(id(num) == id(num2))
# print(num is not num2)

#membership opearator
# name = "Python"

# print("P" in name)
# print("z" not in name)

#conditional operator

print(10)
print("shivma")

age = 19
#prblm statement:greater then 18 to eligible to vote, agar greater then 22 eligible to buy house, if both 18 > and also 22 > then elegible to vote and buy house
age = int(input("enter your age:"))

if(age >= 18 and age <= 22):
    print("Eligible to vote")
elif(age >= 22):
    print("Eligible to buy house")
elif(age >= 18 and age >= 22):
    print("Eligible to vote and buy house")
else:
    print("Not eligible")