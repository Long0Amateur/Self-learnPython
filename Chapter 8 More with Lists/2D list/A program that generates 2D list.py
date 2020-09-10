# A program that generates 2D list

from pprint import pprint

r = 5
c = 6

# Remember: L[i][j] = i*j

L = [ [i*j for j in range(c)] for i in range(r)]

pprint(L)
