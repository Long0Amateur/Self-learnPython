# List comprehension


# A program generates a list L of 50 random numbers between 1 and 100
from random import randint

L = [randint(1,100) for i in range(50)]
print(L,'\n')
N = L[:]
P = L[:]
# A program replaces each element in a list L with its square
L = [ i*2 for i in L]
print(L,'\n')


# A program counts how many items in list L are greater than 50

N = [  i for i in N if i >= 50 ]
print(N,'\n')


# A program creates a new list whose first element is how many ones are in L,
# whose second elements is how many twos are in L

frequencies = [ P.count(i) for i in range(1,101) ]
print(frequencies)
