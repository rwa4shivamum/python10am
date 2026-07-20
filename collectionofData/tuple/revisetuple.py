"""--------------------------------Tuple----------------------------------
1.orderd
2.immutable
3.Hetrogenous
4.indexing and slicing
5. nested tuple
6. memory efficient
"""

# Creating a tuple
my_tuple = (1, 2, 3, "hello", 4.5)
# Slicing the tuple
subset = my_tuple[1:4]  # Output: (2, 3, "hello")
#my_tuple[3] = "world" #tuple is immputable
print(my_tuple)
# del  my_tuple

#method of tuple
print(my_tuple.count(1))
print(my_tuple.index('hello'))