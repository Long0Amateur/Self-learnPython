x = eval(input('Enter a power:'))
x_power = 2**x
print('The last digit of 2 raised to that power is (mod the numbe by 10):',x_power % 10)

print(sep='')

x = eval(input('Enter a power:'))
x_power = 2**x
print('The last digit of 2 raised to that power is (mod the numbe by 100):',x_power % 100)

print(sep='')

x = eval(input('Enter a power:'))
y = eval(input('Enter how many digits:'))
x_power = 2**x
print('The last digit of 2 raised to that power is (mod the numbe by 10)',x_power % (10*y))




