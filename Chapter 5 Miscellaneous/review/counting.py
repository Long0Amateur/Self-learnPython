# A progran gets 10 numbers from user and count how many of those numbers are
# greater than 10

count = 0 # define

for i in range(10):
    num = eval(input('Enter a number:'))
    if num>10:
        count=count+1
        
print('There are',count,'numbers greater than 10.')        
        
