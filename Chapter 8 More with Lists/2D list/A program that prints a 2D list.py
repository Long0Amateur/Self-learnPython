# A program that prints a 2D list

# Visit: https://snakify.org/en/lessons/two_dimensional_lists_arrays/

from pprint import pprint

L =[[1,2,3],[4,5,6],[7,8,9]]

for r in range(len(L)):    
    for c in range(len(L[r])): 
        print(L[r][c],end='')
    print()

print('Shorter via pretty print:\n')
pprint(L)  
