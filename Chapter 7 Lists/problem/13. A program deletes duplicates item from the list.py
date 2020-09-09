# A program removes repeated items from a list
# i.e [1,1,2,3,4,3,0,0] => [1,2,3,4,0]

# Visit: https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/


from random import randint

L = []
for i in range(10):
    L.append(randint(0,3))
print(L)

# Naive method
remove_dup = []
for j in L:
    if j not in remove_dup:
        remove_dup.append(j)

print('The list after removing duplicated elements:\n',remove_dup)

# List comprehension + enumerate()
remove_dup2 = [ i for n, i in enumerate(L) if i not in L[:n] ]

print('Via enumerate:\n',remove_dup2)
