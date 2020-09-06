# A program asks user to enter a list containing numbers between 1 and 12.
# Then, it replaces all entries in the list are greater than 10 with 10

from random import randint

L = []
for i in range(10):
    L.append(randint(1,12))
print(L)

for j in range(len(L)):
    if L[j] > 10:
        L[j] = 10
print(L)
