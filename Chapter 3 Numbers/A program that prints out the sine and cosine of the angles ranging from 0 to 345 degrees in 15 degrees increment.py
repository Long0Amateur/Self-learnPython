# A program that prints out the sine and cosine of the angles ranging from 0 to 345 degree in
# 15 degrees increments. Each result should be rounded to 4 decimal places.

from math import sin, cos, pi

for i in range(0,360,15):
    x = sin((i*pi)/180) # To convert degree to radian, multiplying by pi divided by 180
    y = cos((i*pi)/180)
    print(i, '---',round(x,4),round(y,4))
    


