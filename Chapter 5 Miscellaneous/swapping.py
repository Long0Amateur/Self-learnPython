# A program swaps the values of 3 variables
# x gets value of y, y gets value of z, and z gets value of x

x = 1
y = 2
z = 3

hold = x
x = y
y = hold

hold = y
y = z
z = hold

hold = z
z = x
z = hold


print('Value of x =',x)
print('Value of y =',y)
print('Value of z =',z)
