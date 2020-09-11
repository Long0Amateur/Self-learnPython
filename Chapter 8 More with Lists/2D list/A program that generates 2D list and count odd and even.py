# A program that generates 2D list and counts how many are even/odd

from pprint import pprint

r = 10
c = 5

# Remember: L[i][j] = i*j

L = [ [ i*j for j in range(c) ] for i in range(r) ]

pprint(L)

count_odd = sum( [1 for r in range(10) for c in range(5) if L[r][c]%2 != 0])

print('Odd:%d' %count_odd)
print('Even:', (len(L) * len(L[0]))- count_odd )

