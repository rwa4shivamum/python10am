n=5
# *
# **
# ***
# ****
# *****

# for i in range(1,n+1):
#     for j in range(0,i):
#         print("*", end="")
#     print("")


# for i in range(1,n+1):
#     for j in range(0,i):
#         print("*", end="")
#     print("")

#defn of function:function is a self-contained, reusable block of code designed to perform a single, specific task
def printStartPattrn(n):
    for i in range(1,n+1):
       for j in range(0,i):
          print("*", end="")
       print("")

print("Hello")
printStartPattrn(n)
printStartPattrn(7)



students = [
    {"id": 1, "name": "Amit", "marks":70},
    {"id": 2, "name": "Neha", "marks":80}
]
for i in students:
   print(i.get("name"),i.get("marks"))
