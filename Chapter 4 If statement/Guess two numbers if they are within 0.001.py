# Guess two numbers if they are close within .001 of each other

x = float(input('Enter the first number:'))
y = float(input('Enter the second number:'))

z = abs(x-y)

if z == 0.001:
    print('Close')
else:
    print('Not close')
