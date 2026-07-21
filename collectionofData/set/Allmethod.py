# Base sets
A = {1, 2, 3}
B = {3, 4, 5}

# 1. add() → add single element
A.add(10)

# 2. clear() → remove all elements
temp = {1, 2}
temp.clear()

# 3. copy() → create copy
C = A.copy()

# 4. difference() → A - B (new set)
print(A.difference(B))

# 5. difference_update() → A = A - B
A.difference_update(B)

# 6. discard() → remove element (no error)
A.discard(2)

# 7. intersection() → common elements (new set)
print(A.intersection(B))

# 8. intersection_update() → keep only common
A.intersection_update(B)

# 9. isdisjoint() → no common elements?
print(A.isdisjoint(B))

# 10. issubset() → A ⊆ B ?
print(A.issubset(B))

# 11. issuperset() → A ⊇ B ?
print(A.issuperset(B))

# 12. pop() → remove random element
A.pop()

# 13. remove() → remove element (error if not found)
# A.remove(100)  # uncomment → error

# 14. symmetric_difference() → non-common (new set)
print(A.symmetric_difference(B))

# 15. symmetric_difference_update() → keep non-common
A.symmetric_difference_update(B)

# 16. union() → combine sets (new set)
print(A.union(B))

# 17. update() → add all elements from B into A
A.update(B)

print(A)  # final result