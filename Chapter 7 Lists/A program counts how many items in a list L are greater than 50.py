# A programs counts how many numbers are greater than 50.

from random import randint

L =[]
for i in range(10):
    L.append(randint(1,100))

count = 0
for item in L:
    if item > 50:
        count+=1

print(L)
print('There are',count,'numbers greater than 50.')
