# Using a for loop, create the list below, with increasing zeros
# The last two ones should be separated by ten zeros

# [1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1...]

L = []
for i in range(11):
    L.append(1)
    for j in range(i):
        L.append(0)
P = L + [1]
print(P)


# https://www.pythonforbeginners.com/basics/list-comprehensions-in-python

N = [int(y==0) for x in range(12) for y in range(x)]+[1]

print(N)



