# A program asks user enter 10 test scores



# print out the highest and lowest scores
x_max = eval(input('Enter a score:'))
x_min = eval(input('Enter a score:'))

s = 0
for i in range(10):
    x = eval(input('Enter test score:'))
    s = s + x
    if x > x_max:
        x_max = x # this is important!!!
        if x < x_max:
            
    if x < x_min:
        x_min = x
        
print('The largest score is',x_max)
print('The smallest score is',x_min)

# print out the average of the scores
print('The average of scores is',s/10)  


# print out the second largest, second smallest
