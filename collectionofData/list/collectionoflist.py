# name1="kjsbfd"
# name2="ajkbsd"
# name3="kjsbd"
# name4="sdfsdf"


# print(collectionList)
# #1.allows duplicate 
# #2.mutable(can cahnge the value)
# #3.value get by indexed or change by indexed
# #4.supported ordered manner
# collectionList[1] = "sani"
# print(collectionList)
# # print(collectionList[0])

# print(len(collectionList)) #len(collectionList)
# # for i in collectionList:
# #     print(i)


# #list                0         1         2         3         4
# collectionList = ["shivam", "shivam", "ahajds", "kjbsd", "skdjfns"]
# collectionList[1] = "sani"
# print(collectionList[1])
# # for i in collectionList:
# #     print(i)
# print(len(collectionList))
# lengthOfCollect = len(collectionList)
# for i in range(lengthOfCollect):
#     if(i%2==0):
#         collectionList[i] = "some"
#     print(collectionList[i])

# fibonacci series 0 to 100
# 0 , 1,  1 , 2 , 3 , 5,  8,  13,  21
# 0 + 1 = 1
#     1 + 1 = 2
#         1 + 2 = 3
#             2 + 3 = 5
#                 3 + 5 = 8
#                     5 + 8 = 13
#                         8 + 13 = 21 
#collection of data/values list
#allows duplicate
#mutable(can change)

# lst = [1,2,3,4,3,3]
# lst.append(5)#it add the element at the end of the list
# print(lst)
# #lst.clear()#it clear the element of the lst
# lst2 = lst.copy()#it copy the entire list
# print(lst2.count(3))#it count the element presnt in list
# #extend->do ot by your own self
# print(lst2.index(5))#it gives a index value of an element
# lst2.insert(2,8)#add value at given index inser(index, value)
# print(lst2.pop())
# print(lst2)
# print(dir(lst))

# lst = [1,6,7,8,2,3,4,5]
# print(dir(lst))
# print(lst.pop())
# lst.reverse()
# lst.sort()
# print(lst)
lst = []
for i in range(0,5):
    lst.append(int(input("Enter a number:")))


# for i in lst:
#     print(i)
lenoflst = len(lst)
max = lst[0]
for i in range(0,lenoflst):
    if(max < lst[i]):
        max = lst[i]

print(max)