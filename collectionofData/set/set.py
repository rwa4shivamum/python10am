"""___________________________SET__________________________________________
1.unordered: The elements in a set do not have a defined order, and you cannot access them using indexes.
2.unique ELement
4.mutable
4.dynamic size
"""
my_set = {1,2,3,4,4,3,5,7,6}
print(my_set)
# print(dir(my_set))
my_set.add(5)
my_set.update([2,7])#we'll see toomorrow

myunique={1,2,3,4,5}
print(7 not in myunique)

num = 10
num1 = 10
print(id(num), id(num1))
print(num is num1)