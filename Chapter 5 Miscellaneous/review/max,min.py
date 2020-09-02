# Find max,min in a series of values

print('Finding max')
x_max = eval(input('Enter a positive number:'))


for i in range(5):
    x = eval(input('Enter a positive number:'))
    if x > x_max:
        x_max = x
        flag = 1
   
if flag == 1:   
    print(x_max,'is largest number')
    
print('Finding min')
x_min = eval(input('Enter a positive number:'))

flag = 0
for i in range(5):
    x = eval(input('Enter a positive number:'))
    if x < x_min:
        x_min = x
        flag = 2 

if flag == 2:
    print(x_min,'is smallest number')
