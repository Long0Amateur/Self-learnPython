# Hollow diamond


x = int(input('Enter height of diamond:'))
for i in range(1,x,2):
    print(' '*(x//2 - i//2), '*'*i)

for i in range(x, 0, -2):
    print(' '*(x//2-i//2), '*'*i)
