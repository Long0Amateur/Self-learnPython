print('Excercise 1')
# Print a number pattern using a for loop and range function
x = eval(input('Enter total number to print:'))
for num in range(x):
    for i in range(num):
        print(num,end=' ') # print number
    print('\n') # new line after each row to display pattern correctly

print('Excercise 2')
# Triangular half pyramid number pattern
print('Second number pattern')
lastNumber = 6
for row in range(1,lastNumber):
    for column in range (1, row):
        print(column, end=' ') #print column number and give spaces between them
    print('\n') # new line after each row to display pattern correctly
    


