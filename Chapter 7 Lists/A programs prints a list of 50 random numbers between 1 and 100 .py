# A program generates a list L of 50 random numbers between 1 and 100

from random import randint
L = []
for i in range(50):
    L.append(randint(1,100))

print(L)
    

