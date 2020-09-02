# A program that asks the user to enter an angle between -180 and 180.
# Using an expression with the modulo operator, convert the angle to its equivalent between 0 and 360


x = eval(input('Enter an angle between between -180 and 180:'))
print('Equivalent angle between 0 degree and 360 degree is',x%360)


