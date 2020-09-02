# A program counts how many squares of the numbers from 1 to 100
# end in a 1

count = 0
for i in range(1,101):
    if(i**2)%10 == 1:
        count = count + 1
        print(i, i**2)

print('There are',count,'numbers which are squares of 1 to 100 end in 1')
