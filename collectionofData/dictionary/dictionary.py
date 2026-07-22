# name = "kavy Patel"
# age = 17
# education = "12th Complete(pass)"
# fatherName = "Ajay Bhai"
# motherName = "bela Bhen"
# address = "bawla, Ahemadabad"

## What is Dictionary?

# - A **collection of key-value pairs**
# - Unordered, mutable, indexed by keys

kavyPatelInfo = {
    "name":'kavy Patel',
    "age":17,
    "education" : "12th Complete(pass)",
   "fatherName" : "Ajay Bhai",
   "motherName" : "bela Bhen",
   "address" : "bawla, Ahemadabad",
}


# print(kavyPatelInfo[name])
# print(kavyPatelInfo[ "education" ])#specific value getting
# print(kavyPatelInfo)#Dictionary getting
# print(kavyPatelInfo.get("age"))#by using get method
# kavyPatelInfo["city"] = "Ahemadabad" #here we are adding the additional key-value pair
# kavyPatelInfo["age"] = 20 #here we are updating the value by getting the key
# print(kavyPatelInfo)

# print(dir(kavyPatelInfo))

# # kavyPatelInfo.clear() #it clear the key-value pair but not delete the variable
# # del kavyPatelInfo
# kavyPatelBrother = kavyPatelInfo.copy()
# kavyPatelBrother["name"] = "dhey"
# print(kavyPatelInfo)
# print(kavyPatelBrother.pop("address"))
# print(kavyPatelBrother)


#Type Casting Contstructor
print(type(int("10")))        # 10
float("5.5")     # 5.5
str(100)         # "100"
list("abc")      # ['a', 'b', 'c']
tuple([1,2,3])   # (1,2,3)
set([1,1,2])     # {1,2}
dict([("a",1), ("b",2)])  # {'a':1, 'b':2}

# number = "10"
# print(type(number))
# num = int(number)
# print(type(num))
#create Read Update Delete (CRUD)
students = [
    {"id": 1, "name": "Amit"},
    {"id": 2, "name": "Neha"}
]
# lst = [1,2,3]
# print(type(lst[0]))
# print(type(students[0]))
student1 = {"id": 3, "name": "vinod"}
students.append(student1)#create new students
print(students)
students[0] = {'id': 1, 'name': 'lodhanan'} #update

# lst = [1,2,3]
# lst[1] = 4
print(students)

del students[2]
print(students)



diction = {'id': 2, 'name': 'Neha'}
# print(dir(diction))
# print(diction.fromkeys("name")) #we'll see later
# print(diction.items())
# print(diction.keys())
# # print(diction.pop('id'))
# print(diction.popitem())
# print(diction)
# print(diction.values())