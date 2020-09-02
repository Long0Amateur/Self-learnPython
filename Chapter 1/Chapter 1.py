# Example 1
print('Example 1')
print('*******************')
print('*******************')
print('*******************')
print('*******************')

print(sep='')

# Example 2
print('Example 2')
print('*******************')
print('*', '*', sep='                 ')
print('*                 *')
print('*******************')

print(sep='')

# Example 3
print('Example 3')
print('*')
print('**')
print('***')
print('****')

print(sep='')

# Example 4
print('Example 4')
x = (512-282)/(47*48+5)
print(round(x,4))

print(sep='')

# Example 5
print('Example 5')
x = eval(input('Enter a number:'))
print('The square of', x,'is',x*x)

print(sep='')

# Example 6
print('Example 6')
x = eval(input('Enter a number:'))
print(x,2*x,3*x,4*x,5*x, sep='---')

print(sep='')

# Example 7
print('Example 7')
x = eval(input('Enter weight in kilograms:'))
y = x*2.2
print(x,'kgs equals to', round(y,2),'pounds')

print(sep='')

# Example 8
print('Example 8')
x = eval(input('Enter a number:'))
y = eval(input('Enter a number:'))
z = eval(input('Enter a number:'))
total = x+y+z
average = total/3
print('The total of three values are',total)
print('The average of three values are', round(average,2))

print(sep='')

# Example 9
print('Example 9')
x = eval(input('Enter price of meal:'))
y = eval(input('Enter percent tip (%):'))
total = x+(y/100)
print('The total price of meal with', y,'% tips is',round(total,3))
