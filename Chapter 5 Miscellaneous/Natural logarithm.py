# A program asks user to enter a value n, then compute ln(n)
import math
e = 2.718

x = eval(input('Enter a number:'))

s = 0
for i in range(1,x+1):
    s = s + 1/i

print('The natural logarithm of',x,'is',s)
    
y = math.log(x,e)

print('ln(',x,') is',round(y,3))
