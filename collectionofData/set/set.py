"""___________________________SET__________________________________________
1.unordered: The elements in a set do not have a defined order, and you cannot access them using indexes.
2.unique ELement
4.mutable
4.dynamic size
"""
# my_set = {1,2,3,4,4,3,5,7,6}
# print(my_set)
# # print(dir(my_set))
# my_set.add(5)
# my_set.update([2,7])#we'll see toomorrow

# myunique={1,2,3,4,5}
# print(7 not in myunique)

# num = 10
# num1 = 10
# print(id(num), id(num1))
# print(num is num1)
# print(dir(my_set))
C = {4,5,6}
A = {1,2,3}
B = {1,2,3,4,5,6,7}

# A.add(4)
# print(A)

# temp = {1,2,3}
# temp.clear()
# temp.add(1)
# temp.add(2)
# print(temp)

# temp2 = temp.copy()
# print(temp2)

#4.difference
# print(B.difference(A))
# print(B)
# #5.differenceUpdate
# B.difference_update(A)
# print(B)
# print(A.difference_update(B))#W'll see later onn

#6.discard
# A.discard(3)
# print(A)

# #7.intersection
# print(A.intersection(B)) #common element


# #8.interScetion_update
# B.intersection_update(A)
# print(B)


#9.issubset
print(A.issubset(B))#common element in A and B the it's true
print(B.issuperset(A))
# strng = "jksdnfsjkdf"
# strit = "jksd"
# striy = "sjkdf"
print(A.pop())


#10.remove

# B.remove(7)
# print(B)



#################Do it by yourself###############
# # 14. symmetric_difference() → non-common (new set)
# print(A.symmetric_difference(B))

# # 15. symmetric_difference_update() → keep non-common
# A.symmetric_difference_update(B)

# # 16. union() → combine sets (new set)
# print(A.union(B))

# # 17. update() → add all elements from B into A
# A.update(B)
#################Do it by yourself###############