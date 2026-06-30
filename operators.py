#data types
# char,int, float, bool
#variable decalare type() , type conversion int("2") , 

# num1 = 2
# num2 = 4

# print(num1 + num2) #variable that perform arithmatic operation

# print(3 + 4) #value that perform arithmatic operation


# operator = +, -, * , / , % 
# operands = the aside value between operator


#Arithematic operators
# print(10 + 1)
# print(10 - 1)
# print(10 * 2)
# print(10 / 2)
# print(10 // 3) #floor
# print(10 % 3) #modulo
# print(10 ** 4) #10 * 10 = 100 * 10 = 1000 * 10 = 10000
#-5 -4 -3 -2 -1 0 1 2 3 4 5 6

#Assignment operator

# num1 = 4
# num1 += 5
# num1 -= 4
# num1 *= 2
# num1 /= 10
# print(num1)


#comparison operator
# print(1==1)
# print(1!=2)
# print(10 > 2)
# print(10 < 2)
# print(10 >= 10)
# print(10 <= 10)


#logical operator
# print(True and False)
# print(False or True or False)
# num1 = not True


#identity operator
# a = 1
# a = 1 (893472)
# b = 2
# [1,2,9] (83291)
# a = 83291
# a = 83291

###########################identity Operator Later Onn 


#membership Operator 
name = "Python"

# print("P" in name)
# print("z" not in name)

# print((10 + 2) + 2**2 / 2 * 2 + 3 - 3)
#       12 + 4 + 3 - 3 = 16

num1 = "2"
# print(int(num1) + 2)


# TYPE CONVERSION
#1. IMplicit Type Conversion - python automatically convert datatype
# a = 10
# b = 5.5
# c = a+b
# print(c, type(c))

#2.Explicit Type Conversion
# print(int("2"))
# print(type(float(2)), float(2))
# print(str(2), type(str(2)))
# print(bool("Python"))

#do find what is truthy value and falsy value

# id is used to identify memory address of variable
# print(id(1))
a = [1, 2]
b = a

print(id(a))
print(id(b))
print((10 > 5 or 5 > 10) and not(3 == 3))