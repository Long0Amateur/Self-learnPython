# A program counts how many squares of the numbers from 1 to 100
# end in a 4
#  how many end in a 9

count = 0
for i in range (1,101):
    if (i**2)%10 == 4:
        count = count + 1
        print(i,i**2)

print('There are',count,'numbers which are squares of 1 to 100 end in 4')
print(sep='')

count = 0
for i in range (1,101):
    if (i**2)%10 == 9:
        count = count + 1
        print(i,i**2)
        
print('There are',count,'numbers which are squares of 1 to 100 end in 9')
        
