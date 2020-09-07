# A program creating list using a for loop
import string
# A list consisting of the integers 0 through 49

L = []
for i in range(50):
    L.append(i)

print('A list consisting of the integers 0 through 49:\n',L,'\n')

# A list containing the squares of the integers 1 through 50
N = []
for j in range(1,51):
    N.append(j**2)

print('A list containing the squares of the integers 1 through 50:\n',N,'\n')

# The list['a','bb','ccc','dddd',...] that ends with 26 copies of the letter z

s = string.ascii_lowercase

print('Via enumerate method:')
print([(i+1)*char for i, char in enumerate(s)])
print('\n')

print('Via for loop method:')

M = []
length = len(s)
for z in range(0,length):
    c = s[z]*(z+1)
    M.append(c)
print(M)


