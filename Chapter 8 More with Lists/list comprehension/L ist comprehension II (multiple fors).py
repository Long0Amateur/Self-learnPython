# Multiple fors in list comprehension


L = [ [i,j] for i in range(2) for j in range(2)]

# print [ [0,0],[0,1],[1,0],[1,1] ]

print(L)

M = [ [i,j] for i in range(4) for j in range(i) ]

# print [ [1,0],[2,0],[2,1],[3,0],[3,1],[3,2] ]

print(M[i])
