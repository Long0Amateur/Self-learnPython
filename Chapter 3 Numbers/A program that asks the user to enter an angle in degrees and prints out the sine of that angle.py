# A program that asks the user to enter an angle in degrees and prints out the sine of that angle

from math import sin, pi

x = eval(input('Enter an angle in degrees:'))
print(sin((x*pi)/180))
