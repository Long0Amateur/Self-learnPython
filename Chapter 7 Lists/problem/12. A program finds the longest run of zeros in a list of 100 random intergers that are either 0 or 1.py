# A program generates 100 random integers that are either 0 or 1, and then
# find the longest run of zeros
# i.e [1,0,1,1,0,0,0,0,1,0,0] the longest run of zeros is 4

# Visit: https://codereview.stackexchange.com/questions/219872/program-for-
# finding-longest-run-of-zeros-from-a-list-of-100-random-integers-whic

from random import randint
import itertools

def group_zero(L):
    count = 0
    for j in L:
        if j == 0:
            count+=1
        else:
            yield count
            count = 0

def itertool_group_zero(L):
    return max(len(list(g)) for k, g in itertools.groupby(L) if k == 0)

L = []
for i in range(100):
    L.append(randint(0,1))
          
print(L,'\n')
        
print('The longest run of zeros:',max(group_zero(L)))

print('Alternate approach via itertools:',itertool_group_zero(L))
