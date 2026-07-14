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

# print(10)
# print("shivma")

# age = 19
#prblm statement:greater then 18 to eligible to vote, agar greater then 22 eligible to buy house, if both 18 > and also 22 > then elegible to vote and buy house
# age = int(input("enter your age:")) #17

# if(age >= 18 and age >= 22):
#     print("Eligible to vote and buy house")
# elif(age >= 18):
#     print("Eligible to vote")
# else:
#     print("Not eligible")


# print("Hello")
# print("jnefn")

# num = 194
# num1 = num // 10
# lstDigit = num % 10
# print(num1, lstDigit)
# num2 = num1 // 10 
# scndLastDigit = num1 % 10
# print(num2,scndLastDigit)
# num3 = num2 // 10
# thirdLastDigit = num2 % 10
# print(num3, thirdLastDigit)

# num = 194
# num1 = num % 10
# print(num1)
# num2 = num1 % 10 
# print(num2)
# num3 = num2 % 10
# print(num3)



# num = 194
# total = 0
# count = 0
# while(num > 0):
#     lstDigit = num % 10
#     total = total + lstDigit
#     count = count + 1
#     num = num // 10
# #num=194;total = 0 while(194 > 0): lstDigit = num % 10 ; lstDigit = 4; total = 0 + 4; total = 4; num = 194 // 10 num=19
# #num=19; total = 4 while(19 > 0): lstDigit = 19 % 10; lstDigt = 9; total = 4 + 9 = 13; num = 19 // 10; num = 1
# #num=1; total = 13 while(1 > 0): lstDigit = 1%10; lstDigt = 1; total = 13 + 1=14; num = 1 // 10; num=0
# #num=0; total = 14 while(0>0)
# print(total, count)



# name1="shivam"
# name2="shivanakn"
# name3="jsklfs"
# name4="kljsndf"
# name5="kjsdfn"
# print(name)
# #              0         1       2         3         4
# lstofName = ["shivam" ,"sani", "kajal", "sohuvn", "jhbdsf"] 
# print(lstofName[4])


# for i in range(5):
#     print(i)

#            start, stop, step  
# for i in range(1,5,2):
#     print(i)

# for i in range(10,-10,-2):
#     print(i)
-5,-4,-3,-2,-1,0,1,2,3,4,5
for i in range(0):
    print(i)

#10,8,6,4,2,0,-2,-4,-6,-8