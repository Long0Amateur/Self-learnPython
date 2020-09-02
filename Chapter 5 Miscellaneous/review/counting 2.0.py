# A progran gets 10 numbers from user and count how many of those numbers are
# greater than 10
# and smaller than 10
# equal to 10

count1 = 0
count2 = 0
count3 = 0

for i in range(10):
    x = eval(input('Enter a number:'))

    if x>10:
        count1 = count1 + 1
        
    elif x<10:
        count2 = count2 + 1

    elif x==10:
        count3 = count3 + 1
    

print('There are',count1,'numbers greater than 10')
print('There are',count2,'numbers lesser than 10')
print('There are',count3,'numbers equal to 10')  
        
