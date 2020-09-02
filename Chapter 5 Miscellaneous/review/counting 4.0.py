# A program generates 10000 random numbers between 1 and 100 and
# counts how many of them are multiples of 12

from random import randint

count = 0
for i in range(10000):
    x = randint(1,100)
    if x%12 == 0:
        count = count + 1


print('Number of multiples of 12:',count)
